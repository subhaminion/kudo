from django.conf.urls import url
from django.urls import include
from django.contrib import admin
from rest_framework_nested import routers
from main.views import (
	LoginView, UserView,
	KudosView, UserKudosView,
	MeView
)

router = routers.SimpleRouter()
router.register(r'user', UserView, basename="user")
router.register(r'me', MeView, basename="me")
router.register(r'kudo', KudosView, basename="kudo")

user_kudos_router = routers.NestedSimpleRouter(router, r'user', lookup='user')
user_kudos_router.register(r'kudos', UserKudosView, basename='user-kudos')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/login/', LoginView.as_view()),
    url(r'^api/', include(router.urls)),
    url(r'^api/', include(user_kudos_router.urls)),
]
