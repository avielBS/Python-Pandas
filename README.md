### Python-Pandas 

This is the cli for analyzing the data of the rated movies by the users

## Usage: 
```bash
analyzer [OPTIONS] COMMAND [ARGS]...
```
##Commands:
#### Compare two movies by their title
```bash
Usage: analyzer compare_two_movies_by_title [OPTIONS]

  compare between two movies by their ratings

Options:
  -t1, --title1 TEXT    The title of the first movie
  -t2, --title2 TEXT    The title of the second movie
  -g, --graphical TEXT  Show results in graph
  --help                Show this message and exit.
```

#### Get the average age of users rated a movie

```bash
Usage: analyzer get_average_age [OPTIONS]

  Get average age of users rated a specific movie by title

Options:
  -t, --title TEXT  The title of the movie
  --help            Show this message and exit.
```

#### Get average ratings of the movies in the dataset

```bash
Usage: analyzer get_average_ratings [OPTIONS]

  Get average ratings for the movies

Options:
  -g, --graphical TEXT  Show results in graph
  -e, --end TEXT        Maximum rating to fetch
  -b, --begin TEXT      Minimum rating to fetch
  -s, --sort TEXT       Sort type ascending or descending
  -h, --head TEXT       Number of items to retrieve
  --help                Show this message and exit.
```

#### Get the highest rated movies

```bash
Usage: analyzer get_highest_rated_movies [OPTIONS]

  get the highest rated movie

Options:
  -h, --head INTEGER    Number of items to retrieve
  -g, --graphical TEXT  Show results in graph
  --help                Show this message and exit.
```

#### Get the lowest rated movies
```bash
Usage: analyzer get_lowest_rated_movies [OPTIONS]

  get the lowest rated movie

Options:
  -h, --head INTEGER    Number of items to retrieve
  -g, --graphical TEXT  Show results in graph
  --help                Show this message and exit.
```
#### Get average rating for specific movie
```bash
Usage: analyzer get_rating_of_movie [OPTIONS]

  Get average ratings for a specific movie

Options:
  -t, --title TEXT  The title of the movie
  --help            Show this message and exit.
```

#### Get ratings of a specific user for a specific movie
```bash
Usage: analyzer get_rating_of_user_for [OPTIONS]

  Get ratings of a particular user for a specific movie

Options:
  -u, --userID TEXT  The user id of the user you want to get info for
  -t, --title TEXT   The title of the movie
  --help             Show this message and exit.
```

#### Get the joined table of ratings and movies
```bash
Usage: analyzer get_ratings_movies [OPTIONS]

  Get a joined table of ratings and movies

Options:
  --help  Show this message and exit.
```

#### Get the joined table of ratings and users
```bash
Usage: analyzer get_ratings_users [OPTIONS]

  Get a joined table of ratings and users

Options:
  --help  Show this message and exit.
```

#### Get the joined table of ratings, movies and users
```bash
Usage: analyzer get_ratings_movies_users [OPTIONS]

  Get a joined table of ratings, movies and users

Options:
  --help  Show this message and exit.
```

#### Get users info for a specific user
```bash
Usage: analyzer get_user_info [OPTIONS]

  Get info about a user by its id

Options:
  -u, --userID TEXT  The user id of the user you want to get info for
  --help             Show this message and exit.
```

#### Get users movie count
```bash
Usage: analyzer get_user_movie_count [OPTIONS]

  Get the users average rating for all the movies he rated

Options:
  -u, --userID TEXT  The user id of the user you want to get info for
  --help             Show this message and exit.
```

#### Get the average ratings of user to his movies
```bash
Usage: analyzer get_user_rating_average [OPTIONS]

  Get the users average rating for all the movies he rated

Options:
  -u, --userID TEXT  The user id of the user you want to get info for
  --help             Show this message and exit.
```

#### List all the movies a user has rated
```bash
Usage: analyzer list_rated_movies [OPTIONS]

  Lists the movies a particular user has rated

Options:
  -g, --graphical TEXT  Show results in graph
  -u, --userID TEXT     The user id of the user you want to get info for
  --help                Show this message and exit.
```
