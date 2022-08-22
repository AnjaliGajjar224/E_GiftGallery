from django.contrib import admin
from django.urls import include, path

from .views import AddBook, ViewBook , DetailBook , DeleteBook , UpdateBook


urlpatterns = [
    path('add/',AddBook.as_view(),name='add_Bookes'),
    path('view/',ViewBook.as_view(),name='view_Bookes'),
    path('<int:pk>/view/',DetailBook.as_view(),name='detail_Bookes'),
    path('<int:pk>/delete/',DeleteBook.as_view(),name='delete_Bookes'),
    path('<int:pk>/update/',UpdateBook.as_view(),name='update_Bookes'),

]