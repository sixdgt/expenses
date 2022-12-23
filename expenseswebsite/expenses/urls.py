from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="expenses"),
    path('add-expense', views.add_expense, name="expense.add"),
    path('edit-expense/<int:id>/', views.edit_expense, name="expense.edit"),
    path('delete-expense/<int:id>/', views.delete_expense, name="expense.delete"),
]