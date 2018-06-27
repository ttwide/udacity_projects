import webbrowser


class Movie(object):
    """ This class provides a way to store movie related information"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, audience_score):
        """Initializes the movie instance.
        Arguments:
        movie_title: title of the movie
        movie_storyline: brief summary of the movie
        poster_image: image of the movie poster_image
        trailer_youtube: the official trailer on youtube
        audience_score: the audience rated scores from www.rottentomatoes.com
        Returns:
        None
        """

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.audience_score = audience_score

    def show_trailer(self):
        """shows official movie trailer
        Arguments: the movie (when user clicks on the movie poster)
        Returns: opens a browser window for movie and displays official trailer
        from youtube
        """
        webbrowser.open(self.trailer_youtube_url)
