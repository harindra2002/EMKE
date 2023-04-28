from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('',views.home,name='home'),
    path('login/', views.login_doctor, name='login'),
    path('signup/',views.signup_doctor, name='signup'),
    path('signup/verify_doctor',views.verify_doctor,name='verify'),
    path('doc_home/',views.verify_login,name='verify_login'),
    path('add_patient/',views.add_patient,name='add_patient'),
    path('view_patients/',views.view_patients,name='view_patients'),
    path('save_patients/',views.save_patient,name='save_patient'),
    path('get_records/',views.get_records,name='get_record')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)