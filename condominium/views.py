from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .models import FlatResident
from .forms import FlatResidentForm, FlatResidentDeleteForm

# Create your views here.

def homepage(request):
    return render(request, 'condominium/homepage.html')


def resident_book(request):
    residents = FlatResident.objects.select_related('flat').select_related('flat__building').all()
    return render(request, 'condominium/resident-book.html', {'residents': residents})


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
        messages.warning(request, f"Данните {resident.first_name} {resident.last_name} за бяха успешно обновени!")
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

