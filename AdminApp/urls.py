
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name="Dashboard"),
    path('orders', views.orders,name="orders"),
    path('orderviews',views.orderviews,name='ordersview'),
    path('settings',views.settings,name='settings'),
    path('notifications',views.notifications,name='notifications'),
    path('clientmessage',views.clientmessage,name='clientmessage'),
    path('logos',views.logos,name='logos'),
    path('categoryview',views.categoryview,name='categoryview'),
    path('categorydata',views.categorydata,name='categorydata'),
    path('categoryinsert',views.categoryinsert,name='categoryinsert'),
    path('categoryupdatedata',views.categoryupdatedata,name='categoryupdatedata'),
    path('delcategory',views.delcategory,name='delcategory'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('updatelogodata',views.updatelogodata,name='updatelogodata'),
    path('accept/<int:id>',views.accept,name='accept'),
    path('logoupdate/<int:id>',views.logoupdate,name='logoupdatepage'),
    path('deletelogo/<int:id>',views.deletelogo,name='deletelogo')


]