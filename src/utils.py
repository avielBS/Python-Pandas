import pandas as pd


class Utils:

    @staticmethod
    def get_data_dict():
        return {
            "movies": Utils.get_movies(),
            "ratings": Utils.get_ratings(),
            "users": Utils.get_users()
        }

    @staticmethod
    def get_movies():
        return Utils.__read_csv__('../resources/movies.dat', names=['MovieID', 'Title', 'Genres'])

    @staticmethod
    def get_ratings():
        return Utils.__read_csv__('../resources/ratings.dat',
                                  names=['UserID', 'MovieID', 'Rating', 'Timestamp']).iloc[:, 0:3]

    @staticmethod
    def get_users():
        return Utils.__read_csv__('../resources/users.dat',
                                  names=['UserID', 'Gender', 'Age', 'Occupation', 'Zip-Code']).iloc[:, 0:3]

    @staticmethod
    def __read_csv__(filename, sep="::", names=None):
        return pd.read_csv(filename, sep=sep, engine='python', names=names)
