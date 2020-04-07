import click
import sys
from tkinter import *
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
@click.option("-o", "--output", "output_file", default=sys.stdout, type=click.File(mode="w"), help="Output file")
@analyzer.command()
def get_user_info(userid, output_file):
    """Get info about a user by its id"""
    click.echo(data_analyzer.get_info_for(int(userid)), file=output_file)


@click.option('-t', '--title', help='The title of the movie')
@click.option("-o", "--output", "output_file", default=sys.stdout, type=click.File(mode="w"), help="Output file")
@analyzer.command()
def get_average_age(title, output_file):
    """Get average age of users rated a specific movie by title"""
    click.echo(data_analyzer.get_raters_avg_age(title), output_file)


@click.option('-u', '--userID', help='The user id of the user you want to get info for')
@click.option('-h', '--head', default=10, help='Number of items to retrieve')
@click.option('-g', '--graphical', default='false', help='Show results in graph')
@click.option("-o", "--output", "output_file", default=sys.stdout, type=click.File(mode="w"), help="Output file")
@analyzer.command()
def list_rated_movies(userid, graphical, head, output_file):
    """Lists the movies a particular user has rated"""
    if use_graphical(graphical):
        click.echo(data_analyzer.get_users_rated_movies(int(userid), int(head), use_graphical(graphical)))
    else:
        click.echo(data_analyzer.get_users_rated_movies(int(userid), int(head), False), file=output_file)


@click.option('-u', '--userID', help='The user id of the user you want to get info for')
@click.option("-o", "--output", "output_file", default=sys.stdout, type=click.File(mode="w"), help="Output file")
@analyzer.command()
def get_user_rating_average(userid, output_file):
    """Get the users average rating for all the movies he rated"""
    click.echo(data_analyzer.get_user_rating_average(int(userid)), file=output_file)


@click.option('-u', '--userID', help='The user id of the user you want to get info for')
@click.option("-o", "--output", "output_file", default=sys.stdout, type=click.File(mode="w"), help="Output file")
@analyzer.command()
def get_user_movie_count(userid, output_file):
    """Get the number of movies he rated"""
    click.echo(data_analyzer.get_user_movies_count(int(userid)), file=output_file)


@click.option('-t', '--title', help='The title of the movie')
@click.option('-u', '--userID', help='The user id of the user you want to get info for')
@click.option("-o", "--output", "output_file", default=sys.stdout, type=click.File(mode="w"), help="Output file")
@analyzer.command()
def get_rating_of_user_for(userid, title, output_file):
    """Get ratings of a particular user for a specific movie"""
    click.echo(data_analyzer.get_user_ratings_for(int(userid), title), file=output_file)


@click.option('-h', '--head', default=None, help='Number of items to retrieve')
@click.option('-s', '--sort', default='descending', help='Sort type (ascending or descending)')
@click.option('-b', '--begin', default=1, help='Minimum rating to fetch')
@click.option('-e', '--end', default=5, help='Maximum rating to fetch')
@click.option('-g', '--graphical', default='false', help='Show results in graph')
@click.option("-o", "--output", "output_file", default=sys.stdout, type=click.File(mode="w"), help="Output file")
@analyzer.command()
def get_average_ratings(head=None, sort=None, begin=None, end=None, graphical='false', output_file=sys.stdout):
    """Get average ratings for the movies"""
    if use_graphical(graphical):
        click.echo(
            data_analyzer.get_average_ratings(int(head), sort, float(begin), float(end), use_graphical(graphical)))
    else:
        click.echo(
            data_analyzer.get_average_ratings(int(head), sort, float(begin), float(end), False), file=output_file)


@click.option('-t', '--title', help='The title of the movie')
@click.option("-o", "--output", "output_file", default=sys.stdout, type=click.File(mode="w"), help="Output file")
@analyzer.command()
def get_rating_of_movie(title, output_file):
    """Get average ratings for a specific movie"""
    click.echo(data_analyzer.get_rating_of(title), output_file)


@analyzer.command()
@click.option('-h', '--head', default=10, help='Number of items to retrieve')
@click.option('-g', '--graphical', default='false', help='Show results in graph')
@click.option("-o", "--output", "output_file", default=sys.stdout, type=click.File(mode="w"), help="Output file")
def get_highest_rated_movies(head, graphical, output_file):
    """get the highest rated movie"""
    if use_graphical(graphical):
        click.echo(data_analyzer.get_highest_rated_movies(int(head), use_graphical(graphical)))
    else:
        click.echo(data_analyzer.get_highest_rated_movies(int(head), False), file=output_file)


@analyzer.command()
@click.option('-h', '--head', default=10, help='Number of items to retrieve')
@click.option('-g', '--graphical', default='false', help='Show results in graph')
@click.option("-o", "--output", "output_file", default=sys.stdout, type=click.File(mode="w"), help="Output file")
def get_lowest_rated_movies(head, graphical, output_file):
    """get the lowest rated movie"""
    if use_graphical(graphical):
        click.echo(data_analyzer.get_lowest_rated_movies(int(head), use_graphical(graphical)))
    else:
        click.echo(data_analyzer.get_lowest_rated_movies(int(head), False), output_file)


@analyzer.command()
@click.option('-t1', '--title1', help='The title of the first movie')
@click.option('-t2', '--title2', help='The title of the second movie')
@click.option('-g', '--graphical', default='false', help='Show results in graph')
@click.option("-o", "--output", "output_file", default=sys.stdout, type=click.File(mode="w"), help="Output file")
def compare_two_movies_by_title(title1, title2, graphical, output_file):
    """compare between two movies by their ratings"""
    if use_graphical(graphical):
        click.echo(data_analyzer.compare_two_movies_by_title(title1, title2, use_graphical(graphical)))
    else:
        click.echo(data_analyzer.compare_two_movies_by_title(title1, title2, False), file=output_file)


def use_graphical(graphical):
    return graphical.lower() in ['true', '1', 't', 'y', 'yes']


if __name__ == "__main__":
    analyzer()
