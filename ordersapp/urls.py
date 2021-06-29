import ordersapp.views as ordersapp
from django.urls import path

app_name = "ordersapp"

urlpatterns = [
    path('verify/<email>/<key>/', ordersapp.verify, name='verify'),

]