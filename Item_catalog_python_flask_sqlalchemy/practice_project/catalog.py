from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, SportCategory, SportItem, User
from flask import session as login_session, jsonify
import random
import string
import os

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)


CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Catalog App"


engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create anti-forgery state token
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase +
                                  string.digits) for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already '
                                            'connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id
    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += (' " style = "width: 300px; height: 300px;border-radius: '
               '150px;-webkit-border-radius: 150px;-moz-border-radius: '
               '150px;"> ')
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output


def createUser(login_session):
    newUser = User(name=login_session['username'],
                   email=login_session['email'],
                   picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


@app.route('/gdisconnect')
def gdisconnect():
    access_token = login_session.get('access_token')
    if access_token is None:
        print 'Access Token is None'
        response = make_response(json.dumps('Current user not connected.'),
                                 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    print 'In gdisconnect access token is %s', access_token
    print 'User name is: '
    print login_session['username']
    url = ('https://accounts.google.com/o/oauth2/revoke?token=%s'
           % login_session['access_token'])
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print 'result is '
    print result
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    else:
        response = make_response(json.dumps('Failed to revoke token for given '
                                 'user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response


@app.route('/')
@app.route('/catalog')
def catalogWelcome():
    categories = session.query(SportCategory).all()
    if 'username' not in login_session:
        return render_template('publiccategory.html', categories=categories)
    else:
        return render_template('category.html', categories=categories)


@app.route('/catalog/<name>/items')
def singleCategoryItems(name):
    categories = session.query(SportCategory).all()
    catItems = session.query(SportItem).filter_by(sportcategory_name=name
                                                  ).all()
    if 'username' not in login_session:
        return render_template('publicindividual_category.html', name=name,
                               catItems=catItems)
    else:
        return render_template('individual_category.html', name=name,
                               catItems=catItems)


@app.route('/catalog/<name>/<item>')
def showSingleItem(name, item):
    category = session.query(SportCategory).filter_by(name=name).one()
    singleItem = session.query(SportItem).filter_by(name=item).one()
    if 'username' not in login_session:
        return render_template('publicindividual_item.html', category=category,
                               singleItem=singleItem)
    else:
        return render_template('individual_item.html', category=category,
                               singleItem=singleItem)


@app.route('/catalog/new', methods=['GET', 'POST'])
def newItem():
    categories = session.query(SportCategory).all()
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        newCatalogItem = SportItem(name=request.form['name'],
                                   description=request.form['description'],
                                   price=request.form['price'],
                                   sportcategory_name=request.form
                                   ['sportcategory_name'],
                                   user_id=login_session['user_id'])
        session.add(newCatalogItem)
        session.commit()
        return redirect(url_for('singleCategoryItems',
                                name=newCatalogItem.sportcategory_name))
    else:
        return render_template('new_individual_item.html')


@app.route('/catalog/<item>/edit', methods=['GET', 'POST'])
def editCatalogItem(item):
    editedSportItem = session.query(SportItem).filter_by(name=item).one()
    if 'username' not in login_session:
        return redirect('/login')
    if editedSportItem.user_id != login_session['user_id']:
        return ("<script>function myFunction() {alert ('You are not "
                "authorized to edit this item.  Please create your own "
                "catalog in order to edit.');}</script><body "
                "onload='myFunction()''>")
    if request.method == 'POST':
        if request.form['name']:
            editedSportItem.name = request.form['name']
        if request.form['description']:
            editedSportItem.description = request.form['description']
        if request.form['price']:
            editedSportItem.price = request.form['price']
        if request.form['sportcategory_name']:
            editedSportItem.sportcategory_name = (request.form
                                                  ['sportcategory_name'])
        session.add(editedSportItem)
        session.commit()
        return redirect(url_for('singleCategoryItems',
                        name=editedSportItem.sportcategory_name))
    else:
        return render_template('editindividualitem.html',
                               editedSportItem=editedSportItem)


@app.route('/catalog/<item>/delete', methods=['GET', 'POST'])
def deleteCatalogItem(item):
    deleteItem = session.query(SportItem).filter_by(name=item).one()
    if 'username' not in login_session:
        return redirect('/login')
    if deleteItem.user_id != login_session['user_id']:
        return ("<script>function myFunction() {alert ('You are not "
                "authorized to delete this item.  Please create your own "
                "catalog in order to delete.');}</script><body "
                "onload='myFunction()''>")
    if request.method == 'POST':
        session.delete(deleteItem)
        session.commit()
        return redirect(url_for('singleCategoryItems',
                        name=deleteItem.sportcategory_name))
    else:
        return render_template('deleteindividualitem.html',
                               deleteItem=deleteItem)


@app.route('/catalog.json')
def catalogJSON():
    items = session.query(SportItem).all()
    return jsonify(SportItem=[i.serialize for i in items])


# Refreshes the css each time you login
# Static url cache buster http://flask.pocoo.org/snippets/40/
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


# Used this extra disconnect so I could reroute to public template
@app.route('/disconnect')
def disconnect():
    gdisconnect()
    return redirect(url_for('catalogWelcome'))


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
