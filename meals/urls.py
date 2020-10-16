from django.urls import path

from .views import MealListView, MealsDetailsView

urlpatterns = [
    path('', MealListView.as_view(), name='meals_list'),
    path('<int:pk>', MealsDetailsView.as_view(), name='meals_details'),
]
