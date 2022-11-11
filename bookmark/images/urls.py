from django.urls import path
from .views import image_create, image_list, image_detail, image_like

app_name = "images"

urlpatterns = [
    path('create/', image_create, name="create"),
    path('', image_list, name='list'),
    path('detail/<int:id>/<slug:slug>/', image_detail, name='detail'),
    path('like/', image_like, name='like'),
]
