import json

from moviemanager import Movie


class MovieManager:
    def __init__(self, path):
        self.movies = []
        self.path = path

    def fetch_data(self):
        try:
            json_data = open(self.path).read()
            self.data = json.loads(json_data)

            for elem in self.data["movies"]["movie"]:
                movie = Movie(elem)
                self.movies.append(movie)
        except ValueError:
            print(ValueError)

    def add_movie(self,json):
        self.data["movies"]["movie"].append(json)
        self.savejson()

    def del_movie(self,movie_title):
        for movie in self.movies:
            if movie.title == movie_title:
                self.movies.remove(movie)
                self.del_movie_fromjson(movie_title)

        self.savejson()

    def del_movie_fromjson(self,movie_title):
        for elem in self.data["movies"]["movie"]:
            if elem["Title"] == movie_title:
                self.data["movies"]["movie"].remove(elem)

    def savejson(self):
        open(self.path, 'w').close()
        file = open(self.path, 'w')
        file.write(self.data)
        file.close()








