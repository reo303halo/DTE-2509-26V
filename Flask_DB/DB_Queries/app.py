from database import DataBase
from movie import Movie


def main():
    with DataBase() as db:
        # Get all movies from db
        movies = [Movie(*movie) for movie in db.getAllData()]

        for i in movies:
            print(i.id, i.title, i.year)




        # Get one movie from db - uses fnr to pick
        movie_data = db.getMovieById(3)

        if movie_data:
            movie = Movie(*movie_data)

            print("Id: ", movie.id)
            print("Title: ", movie.title)
            print("Duration: ", movie.duration)



if __name__ == '__main__':
    main()