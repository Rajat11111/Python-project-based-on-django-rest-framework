# from api.views.adminView import AdminLoginView
# from api.views.UploadMediaView import DeleteMediaView, UploadMediaView
from django.urls import path
from .views import *

app_name = 'onboarding'

urlpatterns = [
    path('user_detail/', User_details_list.as_view(), name='detail'),
    path('get_user/', Get_user_details.as_view(), name='user'),
    path('user_delete/', User_delete.as_view(), name='delete'),
    path('user_role/', Get_User_role.as_view(), name='role'),
    path('user_get/', Get_user.as_view(), name='userget'),
    path('product_detail/', Products_detail.as_view(), name='product_detail'),
    path('get_detail/', Get_detail_by_id.as_view(), name='get_detail'),
    path('register/', User_register.as_view(), name='user_register'),
    path('login/', User_login.as_view(), name='user_login'),
    path('get_data/', User_details_get_by_id.as_view(), name='get_data'),
    path('ticket_detail/', UserBookingRegister.as_view(), name='ticket_detail'),
    path('ticket_booking/', UserBookingLogin.as_view(), name='ticket_booking'),
    
]
