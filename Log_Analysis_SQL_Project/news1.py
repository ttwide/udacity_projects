#!/usr/bin/env python2.7
import psycopg2

DBNAME = "news"

q1_query = ("select articles.title, count (*) as views from articles, log,"
            "authors where authors.id = articles.author and path like "
            "CONCAT('%', articles.slug, '%') group by articles.title order by "
            "views desc limit 3")

q2_query = ("select authors.name, count (*) as views from authors, log, "
            "articles where authors.id = articles.author and log.path like "
            "CONCAT('%', articles.slug, '%') group by authors.name order by "
            "views desc limit 3")

q3_query = ("with total_number as (select date(time), count (*) as "
            "overall_total from log group by date(time)), total_incorrect as "
            "(select date(time), count (*) as incorrect_total from log where "
            "status = '404 NOT FOUND' group by date(time)) select date, "
            "percent_errors from (select total_number.date, "
            "ROUND(incorrect_total * 100.0 / overall_total , 2) as "
            "percent_errors from total_number, total_incorrect where "
            "total_number.date = total_incorrect.date group by "
            "total_number.date, percent_errors)as percent_errors_by_day where "
            "percent_errors > 1")

title_1 = "Top three articles by views:"
title_2 = "Top three authors by views:"
title_3 = "Days greater than 1% error: "


def connect(database_name):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        c = db.cursor()
        return db, c
    except psycopg2.Error as e:
        print "Unable to connect to database"
        sys.exit(1)


def get_query(question, title):
    """takes the query 1, 2, 3 as the input and uses the title to output the
    correct report"""
    db, c = connect(DBNAME)
    print "Opened database successfully"
    c = db.cursor()
    query = question
    c.execute(query)
    rows = c.fetchall()
    db.close()


# And let's loop over it too:
    print
    print title
    for row in rows:
        print "    ", row[0], row[1]


def question_selection():
    """takes the user input for which query the user selects and then runs the
    correct query in the get_query function"""
    print ("Select a query.  1. What are the most popular three articles of "
           "all time? 2. Who are the most popular articles authors of all "
           "time? 3. On which days did more than 1% of requests lead to "
           "errors? ")
    selection = raw_input("Choose a query 1, 2, or 3. ")
    if __name__ == '__main__':
        if selection == "1":
            get_query(q1_query, title_1)
        elif selection == "2":
            get_query(q2_query, title_2)
        else:
            get_query(q3_query, title_3)


question_selection()
