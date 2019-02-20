import webbrowser
class Movie():
    """This class provides a way to store movie related information."""
    valid_ratings = ["PG", "PG-13", "R", "TV-MA"] #Prints out a list with movie ratings

    # This function creates a way to store movie information to bypass in repeation in code with 4 args.
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #This function carries a method to open the url in a browser using the self.trailer_youtube_url instance varible.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
