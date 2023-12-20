from django.shortcuts import render,redirect
from .forms import *
from .models import *
from car.models import *
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import CreateView
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
# Create your views here.
class register(CreateView):
    template_name = 'register.html'
    form_class = register
    success_url = reverse_lazy('login')
    def form_valid(self,form):
        messages.success(self.request,'Account created successfully')
        return super().form_valid(form)

class user_login(LoginView):
    template_name = 'register.html'
    def get_success_url(self):
        return reverse_lazy('profile')
    def form_valid(self, form):
        messages.success(self.request,'Login successful')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.warning(self.request,'Wrong information provided')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context 

@login_required
def profile(request):
    data = buy_record.objects.filter(buyer=request.user)
    return render(request, 'profile.html',{'user':request.user,'data':data})

@method_decorator(login_required,name='dispatch')
class user_logout(LogoutView):
    def get_success_url(self):
        return reverse_lazy('home')
    
@login_required
def user_edit(request):
    if request.method == 'POST':
        form = edit_profile(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'Profile updated successfully')
            return redirect('profile')
    else:
        form = edit_profile(instance=request.user)
    return render(request, 'register.html', {'form': form})

@login_required
def change_pass(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Password changed')
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request,'register.html',{'form':form})
