from django.shortcuts import render,redirect
from django.views.generic import DetailView,CreateView
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

class detailpost(DetailView):
    model = car
    pk_url_kwarg = 'id'
    template_name = "detailpost.html"
    
    def post(self, request, *args, **kwargs):
        comment_form = commentform(data=self.request.POST)
        cr = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.cr = cr
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cr = self.object 
        comments = cr.comments.all()
        comment_form = commentform()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context

@method_decorator(login_required, name='dispatch')   
class buycar(DetailView):
    model = car
    pk_url_kwarg = 'id'
    template_name = "buycar.html"

    def post(self, request, *args, **kwargs):
        cr = car.objects.get(id=self.kwargs['id'])
        if cr.quantity > 0:
            buy_record.objects.create(buyer=request.user, car_bought=cr)
            cr.quantity -= 1
            cr.save()
            messages.success(request, 'Car purchased successfully')
            return redirect('profile')
        else:
            messages.warning(request, 'Car is out of stock')
            return redirect('profile')
