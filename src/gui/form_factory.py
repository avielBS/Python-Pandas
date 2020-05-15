from src.gui.forms.compare_two_movies_by_titles_and_users_count import *
from .forms.get_info_for_user_form import *
from .forms.get_average_age_of_raters_for_movie_form import *
from .forms.list_rated_movies_form import *
from .forms.get_users_rating_average_form import *
from .forms.get_users_movie_count_form import *
from .forms.get_rating_of_user_for_movie_form import *
from .forms.get_average_ratings_form import *
from .forms.get_rating_of_movie_form import *
from .forms.get_highest_rated_movies_form import *
from .forms.get_lowest_rated_movies_form import *
from .forms.compare_two_movies_by_titles_form import *
from .forms.get_movie_rated_users_count_form import *
from utils import Utils


class FormFactory:
    options = {
        'Get info for user': GetInfoForUserForm,
        'Get average age of raters for movie': GetAverageAgeOfRatersForMovieForm,
        'List rated movies': ListRatedMoviesForm,
        'Get users\' rating average': GetUsersRatingAverageForm,
        'Get user\'s movie count': GetUsersMovieCountForm,
        'Get rating of user for movie': GetRatingOfUserForMovieForm,
        'Get average ratings': GetAverageRatingsForm,
        'Get rating of movie': GetRatingOfMovieForm,
        'Get highest rated movies': GetHighestRatedMoviesForm,
        'Get lowest rated movies': GetLowestRatedMoviesForm,
        'Compare two movies by titles': CompareTwoMoviesByTitlesForm,
        'Compare two movies by titles - users counts': CompareTwoMoviesByTitlesAndUsersCountForm,
        'Get movie\'s rated user count': GetMovieRatedUsersCountForm
    }

    @staticmethod
    def get_choices():
        return FormFactory.options.keys()

    @staticmethod
    def get_form(value):
        return FormFactory.options[value].get_instance()

    @staticmethod
    def place_labels_and_entries(form, formFrame):
        for index, label in enumerate(form.labels):
            Label(formFrame, text=label).grid(row=0, column=index * 2)
            if form.dropdowns is not None and label in form.dropdowns:
                OptionMenu(formFrame, form.labels[label], *Utils.get_movie_list(), command=form.labels[label].set).grid(
                    row=0, column=index * 2 + 1)
            else:
                Entry(formFrame, textvariable=form.labels[label]).grid(row=0, column=index * 2 + 1)
