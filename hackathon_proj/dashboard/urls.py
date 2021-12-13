from django.contrib import admin
from django.urls import path
from dashboard.views import DashboardView, AddRoomsView, PriceEditView, ExecuteRPA, ImageEditView



app_name = 'dashboard'
urlpatterns = [
    path('',DashboardView.as_view(), name='dashboard-page'),
    # path('executepeekingduck/',ExecutePeekingDuck.as_view(), name='exepeekingduck'),
    path('addrooms/',AddRoomsView.as_view(), name="add-rooms"),
    path('priceupdate/<int:pk>/',PriceEditView.as_view(),name="price-edit"),
    path('imageupdate/<int:pk>/',ImageEditView.as_view(),name='image-edit'),
    path('executerpa/',ExecuteRPA.as_view(),name="exe-rpa")
]