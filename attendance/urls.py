from django.urls import path
from attendance.views import ScanView, HomeView, CreateView

app_name = "attendance"
urlpatterns = [
	path("", HomeView.as_view(), name="home"),
	path("create", CreateView.as_view(), name="create"),
	path("scan", ScanView.as_view(), name="scan"),
]
