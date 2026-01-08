from django.contrib import admin
from django.urls import path , include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from api.auth import CustomAuthToken


#Creating router object
router = DefaultRouter()

# Registered StudentViewSet with Router
router.register('studentapi', views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/',include('rest_framework.urls', namespace='rest_framework')) , # basic authentication me login ka form type khud hi show ho jata tha lakin session authentication me ye line add kar ke show ho ga wase ni ho ga
    path('gettoken/',CustomAuthToken.as_view())
]   
