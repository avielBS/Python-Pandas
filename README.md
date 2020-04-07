### Python-Pandas 

This is the cli for analyzing the data of the rated movies by the users

### GUI
To run the gui version, simply run python src/main.py

### CLI Usage: 
```bash
python src/cli.py [OPTIONS] COMMAND [ARGS]...
```
##Commands:
#### Compare two movies by their title
```bash
Usage: python src/cli.py compare-two-movies-by-title [OPTIONS]

  compare between two movies by their ratings

Options:
  -t1, --title1 TEXT     The title of the first movie
  -t2, --title2 TEXT     The title of the second movie
  -g, --graphical TEXT   Show results in graph, if -o not specified
  -o, --output FILENAME  Output file
  --help                 Show this message and exit.
```

#### Get the average age of users rated a movie

```bash
Usage: python src/cli.py get-average-age [OPTIONS]

  Get average age of users rated a specific movie by title

Options:
  -o, --output FILENAME  Output file
  -t, --title TEXT       The title of the movie
  --help                 Show this message and exit.
```

#### Get average ratings of the movies in the dataset

```bash
Usage: python src/cli.py get-average-ratings [OPTIONS]

  Get average ratings for the movies

Options:
  -o, --output FILENAME  Output file
  -g, --graphical TEXT   Show results in graph
  -e, --end INTEGER      Maximum rating to fetch
  -b, --begin INTEGER    Minimum rating to fetch
  -s, --sort TEXT        Sort type (ascending or descending)
  -h, --head TEXT        Number of items to retrieve
  --help                 Show this message and exit.

```

#### Get the highest rated movies

```bash
Usage: python src/cli.py get-highest-rated-movies [OPTIONS]

  get the highest rated movie

Options:
  -h, --head INTEGER     Number of items to retrieve
  -g, --graphical TEXT   Show results in graph
  -o, --output FILENAME  Output file
  --help                 Show this message and exit.
```

#### Get the lowest rated movies
```bash
Usage: python src/cli.py get-lowest-rated-movies [OPTIONS]

  get the lowest rated movie

Options:
  -h, --head INTEGER     Number of items to retrieve
  -g, --graphical TEXT   Show results in graph
  -o, --output FILENAME  Output file
  --help                 Show this message and exit.

```
#### Get average rating for specific movie
```bash
Usage: python src/cli.py get-rating-of-movie [OPTIONS]

  Get average ratings for a specific movie

Options:
  -o, --output FILENAME  Output file
  -t, --title TEXT       The title of the movie
  --help                 Show this message and exit.

```

#### Get ratings of a specific user for a specific movie
```bash
Usage: python src/cli.py get-rating-of-user-for [OPTIONS]

  Get ratings of a particular user for a specific movie

Options:
  -o, --output FILENAME  Output file
  -u, --userID TEXT      The user id of the user you want to get info for
  -t, --title TEXT       The title of the movie
  --help                 Show this message and exit.
```

#### Get the joined table of ratings and movies
```bash
Usage: python src/cli.py get-ratings-movies [OPTIONS]

  Get a joined table of ratings and movies

Options:
  --help  Show this message and exit.
```

#### Get the joined table of ratings and users
```bash
Usage: python src/cli.py get-ratings-users [OPTIONS]

  Get a joined table of ratings and users

Options:
  --help  Show this message and exit.
```

#### Get the joined table of ratings, movies and users
```bash
Usage: python src/cli.py get-ratings-movies-users [OPTIONS]

  Get a joined table of ratings, movies and users

Options:
  --help  Show this message and exit.
```

#### Get users info for a specific user
```bash
Usage: python src/cli.py get-user-info [OPTIONS]

  Get info about a user by its id

Options:
  -o, --output FILENAME  Output file
  -u, --userID TEXT      The user id of the user you want to get info for
  --help                 Show this message and exit.
```

#### Get users movie count
```bash
Usage: python src/cli.py get-user-movie-count [OPTIONS]

  Get the number of movies he rated

Options:
  -o, --output FILENAME  Output file
  -u, --userID TEXT      The user id of the user you want to get info for
  --help                 Show this message and exit.
```

#### Get the average ratings of user to his movies
```bash
Usage: python src/cli.py get-user-rating-average [OPTIONS]

  Get the users average rating for all the movies he rated

Options:
  -o, --output FILENAME  Output file
  -u, --userID TEXT      The user id of the user you want to get info for
  --help                 Show this message and exit.
```

#### List all the movies a user has rated
```bash
Usage: python src/cli.py list-rated-movies [OPTIONS]

  Lists the movies a particular user has rated

Options:
  -o, --output FILENAME  Output file
  -g, --graphical TEXT   Show results in graph
  -h, --head INTEGER     Number of items to retrieve
  -u, --userID TEXT      The user id of the user you want to get info for
  --help                 Show this message and exit.
```
