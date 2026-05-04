class Movie:
    def __init__(self, movie_name, director, rating):
        self.movie_name = movie_name
        self.director = director
        self.rating = rating

    def update_rating(self, rating):
        self.rating = rating

    def display(self):
        print(self.movie_name, self.director, self.rating)


movie = Movie("Inception", "Nolan", 8.5)
movie.update_rating(9.0)
movie.display()
