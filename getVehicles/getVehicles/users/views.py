from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib import messages 
from django.urls import reverse
from  django.contrib.auth.views import LoginView
from .forms import contactForm
# Create your views here.

def register(request):
    if(request.method == 'POST'):
        form = RegisterForm(request.POST)
        if(form.is_valid()):
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Welcome {username}, Your account has been registered, Thank You !!!")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request,'users/register.html',{'form':form})


def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out, Thank You !!!")
    return redirect(reverse('cars:index'))


class OwnLoginView(LoginView):
    template_name = 'users/login.html'

    def form_valid(self,form):
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        messages.success(self.request,f"Welcome!!! {username}, You have been logged In")
        return response
    
    def get_success_url(self):
        return reverse('cars:index')
    
@login_required
def getContact(request):
    form = contactForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request,"Your feedback has been submitted, Thank You for the feedback...")
        return redirect('cars:index')
    return render(request,'users/contact.html',{'form' : form})