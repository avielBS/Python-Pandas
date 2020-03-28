from utils import Utils
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class DataAnalyzer:
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
        return self.ratings_movies_users.groupby("UserID").get_group(userID)[["UserID", "MovieID", "Rating"]]

    def get_raters_avg_age(self, title):
        return self.ratings_movies_users.groupby("Title").get_group(title)['Age'].mean()

    def get_users_rated_movies(self, userID, graphical=False):
        data = self.get_info_for(userID)[["Title", "Rating"]]
        if not graphical:
            return data
        df = pd.DataFrame(data, columns=['Title', 'Rating'])
        DataAnalyzer.Plotter.plot(df, 'Title', 'Rating')

    def get_user_movies_count(self, userID):
        return self.get_info_for(userID).count()[0]

    def get_user_rating_average(self, userID):
        return self.get_info_for(userID)["Rating"].mean()

    def get_user_ratings_for(self, userID, title):
        x = self.get_users_rated_movies(userID)
        return x[x['Title'] == title]['Rating']

    def get_average_ratings(self, head=None, sort=None, start=None, end=None, graphical=False):
        average = self.ratings_movies.groupby("Title")['Rating'].mean()
        if start:
            average = average[average > start]
        if end:
            average = average[average < end]
        if sort is not None:
            average = average.sort_values(ascending=(True if sort == "ascending" else False))
        ret = average.head(head) if head is not None else average
        if not graphical:
            return ret
        print(ret)
        df = pd.DataFrame(data=[[title, average.get(title)] for title in ret.keys()], columns=['Title', 'Rating'])
        DataAnalyzer.Plotter.plot(df, 'Title', 'Rating')

    def get_rating_of(self, name):
        return self.get_average_ratings()[name]

    def get_highest_rated_movies(self, head, graphical):
        average = self.get_average_ratings(head=head, sort='descending')
        if not graphical:
            return average
        df = pd.DataFrame(data=[[title, average.get(title)] for title in average.keys()], columns=['Title', 'Rating'])
        DataAnalyzer.Plotter.plot(df, 'Title', 'Rating')

    def get_lowest_rated_movies(self, head, graphical):
        average = self.get_average_ratings(head=head, sort='ascending')
        if not graphical:
            return average
        df = pd.DataFrame(data=[[title, average.get(title)] for title in average.keys()], columns=['Title', 'Rating'])
        DataAnalyzer.Plotter.plot(df, 'Title', 'Rating')

    def compare_two_movies_by_title(self, title1, title2, graphical):
        movie1_rating = float(self.get_rating_of(title1))
        movie2_rating = float(self.get_rating_of(title2))
        if not graphical:
            return f"{title1}\t{movie1_rating}\n" \
                   f"{title2}\t{movie2_rating}"
        data = [[title1, movie1_rating],
                [title2, movie2_rating]]
        df = pd.DataFrame(data=data, columns=['Title', 'Rating'])
        DataAnalyzer.Plotter.plot(df, 'Title', 'Rating')

    class Plotter:
        @staticmethod
        def plot(data, x, y):
            data.plot.bar(x=x, y=y, rot=0)
            plt.show()
