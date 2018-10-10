from django.shortcuts import render
import markdown

blog.content = markdown.markdown(blog.content)

# Create your views here.
