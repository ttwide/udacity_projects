# ud036_StarterCode-Movie Trailer Website
Source code for a Movie Trailer website.  There are 4 files to help you create
your own favorite movie trailer website.  The end result is a webpage with your
favorite movies and their poster image.  When the user clicks on a movie
poster image the official movie trailer will play via Youtube.

## Instructions
Open the entertainment_center.py using python.  Run the file. It will display
your favorite movies.  Click on a movie poster to see its trailer.

## Files

1. media.py
2. entertainment_center.py
3. fresh_tomatoes.py
4. fresh_tomatoes.html

## Explanation of Individual Files
* media.py-media.py initializes a class called Movies.  I gave the arguments   
movie_title, movie_storyline, poster_image, trailer_youtube, audience_score.
All of the arguments are self explanatory except for audience score, which is
taken from www.rottentomatoes.com.  media.py also contains the
show_trailer function that opens the browser and displays the youtube video.

* entertainment_center.py-This is where the individual movie objects are created.
This file contains the movie title with all the individual arguments.    

* fresh_tomatoes.py-This file has the function the loads the information to be
displayed.  For example I displayed movie title, storyline, and audience.  You
will need to edit the python code to display the items desired.

* fresh_tomatoes.html-This is the html and css template designed for you use.

## Requirements

* Python 2.7 or greater
* For youtube:
  * Most recent version of Google Chrome, Firefox, MS Edge, or Safari
  * Windows 7+, Mac OS X 10.7+, or Ubuntu 10+
  * Internet connection with 1+ Mbps

## Acknowledgments
* The fresh_tomatoes.html template was provided by udacity.com  
