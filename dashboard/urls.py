from django.conf.urls import include,url

from . import views

urlpatterns = [
    # url(r'^$', views.logon,name ='logon'),
    # url(r'^admin/', admin.site.urls),
    # url(r'^inventory/', include('inventory.urls')),
    # url(r'^quote/', include('quote.urls')),
    # url(r'^lists/',include('lists.urls')),
    url(r'^$',views.home, name = 'home'),
    #url(r'^$', views.inventory, name ='inventory'),
   
]