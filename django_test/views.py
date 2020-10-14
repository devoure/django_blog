from django.shortcuts import render
#the next import is for finding your templates
from django.http import HttpResponse
#from django.shortcuts import render_to_response
from django.shortcuts import render
from article.models import Article
from django.contrib import auth
from django.views.decorators.csrf import requires_csrf_token
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django_test.forms import MyRegistrationForm
from formtools.wizard.views import SessionWizardView
from django.core.mail import send_mail
import logging
logr=logging.getLogger(__name__)
#from django.contrib.auth import logout

# Create your views here.
@requires_csrf_token
def login (request):
    c = {}
    return render (request, "login.html", c)

def auth_view (request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return redirect('/accounts/loggedin/')
    else:
        return redirect('/accounts/invalid/')

def loggedin(request):
    return render(request, 'loggedin.html',
                  {'full_name': request.user.username})
def invalid_login(request):
    return render('ivalid_login.html')

def logout(request):
    auth.logout(request)
    return render (request, 'logout.html')


@requires_csrf_token
def register_user (request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/register_success/')

    args = {}
    args['form'] = MyRegistrationForm()
    return render (request, 'register.html', args)

def register_success (request):
    return render(request, 'register_success.html')

class ContactWizard(SessionWizardView):
    template_name = "contact_form.html"

    def done(self, form_list, **kwargs):
        form_data=process_form_data(form_list)
        return render('done.html', {'form_data':form_data})
def process_form_data(form_list):
        form_data = [form.cleaned_data for form in form_list]

        logr.debug(form_data[0]['subject'])
        logr.debug(form_data[1]['sender'])
        logr.debug(form_data[2]['message'])

        send_mail(form_data[0]['subject'],
                  form_data[2]['message'],form_data[1]['sender'],['disguisedsandwich.gmail.com'], fail_silently=False)
        return form_data
