import webbrowser

class Movie():
    """Provides a way to store information about different movies"""
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Opens class instance trailer in youtube"""
        webbrowser.open(self.trailer_youtube_url)
