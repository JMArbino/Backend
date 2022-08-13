from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post

# Create your views here.

class BlogHomePageView(TemplateView):
    template_name='blog/index.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['posts']=Post.postobjects.all()
        print(context)
        return context

