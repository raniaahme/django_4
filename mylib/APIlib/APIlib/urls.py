
from django.contrib import admin
from django.urls import path
from publisher.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ApiOverview, name='home'),
    path('create/', add_items, name='add-items'),
    path('all/', view_items, name='view_items'),
    path('update/<int:pk>/', update_items, name='update-items'),
    path('item/<int:pk>/delete/', delete_items, name='delete-items'),

]

