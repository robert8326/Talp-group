from django.urls import reverse_lazy
from django.views import generic

from blog.models import Blog, Category


class BlogList(generic.ListView):
    """ Список блоков """

    queryset = Blog.objects.all().order_by('-created')
    template_name = 'index.html'


class CategoryList(generic.ListView):
    """ Список Категории """
    queryset = Category.objects.all().order_by('-created')
    template_name = 'category_list.html'


class BlogDetail(generic.DetailView):
    """ Подробности блога """
    model = Blog
    context_object_name = 'blog'
    template_name = 'blog_detail.html'


class CategoryDetail(generic.DetailView):
    """ Подробности Категории """
    model = Category
    context_object_name = 'category'
    template_name = 'category_detail.html'


class BlogCreateView(generic.CreateView):
    model = Blog
    template_name = 'blog_create.html'
    fields = '__all__'


class BLogUpdateView(generic.UpdateView):
    model = Blog
    context_object_name = 'blog'
    template_name = 'blog_update.html'
    fields = "__all__"


class CategoryUpdateView(generic.UpdateView):
    model = Category
    context_object_name = 'category'
    template_name = 'category_update.html'
    fields = "__all__"


class BlogDeleteView(generic.DeleteView):
    model = Blog
    context_object_name = 'blog'
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('home')


class CategoryDeleteView(generic.DeleteView):
    model = Category
    context_object_name = 'category'
    template_name = 'category_delete.html'
    success_url = reverse_lazy('category_list')


class CategoryCreateView(generic.CreateView):
    model = Category
    template_name = 'category_create.html'
    fields = '__all__'
