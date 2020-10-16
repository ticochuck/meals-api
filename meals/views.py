from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Meals
from .serializers import MealsSerializer


class MealListView(ListCreateAPIView):
    queryset = Meals.objects.all()
    serializer_class = MealsSerializer


class MealsDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Meals.objects.all()
    serializer_class = MealsSerializer
