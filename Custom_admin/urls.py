from django.contrib import admin
from django.urls import path, include
from Custom_admin.views import *

urlpatterns = [
    path('', admindashboard, name='admindashboard'),
    path('logout/', Logout , name='adminlogout'),
    path('stocks/', stocks, name='stocks'),
    # path('commodities/', commodities, name='commodities'),
    path('users_data/', users_data, name='users_data'),
    path('Approve/<str:username>/',Approve,name='approve'),
    path('Decline/<str:username>/',Decline,name='decline'),
    path('delete_selected_users/',delete_selected_users,name='delete_selected_users'),
    path('active_user/', active_user, name='active_user'),
    path('admintrans/', admintrans, name='admintrans' ),
    path('deactivate_user/', deactivate_user, name='deactivate_user'),
    path('adminbuyhistory/',adminbuyhistory, name='adminbuyhistory'),
    path('faq/', faq, name='faq'),
    path('error_404/', error_404, name='error_404'),
    path('contact/', contact, name='contact'),
    path('blank/', blank, name='blank'),
    path('admin_profile/', admin_profile, name='admin_profile'),
    path('commodities/silverbeesns/', silverbeesns,name="silverbeesns"),
    path('stocks/itbeesns/', itbeesns,name="itbeesns"),
    path('stocks/sbietfitns/', sbietfitns,name="sbietfitns"),
    path('stocks/niftybeesns/', niftybeesns,name="niftybeesns"),
    path('commodities/goldbeesns/', goldbeesns,name="goldbeesns"),
    # path('adminstocksdd/',adminstocksdd, name="adminstocksdropdown"),
    path('admincommoditiesdd/',admincommoditiesdd, name="admincommoditiesdropdown"),
    path('stocks/techns/', techns,name="techns"),
    path('stocks/psubnkns/', psubnkns,name="psubnkns"),
    path('stocks/nifitns/', nifitetfns,name="nifitetfns"),
    path('stocks/movaluens/', movaluens,name="movaluens"),
    path('stocks/mafangns/', mafangns,name="mafangns"),
    path('stocks/kotakns/', kotakns,name="kotakns"),
    path('stocks/itins/', itins,name="itins"),
    path('stocks/infrabeesns/', infrabeesns,name="infrabeesns"),
    path('stocks/icicib22ns/', icicib22ns,name="icicib22ns"),
    path('commodities/egoldns/', egoldns,name="egoldns"),
    path('stocks/dspq50ns/', dspq50etfns,name="dspq50etfns"),
    path('stocks/dspitns/', dspitetfns,name="dspitetfns"),
    path('stocks/cpsens/', cpseetfns,name="cpseetfns"),
    path('stocks/commoins/', commoietfns,name="commoietfns"),
    path('stocks/axistecns/', axistecns,name="axistecns"),
    path('stocks/abslnnns/', abslnn50etns,name="abslnn50etns"),
    path('admintransdetails/', adminbuydetails, name='adminbuydetails'),
    path('adminallhistory/', adminalldetails, name='adminalldetails'),
    path('adminsellhistory/', adminselldetails, name='adminselldetails'),
    
]