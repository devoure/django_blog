from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import requires_csrf_token
from django.template.context_processors import csrf
from userprofile.forms import UserProfileForm
from django.contrib.auth.decorators import login_required



# Create your views here.
@requires_csrf_token
@login_required
def user_profile(request):
    if request.method =='POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('/accounts/loggedin')
    else:
        user = request.user
        profile = user.profile
        form = UserProfileForm(instance=profile)

    args = {}
    args.update(csrf(request))

    args['form']= form

    return render(request, 'profile.html', args)




