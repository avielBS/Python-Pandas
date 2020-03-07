import pandas as pd
import matplotlib.pyplot as plt

movies = pd.read_csv('movies.dat', sep="::", engine='python', names=['MovieID', 'Title', 'Geners'])
movies = movies.set_index('MovieID')

users = pd.read_csv('users.dat', sep="::", engine='python', names=['UserID', 'Gender', 'Age', 'Occupation', 'Zip-Code'])
users = users.set_index('UserID')

ratings = pd.read_csv('ratings.dat', sep="::", engine='python', names=['UserID', 'MovieID', 'Rating', 'Timestamb'])

movies_users = ratings.join(movies, on="MovieID")
movies_users = movies_users[['UserID', 'Rating', 'Title']]

pd.set_option('display.max_columns', None)
print(movies_users)

print()
print()


movies_rating = movies_users.groupby("Title")['Rating'].mean()
movies_rating = movies_rating.head(10)

print(movies_rating)

ax = movies_rating.plot.bar(x='Title',y='Rating',rot=0)
plt.show()