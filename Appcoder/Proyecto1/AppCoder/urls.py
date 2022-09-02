from django.urls import path , include
from AppCoder.views import inicio , familiares 

    

urlpatterns = [
    path("inicio/", inicio),
    path("familiares/", familiares),
]