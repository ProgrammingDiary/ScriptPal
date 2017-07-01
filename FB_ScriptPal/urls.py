from django.conf.urls import include, url
from . import views
from .views import BotView


urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^a25abde08430f96d71d4b1f2ac0fb9e9fde64142/?$', BotView.as_view()),

]