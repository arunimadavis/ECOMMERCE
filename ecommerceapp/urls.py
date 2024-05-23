from django.urls import path
from . import views
app_name='ecommerceapp'
urlpatterns = [
    path('search/',views.searchresult,name='searchresult'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='procategorydetail'),
    path('<slug:c_slug>/',views.allproducts,name='product_by_category'),
    path('',views.allproducts,name='allproducts')
]