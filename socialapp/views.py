from django.shortcuts import render,redirect
from django.views.generic import CreateView,FormView,ListView
from socialapp.models import Myuser,Photos,Comments
from socialapp.forms import RegistrationForm,LoginForm,PhotoForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout


# Create your views here.

from django.views.generic import TemplateView

class IndexView(ListView):
    template_name='home.html'
    form_class=PhotoForm
    model=Photos
    success_url=reverse_lazy("index")
    context_object_name="posts"

class ProfileView(CreateView):
    template_name='profile.html'
    form_class=PhotoForm
    model=Photos
    success_url=reverse_lazy("index")

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    def get_queryset(self):
        return Photos.objects.all()


class RegView(CreateView):
    model=Myuser
    form_class=RegistrationForm
    template_name="registration.html"
    success_url=reverse_lazy("register") 
class LoginView(FormView):
    form_class=LoginForm
    template_name="login.html"
    def post(self,request,*args,**kw):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("index")
            else:
                return render(request,self.template_name,{"form":form})
                

def add_comment(request,*args,**kw):
    pid=kw.get("id")
    posts=Photos.objects.get(id=pid)
    comment=request.POST.get("comment")
    Comments.objects.create(User=request.user,comment=comment,photo=posts)
    return redirect("index")

def like_view(request,*args,**kw):
    post_id=kw.get("id")
    post=Photos.objects.get(id=post_id)
    post.like.add(request.user)
    post.save()
    return redirect("index")

def delete_post(request,*args,**kw):
    post_id=kw.get("id")
    Photos.objects.get(id=post_id).delete()
    return redirect("index")


def sign_out(request,*args,**kwargs):
    logout(request)
    return redirect("signin")



class UserProfileView(ListView):
    template_name="userprofile.html"
    model=Photos
    context_object_name="photo"

    def get_queryset(self):
        return Photos.objects.all().filter(user=self.request.user)


 