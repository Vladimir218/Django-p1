# Create your views here.
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm, CategoryAdminRegisterForm
from geekshop.mixin import CustomDispatchMixin
from mainapp.models import ProductCategory
from users.models import User


def index(request):
    return render(request, 'admins/admin.html')


class UserListView(ListView, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-read.html'
    context_object_name = 'users'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Пользователи'
        return context


class CategoryListView(ListView, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-category-read.html'
    context_object_name = 'categores'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Категории'
        return context


class CategoryCreateView(CreateView, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-category-create.html'
    form_class = CategoryAdminRegisterForm
    success_url = reverse_lazy('admins:admins_category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Категории'
        return context


class CategoryUpdateView(UpdateView, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-category-update-delete.html'
    form_class = CategoryAdminRegisterForm
    success_url = reverse_lazy('admins:admins_category')

    def get_context_data(self, *, object_list=None, **kwargs):
        category = self.get_object()
        context = super(CategoryUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Обновление категории'
        return context


class UserCreateView(CreateView, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admins:admins_user')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Регистрация'
        return context


class UserUpdateView(UpdateView, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admins_user')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Обновление пользователя'
        return context


class UserDeleteView(DeleteView):
    model = User
    template_name = 'admins/admin-users-read.html'
    success_url = reverse_lazy('admins:admins_user')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserDeleteView, self).dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class CategoryDeleteView(DeleteView, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-category-read.html'
    success_url = reverse_lazy('admins:admins_category')

    def delete(self, request, *args, **kwargs):
        object = ProductCategory.objects.filter(id=kwargs['pk'])
        object.delete()
        return HttpResponseRedirect('/admins/category/')


