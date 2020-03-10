import pandas as pd
import matplotlib.pyplot as plt
from src.DataAnalyzer import DataAnalyzer

data_analyzer = DataAnalyzer()

movies_grouped_by_title = data_analyzer.ratings_movies.groupby("Title")

ratings_average = data_analyzer.get_average_ratings(4)

print(f"User 1 has rated {data_analyzer.user_movies_count(1)} movies")
print(f"User 1 average rating is {data_analyzer.user_rating_average(1)}")

print(ratings_average)

print(data_analyzer.get_rating_of('1-900 (1994)'))

DataAnalyzer.Plotter.plot(ratings_average, 'Title', 'Rating')
