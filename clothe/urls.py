from django.urls import path
from clothe import views as c_views
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ 
    path('',c_views.home, name="home"),
    path('faq/',c_views.fa,name="FAQ"),
    # path('book/',c_views.book,name="book"),
    path('services/',c_views.servi,name="service"),
    path('contact/',c_views.contact,name="contact"),
    path('about/',c_views.about,name="about"),
    path('team/',c_views.team,name="team"),
    path('login/',c_views.log,name="login"),
    path('signup/',c_views.sign,name="signup"),
]