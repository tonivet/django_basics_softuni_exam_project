from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from .models import FlatResident
from .forms import FlatResidentForm, FlatResidentDeleteForm, ResidentSearchForm, ResidentRoleFilterForm

# Create your views here.

def homepage(request):
    return render(request, 'condominium/homepage.html')


def resident_book(request):
    queryset = FlatResident.objects.select_related('flat').select_related('flat__building').all().order_by('flat')
    roles = FlatResident.objects.values('role').distinct()

    search_form = ResidentSearchForm(request.GET or None)
    role_filter_form = ResidentRoleFilterForm(request.GET or None)

    if 'query' in request.GET:
        if search_form.is_valid():
            search_value = search_form.cleaned_data['query']
            queryset = queryset.filter(Q(first_name__icontains=search_value) | Q(last_name__icontains=search_value))

    if 'role' in request.GET:
        if role_filter_form.is_valid():
            role_value = role_filter_form.cleaned_data['role']
            queryset = queryset.filter(Q(role__iexact=role_value))

    p = Paginator(queryset, 10)
    page = request.GET.get('page')
    queryset = p.get_page(page)

    return render(request, 'condominium/resident-book.html', {'queryset':queryset ,'search_form': search_form, 'roles': roles})


def resident_book_create(request):
    form = FlatResidentForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, f"Данните бяха успешно добавени!")
        return redirect('resident-book')

    return render(request, 'condominium/resident-book-create.html', {"form": form})


def resident_book_edit(request, pk:int):
    resident = get_object_or_404(FlatResident, pk=pk)
    form = FlatResidentForm(request.POST or None, instance=resident)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.warning(request, f"Данните за {resident.first_name} {resident.last_name} бяха успешно обновени!")
        return redirect('resident-book')

    return render(request, 'condominium/resident-book-edit.html', {"form": form})


def resident_book_delete(request, pk:int):
    resident = get_object_or_404(FlatResident, pk=pk)
    form = FlatResidentDeleteForm(request.POST or None, instance=resident)

    if request.method == "POST" and form.is_valid():
        resident.delete()
        messages.error(request, f"Данните за {resident.first_name} {resident.last_name} бяха успешно изтрити!")
        return redirect('resident-book')

    return render(request, 'condominium/resident-book-delete.html', {"form": form})

