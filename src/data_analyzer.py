from utils import Utils
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)


class DataAnalyzer:
    """
    DataAnalyzer class for analyzing data of movie ratings by users
    """
    __instance = None

    @staticmethod
    def get_instance():
        if DataAnalyzer.__instance is None:
            DataAnalyzer()
        return DataAnalyzer.__instance

    def __init__(self):
        data_dict = Utils.get_data_dict()
        self._movies = data_dict["movies"].set_index('MovieID')
        self._users = data_dict["users"].set_index('UserID')
        self._ratings = data_dict["ratings"]
        pd.set_option('display.max_columns', None)
        if DataAnalyzer.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            DataAnalyzer.__instance = self

    @property
    def ratings_movies(self):
        """
        Returns:
            :returns the joined tables of ratings and movies on MovieID
        """
        return self._ratings.join(self._movies, on='MovieID').iloc[:, [0, 2, 3, 4]]

    @property
    def ratings_users(self):
        """
        Returns
            :returns the joined tables of ratings and users on UserID
        """
        return self._ratings.join(self._users, on='UserID')

    @property
    def ratings_movies_users(self):
        """
        Returns:
            :returns the joined tables of ratings, users and movies on UserID and MovieID
        """
        return self._ratings.join(self._users, on='UserID').join(self._movies, on='MovieID')

    def get_info_for(self, userID):
        """
        Gets info about a particular user
        Args:
            :param userID (string) - the id of the user to the get info for
        Returns:
            :returns A table contains UserID, MovieID, Title and Rating, where UserID = :param userID
        """
        try:
            return self.ratings_movies_users.groupby("UserID").get_group(userID)[
                ["UserID", "MovieID", "Title", "Rating"]]
        except (KeyError, ValueError):
            return "This user id not in users list"

    def get_raters_avg_age(self, title):
        """
        Gets the average age of raters for a particular movie
        Args:
            :param title (string) - the title of the movie
        Returns:
            :return double: The average age of users rated the movie
        """
        return self.ratings_movies_users.groupby("Title").get_group(title)['Age'].mean()

    def get_users_rated_movies(self, userID, head=None, graphical=False):
        """
        Gets all the movies a user as rated
        Args:
            :param (string) userID - the id of the user
            :param (int) head - amount of items to retrieve
            :graphical (bool) - whether or not to show the results in a graph
        Returns:
            :returns Table that includes Title and Rating columns, if graphical was not specified
        """
        try:
            data = self.get_info_for(userID)[["Title", "Rating"]]
            if head is not None:
                data = data.head(head)
            if not graphical:
                return data
            df = pd.DataFrame(data, columns=['Title', 'Rating'])
            DataAnalyzer.Plotter.plot(df, 'Title', 'Rating')
        except (KeyError, ValueError, TypeError):
            return "This user not in users list"

    def get_user_movies_count(self, userID):
        """
        Get the amount of movies the user has rated
        Args:
            :param userID (string) - the id of the user
        Returns:
            :returns (int) - the count of movies the user has rated
        """
        try:
            return self.get_info_for(userID).count()[0]
        except (KeyError, ValueError, TypeError):
            return "This user id not in users list"

    def get_user_rating_average(self, userID):
        """
        Get the users' average ratings for all the movies he rated
        Args:
            :param userID (string) - the id of the user
        Returns:
            :returns (double) - the average of ratings the user has given
        """
        try:
            return self.get_info_for(userID)["Rating"].mean()
        except (KeyError, ValueError, TypeError):
            return "This user id not in users list"

    def get_user_ratings_for(self, userID, title):
        """
        Gets the users' rating for a particular movie
        Args:
            :param userID (string) - the id of the user
            :param title (string) - the title of the movie
        Returns:
            :returns (double) - the rating of the user to the movie
        """
        x = self.get_users_rated_movies(userID)
        try:
            return x[x['Title'] == title]['Rating'].item()
        except (KeyError, ValueError, TypeError):
            return "The user not rated this movie"

    def get_average_ratings(self, head=None, sort=None, start=None, end=None, graphical=False):
        """
        Get the average ratings for all the movies by all the users
        Args:
            :param head (int) - amount of items to retrieve
            :param sort (string) - one of [desc, asc], to sort the values in descending or ascending order
            :param start (double) - Optional, rating to start from
            :param end (double) - Optional, rating to end at
            :param graphical (boolean) - Optional, whether or not to show the results graphically
        Returns:
            :returns A table with columns Title and Rating, if graphical was not specified
        """
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
        df = pd.DataFrame(data=[[title, average.get(title)] for title in ret.keys()], columns=['Title', 'Rating'])
        DataAnalyzer.Plotter.plot(df, 'Title', 'Rating')

    def get_rating_of(self, name):
        """
        Get the rating of a movie by its name
        Args:
            :param name - the title of the movie
        Returns:
            :returns (double) - the rating of the movie
        """
        return self.get_average_ratings()[name]

    def get_highest_rated_movies(self, head, graphical):
        """
        Get the highest rated movies
        Args:
            :param head (int) - the amount of movies to retrieve
            :param graphical (boolean) - whether to show the results graphically
        Returns:
            :returns A table with Title and Rating of the movies, if graphical wasn't specified
        """
        average = self.get_average_ratings(head=head, sort='descending')
        if not graphical:
            return average
        df = pd.DataFrame(data=[[title, average.get(title)] for title in average.keys()], columns=['Title', 'Rating'])
        DataAnalyzer.Plotter.plot(df, 'Title', 'Rating')

    def get_lowest_rated_movies(self, head, graphical):
        """
       Get the lowest rated movies
       Args:
           :param head (int) - the amount of movies to retrieve
           :param graphical (boolean) - whether to show the results graphically
       Returns:
           :returns A table with Title and Rating of the movies, if graphical wasn't specified
       """
        average = self.get_average_ratings(head=head, sort='ascending')
        if not graphical:
            return average
        df = pd.DataFrame(data=[[title, average.get(title)] for title in average.keys()], columns=['Title', 'Rating'])
        DataAnalyzer.Plotter.plot(df, 'Title', 'Rating')

    def compare_two_movies_by_title(self, title1, title2, graphical):
        """
        Compares the data of the movies
        Args:
            :param title1 (string) - title of movies 1
            :param title2 (string) - title of movie 2
            :param graphical (boolean) - whether to show the results graphically
        Returns:
            :returns (string) - the comparison between the two movies, if graphical was not specified
        """
        movie1_rating = float(self.get_rating_of(title1))
        movie2_rating = float(self.get_rating_of(title2))
        if not graphical:
            return f"{title1}\t{movie1_rating}\n" \
                   f"{title2}\t{movie2_rating}"
        data = [[title1, movie1_rating],
                [title2, movie2_rating]]
        df = pd.DataFrame(data=data, columns=['Title', 'Rating'])
        DataAnalyzer.Plotter.plot(df, 'Title', 'Rating')

    def get_movie_rated_users_count(self, title):
        """
        Returns the users count that rated a specific movie by its title
        Args:
            :param title (string) - the title of the movie
        Returns:
            :return: the user count
        """

        try:
            return float(self.ratings_movies_users.groupby("Title").get_group(title).count()[0])
        except Exception as e:
            return 0

    def compare_two_movies_by_title_and_users_count(self, title1, title2, graphical):
        """
        Compares the data of the movies by viewers
        Args:
            :param title1 (string) - title of movies 1
            :param title2 (string) - title of movie 2
            :param graphical (boolean) - whether to show the results graphically
        Returns:
            :returns (string) - the comparison between the two movies, if graphical was not specified
        """
        movie1_count = self.get_movie_rated_users_count(title1)
        movie2_count = self.get_movie_rated_users_count(title2)

        if not graphical:
            return f"{title1}\t{movie1_count}\n" \
                   f"{title2}\t{movie2_count}"
        data = [[title1, movie1_count],
                [title2, movie2_count]]
        df = pd.DataFrame(data=data, columns=['Title', 'Count'])
        DataAnalyzer.Plotter.plot(df, 'Title', 'Count')

    class Plotter:
        """
        Internal class for plotting data with matplotlib.pyplot
        """

        @staticmethod
        def plot(data, x, y):
            data.plot.bar(x=x, y=y, rot=0)
            plt.show()
