class Movie():
    #object of class movie created and defined.
    def __init__(self,movie_title,movie_rating,movie_release_date,poster_image,trailer_youtube):
        self.title=movie_title
        self.rating=movie_rating
        self.date=movie_release_date
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube
