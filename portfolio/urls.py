from django.urls import path

# from .views import RecipesList, RecipesDetail, BreakfastApiView, LunchApiView, DinnerApiView, RecipeCreate
from .views import PortfolioView, ContactCreate

urlpatterns = [
    path('', ContactCreate.as_view()),
]

