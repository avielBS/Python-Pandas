from .DataAnalyzer import DataAnalyzer


# movies_grouped_by_title = data_analyzer.ratings_movies.groupby("Title")
#
# ratings_average = data_analyzer.get_average_ratings(4)
#
# print(f"User 1 has rated {data_analyzer.get_user_movies_count(1)} movies")
# print(f"User 1 average rating is {data_analyzer.get_user_rating_average(1)}")
#
# print(ratings_average)
#
# print(data_analyzer.get_rating_of('1-900 (1994)'))
#
# DataAnalyzer.Plotter.plot(ratings_average, 'Title', 'Rating')
#
# print(data_analyzer.get_user_ratings_for(1, "Antz (1998)"))


if __name__ == '__main__':
    data_analyzer = DataAnalyzer()
    data_analyzer.analyzer(prog_name='analyzer')
