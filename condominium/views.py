from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, FormView
from django.urls import reverse_lazy
from django.shortcuts import render

from .models import FlatResident
from .mixin import UpdateMessageMixin, DeleteMessageMixin
from .forms import FlatResidentForm, FlatResidentDeleteForm, ResidentRoleFilterForm

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'condominium/homepage.html'


class ResidentBookListView(ListView, FormView):
    queryset = FlatResident.objects.select_related('flat').select_related('flat__building').all().order_by('flat')
    context_object_name = 'residents'
    template_name = 'condominium/resident-book.html'
    paginate_by = 7
    form_class = ResidentRoleFilterForm


class ResidentBookSearchView(ListView):
    model = FlatResident
    template_name = 'condominium/resident-book-table.html'
    context_object_name = 'residents'
    paginate_by = 3

    def get_queryset(self):
        query = self.request.GET.get('query', '')
        queryset = FlatResident.objects.all()

        if query:
            queryset = queryset.filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('query', '')
        return context
    

class ResidentBookFilterView(ListView):
    model = FlatResident
    template_name = 'condominium/resident-book-table.html'
    context_object_name = 'residents'
    paginate_by = 2

    def get_queryset(self):
        query = self.request.GET.get('role', '')
        queryset = FlatResident.objects.all()

        if query:
            queryset = queryset.filter(role=query)
    

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['role'] = self.request.GET.get('role', '')
        return context
        


class ResidentBookCreateView(SuccessMessageMixin, CreateView):
    template_name = 'condominium/resident-book-create.html'
    form_class = FlatResidentForm
    success_message = "Данните бяха успешно добавени!"
    success_url = reverse_lazy('resident-book')


class ResidentBookUpdateView(UpdateMessageMixin, UpdateView):
    model = FlatResident
    template_name = 'condominium/resident-book-edit.html'
    form_class = FlatResidentForm
    # obj is class coming form WarningMassageMixin, 
    # first_name and last_name are attributes to this class coming from the model.
    update_message = "Данните за {obj.first_name} {obj.last_name} бяха успешно обновени!"
    success_url = reverse_lazy('resident-book')


class ResidentBookDeleteView(DeleteMessageMixin, DeleteView):
    model = FlatResident
    template_name = 'condominium/resident-book-delete.html'
    form_class = FlatResidentDeleteForm
    delete_message = "Данните за {obj.first_name} {obj.last_name} бяха успешно изтрити!"
    success_url = reverse_lazy('resident-book')

    def get_initial(self):
        obj = self.get_object()
        initial = obj.__dict__.copy()
        # Include foreign key field in delete form
        initial['flat'] = obj.flat
        return initial



