from django.urls import path
from slam import views
from slam.views import (
    SlamListView,
    SlamMoreInfo
)

urlpatterns = [
    path('slamlist/<int:user_id>', SlamListView.as_view(), name='slamlist'),
    path('slamlist/<int:user_id>/<int:pk>', SlamMoreInfo.as_view(), name='slamview'),
    path('slamlist/slampage', views.slampage, name='slampage')
]