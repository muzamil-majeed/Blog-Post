from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from datetime import date
from .models import Post
from django.views import View
from django.views.generic import ListView,DetailView
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse




# def get_date(post):
#     return post.get("date")

# def home_page(request):
#     latest_post = Post.objects.all().order_by("-date")[:3] 
#     return render(request,"blog/index.html",{"posts":latest_post})
# lets use class based view

# class StartingPageView(View):
#     def get(self,request):
#         latest_posts = Post.objects.all().order_by("-date")[:3]
#         return render(request,"blog/index.html",{"posts":latest_posts})

# we can also use listView extension in class based view as below;

class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"
    
    def get_queryset(self):
        queryset = super().get_queryset()   
        data = queryset[:3]
        return data 



# def posts(request):
#     all_posts = Post.objects.all().order_by()
#     return render(request,"blog/all-posts.html",{
#         "all_posts":all_posts
#     })

class AllPosts(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"

    def get_queryset(self):
        return super().get_queryset()

# def post_detail(request,slug):
    
#     identified_post = Post.objects.get(slug = slug)
#     return render(request,"blog/post-detail.html",{
#         "post": identified_post,
#         "post_tag":identified_post.tag.all()
#     })


class PostDetailView(View):
    def get(self,request,slug):
        post = Post.objects.get(slug=slug)
        return render(request,"blog/post-detail.html",{
            "post":post,
            "post_tag": post.tag.all(),
            "comment_form":CommentForm(),
            "comments":post.comments.all().order_by("-id"),

        })


    def post(self,request,slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page",args=[slug]))
        
       
        return render(request,"blog/post-detail.html",{
            "post":post,
            "post_tag": post.tag.all(),
            "comment_form":comment_form,
            "comments":post.comments.all().order_by("-id"),
        })     




# the below is when I used detail view extension
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["post_tag"] = self.object.tag.all()
    #     context["comment_form"] = CommentForm()
    #     return context