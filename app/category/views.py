from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializer
from django.shortcuts import render, redirect
from app.category.forms.category_form import CategoryForm


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'category/add_category.html', {'form': form})


def list_categories(request):
    categories = Category.objects.all()
    return render(request, 'category/list_categories.html', {'categories': categories})