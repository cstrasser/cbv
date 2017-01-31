from django.conf.urls import url , include
from . import views
from .forms import QuoteForm ,QuoteCreate
from .views import MyQuoteCreate

urlpatterns = [
    
    #url(r'^$', views.quotedetail, name ='quotedetail'),
    url(r'^q$',view = MyQuoteCreate.as_view(),name ='QuoteView'),
    #url(r'^p/(?P<username>[\w.@+-]+)/$', profile_detail, name='about'),
    url(r'^h$', views.home, name = 'home'),
    url(r'^i$', views.qfrm, name = 'qfrm'),    
    url(r'm8', views.m8update, name ='m8update'),
    url(r'f', views.formsetView, name ='formsetView'),
    url(r'^t$', views.editbutton, name = 'testquote'),
    url(r'models',views.modelstest, name = 'modelstest'),
    #url(r'^quotedetail/$', QuoteDetail.as_view(template_name="quoteform.html")),
    #url(r'^/(?P<wargs>\w+)/$', views.quote, name='quote') 
 ]


