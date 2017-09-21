from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import Registration
from .models import profile



class IndexView(View):
	template_name = 'accounts/index.html'



class RegisterView(View):
    form_class=Registration
    template_name='accounts/register.html'


    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)

        if form.is_valid():
            user=form.save(commit=False)
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            #confirm_password=form.cleaned_data['confirm_password']
            user.set_password(password)
            user = authenticate(username=username, password=password)
            user.save()

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('accounts:profile-create')
        return render(request, self.template_name, {'form': form})

class ProfileCreate(CreateView):
    model = profile
    fields = ['fullname']
    template_name = 'accounts/create_profile.html'

