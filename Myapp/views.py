from django.shortcuts import render , get_object_or_404, redirect
from .models import Post , User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from Myapp.forms import PostForm, EditForms
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect

"""
posts = [
    {
        'author': 'Isha Singhal',
        'title': 'Blog Post 1',
        'content': 'this is my first blog post',
        'date_posted': '9th september 2023'
    },
    {
        'author': 'Jiya ',
        'title': 'Blog Post 2',
        'content': 'hello i m going to tell you',
        'date_posted': '7th september 2023'
    }
]
"""
#def home(request):
   # context={
   #    'posts' : Post.objects.all()
   # }
  #  return render(request,"home.html", context)

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))



class HomeView(ListView):
   model = Post
   template_name="home.html"
   ordering = ['-date_posted']
   

class ArticleDetailView(DetailView):
   model = Post
   template_name="article_details.html"
   
   
class UpdatePostView(UpdateView):
    model= Post
    form_class=EditForms
    template_name = "updateblog.html"
    reverse=('blog-home')
    
class DeletePostView(DeleteView):  
    model=Post
    template_name ='deleteblog.html'
    success_url = reverse_lazy('blog-home')
    

def register(request):
    if request.method == "POST":
        pDict = request.POST.copy() 
        form = UserForm(pDict)
        if form.is_valid():
            try:
                form.save()
                form = UserForm()
                #return redirect("/login/")
            except:
                pass
    else:
        
        form = UserForm()
    return render(request, "register.html" ,{'form':form})
    
def Login(request):
    if request.method == "POST":
        Dict = request.POST.copy() 
        forms = AuthenticationForm(Dict)
        user_name = request.POST['user_name']
        upwd = request.POST['upwd']
        user = authenticate(request, user_name = user_name , upwd = upwd)
        if forms.is_valid():
            try:
                forms.save()
                forms = AuthenticationForm()
               # return redirect("/home/")
            except:
                pass
    else:
        forms = AuthenticationForm()
    return render(request, "login.html" ,{'forms':forms})


def base(request):
    return render(request, "base2.html")

# class AddPostView(CreateView):
#     model = Post
#     form= PostForm()
#     template_name= "addblog.html"
#     fields = '__all__'
def AddPostView(request):
    # context = {}
    # context['form']= PostForm()
    # return render(request , "addblog.html", context)
    if request.method == "POST":
        pDict = request.POST.copy() 
        form = PostForm(pDict)
        if form.is_valid():
            try:
                form.save()
                form = PostForm()
                return redirect("blog-home")
            except:
                pass
    else: 
        form = PostForm()
    return render(request, "addblog.html" ,{'form':form})    
    




# class AddCategoryView(CreateView):
#      model = Category
#      #form= PostForm()
#      template_name= "addcategory.html"
#      fields = '__all__'
 

# Create your views here.

