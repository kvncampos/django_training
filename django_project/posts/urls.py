from django.urls import path
from . import views

# Examples of Views
# from example import views
# path('my/fancy/example/', views.example, name='my-example-view')

# from django.urls import reverse
# url = reverse('my-example-view') # will return "my/fancy/example/"

app_name = "posts"

urlpatterns = [
    path("", views.posts_lists, name="list"),
    path("<slug:slug>", views.post_page, name="page"),
]
