from django.urls import path
from . import views

app_name = "menus"
urlpatterns = [
    path(
        route="",
        view=views.MenuListView.as_view(),
        name="list",
        ),
    path(
        route='<slug:slug>/',
        view=views.MenuDetailView.as_view(),
        name='detail',
    ),
    ]
