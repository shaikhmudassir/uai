from django.urls import path
from attendance.views import *

app_name = "attendance"
urlpatterns = [
	path("", HomeView.as_view(), name="home"),
	path("create", CreateView.as_view(), name="create"), # Create QR Code
	path("scan", ScanView.as_view(), name="scan"), # Scan QR Code
	path("login", LoginView.as_view(), name="login"), # Login As Faculty
	path("register", RegisterView.as_view(), name="register"), # Register As student
  path("display", DisplayQRView.as_view(), name="display"),
  path("dashboard", DashboardView.as_view(), name="display"),
  path("atten", AttenView.as_view(), name="atten"),
  path("att_detail", AttenView2.as_view(), name="att_detail"),
]
