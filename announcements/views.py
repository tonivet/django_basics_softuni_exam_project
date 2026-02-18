from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView, FormView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import Announcements
from .forms import AnnouncementsFrom, AnnouncementsUpdateFrom, StatusFilterForm

from common.mixin import UpdateDeleteMessageMixin

# Create your views here.

class AnnouncementsListView(FormView, ListView):
    queryset = Announcements.objects.select_related('author').all().order_by('-created_at')
    context_object_name = 'announcements'
    template_name = 'announcements/announcements-list.html'
    form_class = StatusFilterForm   
    paginate_by = 7

    def get_queryset(self):
        queryset = super().get_queryset()
    
        status_filter = self.request.GET.get('status')
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = StatusFilterForm(self.request.GET or None)
        return context


class AnnouncementsCreateView(SuccessMessageMixin, CreateView):
    template_name = 'announcements/announcements-create.html'
    form_class = AnnouncementsFrom
    success_message = "Данните бяха успешно добавени!"
    success_url = reverse_lazy('announcements-list')


class AnnouncementsUpdateView(UpdateDeleteMessageMixin, UpdateView):
    model = Announcements
    template_name = 'announcements/announcements-edit.html'
    form_class = AnnouncementsUpdateFrom
    update_message = "Статуса на {obj.title} беше успешно променен!"
    success_url = reverse_lazy('announcements-list')


class AnnouncementsDeleteView(UpdateDeleteMessageMixin, DeleteView):
    model = Announcements
    template_name = 'announcements/announcements-delete.html'
    delete_message = "Съобщението беше успешно изтрито!"
    success_url = reverse_lazy('announcements-list')

