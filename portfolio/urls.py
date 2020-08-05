from django.urls import path

# from .views import RecipesList, RecipesDetail, BreakfastApiView, LunchApiView, DinnerApiView, RecipeCreate
from .views import PortfolioView, ContactCreate

urlpatterns = [
    path('', PortfolioView.as_view()),
    path('about/', PortfolioView.as_view()),
    path('portfolioList/', PortfolioView.as_view()),
    path('contact/', ContactCreate.as_view()),
]

