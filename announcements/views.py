from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView, FormView
from django.urls import reverse_lazy

from .models import Announcements
from .forms import AnnouncementsFrom, StatusFilterForm

# Create your views here.

class AnnouncementsListView(FormView, ListView):
    queryset = Announcements.objects.select_related('author').all().order_by('-created_at')
    context_object_name = 'announcements'
    template_name = 'announcements/announcements-list.html'
    form_class = StatusFilterForm
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
    
        status_filter = self.request.GET.get('status')
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        
        return queryset


class AnnouncementsCreateView(SuccessMessageMixin, CreateView):
    template_name = 'announcements/announcements-create.html'
    form_class = AnnouncementsFrom
    success_message = "Данните бяха успешно добавени!"
    success_url = reverse_lazy('announcements-list')


