from src.utils import Utils
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class DataAnalyzer:
    """
        This class should be used as the main interaction with the CLI API we are developing

        The API should include the following functions (Add what ever you like):
        1. get ratings-movies table (@method ratings_movies)
        2. get ratings-users table (@method ratings-users)
        3. get ratings-movies-users table (@method ratings-movies-users)
        4. get user info (@method get_info_for)
        5. get user movie rating count (@method user_movies_count)
        6. get user average ratings (@method user_rating_average)
        7. get average ratings for movies (@method get_average_ratings)
        8. get average rating of specific movie by title (@method get_rating_of)
        9. get users rated movies (NOT IMPLEMENTED)
        10. get average age of users rated a specific movie by title (HARD - NOT IMPLEMENTED)
        11. Get a graphical comparison (rating) between two movies by movie name
        12. get movies list/table that are rated more than x-input value (may be sorted)
        13. get the highest rated movie
        14. get the lowest rated movie
        15. get movies list/table that are rated between (min,max)-input values (may be sorted)
        ..

        The API should support the following graph plotting:
        1. movies average ratings
        2. users average ratings
        3.
    """

    def __init__(self):
        data_dict = Utils.get_data_dict()
        self._movies = data_dict["movies"].set_index('MovieID')
        self._users = data_dict["users"].set_index('UserID')
        self._ratings = data_dict["ratings"]

        pd.set_option('display.max_columns', None)

    @property
    def ratings_movies(self):
        # USERID = 0, MOVIEID = 1, RATING = 2, TITLE = 3, GENRES = 4
        return self._ratings.join(self._movies, on='MovieID').iloc[:, [0, 2, 3, 4]]

    @property
    def ratings_users(self):
        # USERID = 0, MOVIEID = 1, RATING = 2, GENDER = 3, AGE = 4
        return self._ratings.join(self._users, on='UserID')

    @property
    def ratings_movies_users(self):
        return self._ratings.join(self._users, on='UserID').join(self._movies, on='MovieID')

    def get_info_for(self, userID):
        return self.ratings_movies_users.groupby("UserID").get_group(userID)

    def user_movies_count(self, userID):
        return self.get_info_for(userID).count()[0]

    def user_rating_average(self, userID):
        return self.get_info_for(userID)["Rating"].mean()

    def get_average_ratings(self, head=None, sort=None):
        average = self.ratings_movies.groupby("Title")['Rating'].mean()
        if sort is not None:
            average = average.sort_values(ascending=(True if sort == "ascending" else False))
        return average.head(head) if head is not None else average

    def get_rating_of(self, name):
        return self.get_average_ratings()[name]

    class Plotter:
        @staticmethod
        def plot(data, x, y):
            ax = data.plot.bar(x=x, y=y, rot=0)
            plt.show()
