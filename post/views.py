from django.shortcuts import render
import post.models

def index(request):
    lists = [x for x in range(1, 100)]
    names = ['john', 'Peter']
    return render(request, 'index.html', locals())

def get_posts(request):
    object_list = post.models.Post.objects.all()
    return render(request, 'posts.html', locals())
