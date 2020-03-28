import click
from data_analyzer import DataAnalyzer

data_analyzer = DataAnalyzer()


@click.group()
def analyzer():
    """This is the cli for analyzing the data of the rated movies by the users"""


@analyzer.command()
def get_ratings_movies():
    """Get a joined table of ratings and movies"""
    click.echo(data_analyzer.ratings_movies)


@analyzer.command()
def get_ratings_users():
    """Get a joined table of ratings and users"""
    click.echo(data_analyzer.ratings_users)


@analyzer.command()
def get_ratings_movies_users():
    """Get a joined table of ratings, movies and users"""
    click.echo(data_analyzer.ratings_movies_users)


@click.option('-u', '--userID', help='The user id of the user you want to get info for')
@analyzer.command()
def get_user_info(userid):
    """Get info about a user by its id"""
    click.echo(data_analyzer.get_info_for(int(userid)))


@click.option('-t', '--title', help='The title of the movie')
@analyzer.command()
def get_average_age(title):
    """Get average age of users rated a specific movie by title"""
    click.echo(data_analyzer.get_raters_avg_age(title))


@click.option('-u', '--userID', help='The user id of the user you want to get info for')
@click.option('-g', '--graphical', default='false', help='Show results in graph')
@analyzer.command()
def list_rated_movies(userid, graphical):
    """Lists the movies a particular user has rated"""
    click.echo(data_analyzer.get_users_rated_movies(int(userid), graphical))


@click.option('-u', '--userID', help='The user id of the user you want to get info for')
@analyzer.command()
def get_user_rating_average(userid):
    """Get the users average rating for all the movies he rated"""
    click.echo(data_analyzer.get_user_rating_average(int(userid)))


@click.option('-u', '--userID', help='The user id of the user you want to get info for')
@analyzer.command()
def get_user_movie_count(userid):
    """Get the users average rating for all the movies he rated"""
    click.echo(data_analyzer.get_user_movies_count(int(userid)))


@click.option('-t', '--title', help='The title of the movie')
@click.option('-u', '--userID', help='The user id of the user you want to get info for')
@analyzer.command()
def get_rating_of_user_for(userid, title):
    """Get ratings of a particular user for a specific movie"""
    click.echo(data_analyzer.get_user_ratings_for(int(userid), title))


@click.option('-h', '--head', default=None, help='Number of items to retrieve')
@click.option('-s', '--sort', default='descending', help='Sort type (ascending or descending)')
@click.option('-b', '--begin', default=None, help='Minimum rating to fetch')
@click.option('-e', '--end', default=None, help='Maximum rating to fetch')
@click.option('-g', '--graphical', default='false', help='Show results in graph')
@analyzer.command()
def get_average_ratings(head=None, sort=None, begin=None, end=None, graphical='false'):
    """Get average ratings for the movies"""
    click.echo(data_analyzer.get_average_ratings(int(head), sort, float(begin), float(end), bool(graphical)))


@click.option('-t', '--title', help='The title of the movie')
@analyzer.command()
def get_rating_of_movie(title):
    """Get average ratings for a specific movie"""
    click.echo(data_analyzer.get_rating_of(title))


@analyzer.command()
@click.option('-h', '--head', default=10, help='Number of items to retrieve')
@click.option('-g', '--graphical', default='false', help='Show results in graph')
def get_highest_rated_movies(head, graphical):
    """get the highest rated movie"""
    click.echo(data_analyzer.get_highest_rated_movies(int(head), bool(graphical)))


@analyzer.command()
@click.option('-h', '--head', default=10, help='Number of items to retrieve')
@click.option('-g', '--graphical', default='false', help='Show results in graph')
def get_lowest_rated_movies(head, graphical):
    """get the lowest rated movie"""
    click.echo(data_analyzer.get_lowest_rated_movies(int(head), bool(graphical)))


@analyzer.command()
@click.option('-t1', '--title1', help='The title of the first movie')
@click.option('-t2', '--title2', help='The title of the second movie')
@click.option('-g', '--graphical', default='false', help='Show results in graph')
def compare_two_movies_by_title(title1, title2, graphical):
    """compare between two movies by their ratings"""
    click.echo(data_analyzer.compare_two_movies_by_title(title1, title2, bool(graphical)))
