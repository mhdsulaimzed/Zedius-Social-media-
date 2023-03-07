from django.shortcuts import render, redirect
from django.views.generic import View, CreateView, UpdateView, TemplateView, ListView
from wallpage.form import SignupForm, SigninForm, UserProfileForm, PostForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from wallpage.models import UserProfile, Post, Comment
from django.urls import reverse_lazy


# Create your views here.
class SignupView(View,):
    def get(self, request, *args, **kw):
        form = SignupForm()
        return render(request, "signup.html", {"form": form})

    def post(self, request, *args, **kw):
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("log-in")
        else:
            return render(request, "signup.html", {"form": form})


class SigninView(View):
    def get(self, request, *args, **kw):
        form = SigninForm()
        return render(request, "log-in.html", {"form": form})

    def post(self, request, *args, **kw):
        form = SigninForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get("username")
            pwd = form.cleaned_data.get("password")
            usr = authenticate(request, username=uname, password=pwd)
            print(usr)
            if usr:
                login(request, usr)
                return redirect("home")
            else:
                return render(request, "log-in.html", {"form": form})


class SignoutView(View):
    def get(self, request, *args, **kw):
        logout(request)
        return redirect('log-in')


class UserProfileCreateView(CreateView):
    template_name = "profile-create.html"
    form_class = UserProfileForm
    model = UserProfile
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UserProfileUpdateView(UpdateView):
    template_name = "profile-edit.html"
    form_class = UserProfileForm
    model = UserProfile
    success_url = reverse_lazy('home')
    pk_url_kwarg = "id"


class UserProfileView(TemplateView):
    template_name = "userprofile.html"


class IndexView(CreateView, ListView):
    template_name = "index.html"
    form_class = PostForm
    model = Post
    success_url = reverse_lazy('home')
    context_object_name = 'posts'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        return Post.objects.all()


class PostDeleteView(View):
    def get(self, request, *args, **kw):
        id = kw.get("pk")
        Post.objects.filter(id=id).delete()
        return redirect('home')


class CommonUserProfile(View):
    def get(self, request, *args, **kw):
        id = kw.get("id")
        qs = UserProfile.objects.get(id=id)
        followers=qs.followers.all()
        follower_count=len(followers)
        
        if len(followers) == 0:
            is_following = False
        
        
        for f in followers:
            if f == request.user:
                is_following=True
            else:
                is_following=False
        
        context={ 
            "pro": qs,
            "follower_count":follower_count,
            "is_following" : is_following

        }

        return render(request, "otherprofile.html", context)


class LikesViews(View):
    def get(self, request, *args, **kw):
        id = kw.get("id")
        lk = Post.objects.get(id=id)
        lk.likes.add(request.user)
        lk.save()
        return redirect("home")


class CommentView(View):

    def post(self, request, *args, **kw):
        pid = kw.get("id")
        qs = Post.objects.get(id=pid)
        usr = request.user
        cbody = request.POST.get("body")
        Comment.objects.create(user=usr, post=qs, body=cbody)
        return redirect("home")


class CommentLikesViews(View):
    def get(self, request, *args, **kw):
        id = kw.get("id")
        clk = Comment.objects.get(id=id)
        clk.likes.add(request.user)
        clk.save() 
        return redirect("home")

class CommentRemove(View):
    def get(self,request,*args,**kw):
        id=kw.get("id")
        Comment.objects.filter(id=id).delete()
        return redirect("home")

# def commentdeleteview(self,request,*args,**kw)
class AddFollowers(View):
    def post(self,request,*args,**kw):
        id=kw.get("id")
        fw=UserProfile.objects.get(id=id)
        fw.followers.add(request.user)
        fw.save()
        return redirect('user-pro',fw.id) 

class RemoveFollowers(View):
    def post(self,request,*args,**kw):
        id=kw.get("id")
        fw=UserProfile.objects.get(id=id)
        fw.followers.remove(request.user)
        fw.save()
        return redirect('user-pro',fw.id)






