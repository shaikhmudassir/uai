from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views import View
import pyqrcode, io


class HomeView(View):
	def get(self, request):
		html = '<a href="create"><button>Create</button></a> <a href="scan"><button>Scan</button></a>'
		return HttpResponse(html)
	
class CreateView(View):
	def get(self, request):
		s = "{'key':'value'}"
		url = pyqrcode.create(s)
		buffer = io.BytesIO()
		url.svg(buffer, scale=10)
		return HttpResponse(buffer.getvalue())

class ScanView(TemplateView):
	def post(self, request, *args, **kwargs):
		return HttpResponse(f"{request.POST['fname']} {request.POST['lname']}")


	template_name = "attendance/index.html"

