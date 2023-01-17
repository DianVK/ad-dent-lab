from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home" ),
	path('home.html', views.home, name="home" ),
	path('contact.html', views.contact, name="contact" ),
	path('aligners.html', views.aligners, name="aligners" ),
	path('about.html', views.about, name="about" ),
	path('products.html', views.products, name="products" ),
	path('courier.html', views.courier, name="courier" ),
]
