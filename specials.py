class Movie():
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

    def __str__(self):
        return f"{self.title} ({self.year}), directed by {self.director}"
    
m1 = Movie("Inception", "Christopher Nolan", 2010)
print(m1)