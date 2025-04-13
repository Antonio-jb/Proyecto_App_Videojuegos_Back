from reviews.views import CreateReviewView, DeleteReviewView, GetAllReviews
from django.urls import path
from reviews.views import FindReviewByDateView
from reviews.views.review_view import EditReviewView, FindReviewByTitleView, FindReviewByGenreView

urlpatterns = [
     path('v1/create/review/', CreateReviewView.as_view(), name="create_review"),
     path('v1/find/review/date/', FindReviewByDateView.as_view(), name="find_review_by_date"),
     path('v1/find/review/genre/', FindReviewByGenreView.as_view(), name="find_review_by_genre"),
     path('v1/find/review/title/', FindReviewByTitleView.as_view(), name="find_review_by_title"),
     path('v1/edit/review/<int:id>/', EditReviewView.as_view(), name="edit_review"),
     path('v1/delete/review/<int:id>/', DeleteReviewView.as_view(), name="delete_review"),
     path('v1/get/reviews/', GetAllReviews.as_view(), name='get-reviews'),
]