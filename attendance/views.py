from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model, authenticate
from django.views.generic import TemplateView
from django.views import View
from django.shortcuts import render
import pyqrcode, io


class HomeView(View):

  def get(self, request):
    html = '''<a href="create"><button>Create</button></a>
            <a href="scan"><button>Scan</button></a>
            <a href="login"><button>login</button></a>
            '''
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


class LoginView(View):

  def get(self, request):
    # if 'user_id' in request.session:
    #     return HttpResponseRedirect('')

    return render(request, 'attendance/login.html', {})

  def post(self, request, *args, **kwargs):
    email = request.POST['email']
    password = request.POST['password']

    user = authenticate(email=email, password=password)
    if user is not None:
      request.session['user_id'] = user.id
      return HttpResponseRedirect('/')
    else:
      return HttpResponseRedirect('login')


class RegisterView(View):

  def post(self, request, *args, **kwargs):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    roll_no = request.POST['roll_no']
    year = request.POST['year']
    branch = request.POST['branch']
    batch = request.POST['batch']

    print(request.POST)
    return HttpResponseRedirect('login')


class LogoutView(View):

  def get(self, request):
    try:
      del request.session['user_id']
      return HttpResponseRedirect('login')
    except KeyError as e:
      print(e)
      return HttpResponseRedirect('/')
