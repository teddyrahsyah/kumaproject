from django.urls import path

from .views import homepage, servicepage, aboutpage, join_produsen, join_supplier

urlpatterns = [
    path('', homepage, name='home-page'),
    path('service/', servicepage, name='service-page'),
    path('about/', aboutpage, name='about-page'),
    path('produsen-join/', join_produsen, name='produsen-page'),
    path('supplier-join/', join_supplier, name='supplier-page'),
]
