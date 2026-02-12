from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect


from .models import Announcements
from .forms import AnnouncementsFrom, StatusFilterForm

# Create your views here.

def announcements_list(request):
    queryset = Announcements.objects.select_related('author').all().order_by('-created_at')

    status_filter_form = StatusFilterForm(request.GET or None)

    if 'status' in request.GET:
        if status_filter_form.is_valid():
            status_value = status_filter_form.cleaned_data['status']
            if status_value:
                queryset = queryset.filter(status=status_value)

    p = Paginator(queryset, 10)
    page = request.GET.get('page')
    queryset = p.get_page(page)

    return render(request, 'announcements/announcements-list.html', {'queryset': queryset, 'status_filter_form': status_filter_form})


def announcements_create(request):
    form = AnnouncementsFrom(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, f"Данните бяха успешно добавени!")
        return redirect('announcements-list')

    return render(request, 'announcements/announcements-create.html', {"form": form})
