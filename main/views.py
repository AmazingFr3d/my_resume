from django.shortcuts import render
from django.contrib import messages
from django.views import generic

from .forms import ContactForm
from .models import (
    UserProfile,
    Blog,
    Portfolio,
    Testimonial,
    Cerificate
)


# Create your views here.


class IndexView(generic.ListView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)().get_context_data(**kwargs)

        testimonials = Testimonial.objects.fileter(is_active=True)
        certificates = Cerificate.objects.filter(is_active=True)
        blog = Blog.objects.filter(is_active=True)
        portfolio = Portfolio.objects.filter(is_active=True)

        context['testimonials'] = testimonials
        context['certificates'] = certificates
        context['blog'] = blog
        context['portfolio'] = portfolio
        return context


class ContactView(generic.CreateView):
    template_name = 'main/contact.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Thank you. We will be in touch soon')
        return super().form_valid(form)


class PortfolioView(generic.ListView):
    model = Portfolio
    paginate_by = 10
    template_name = 'main/portfolio.html'

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    template_name = 'main/portfolio-detail.html'


class BlogView(generic.ListView):
    model = Blog
    paginate_by = 10
    template_name = 'main/blog.html'

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'main/blog-detail.html'
