from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView,UpdateView, DeleteView
import os



# Create your views here.
from django.views import generic
from .models import Post

def Home(request):
    return redirect("home")

#GET
class PostList(generic.ListView):
    queryset = Post.objects.all().order_by('-created_on')
    print(queryset)
    template_name = 'index.html'

#GET
class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

#POST
class PostCreate(CreateView):  
    model = Post  
    template_name = 'post_form.html'
    fields = '__all__'

#update   
class PostUpdate(UpdateView):  
    model = Post  
    template_name = 'postupdate_form.html'
    fields = '__all__'
    
#delete
class PostDelete(generic.DeleteView):
    
    model = Post
    template_name = 'post_confirm_delete.html'

    success_url = '/home'
