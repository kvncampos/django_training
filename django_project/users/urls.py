from django.urls import path
from . import views

# Examples of Views
# from example import views
# path('my/fancy/example/', views.example, name='my-example-view')

# from django.urls import reverse
# url = reverse('my-example-view') # will return "my/fancy/example/"

app_name = "users"

urlpatterns = [path("register/", views.register_view, name="register")]
