from django.contrib.messages.views import SuccessMessageMixin
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import ListView, CreateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from common.mixin import UpdateDeleteMessageMixin

from .models import DocumentsModel
from .forms import DocumentsForm

# Create your views here.

class DocumentsListView(ListView):
    model = DocumentsModel
    context_object_name = 'documents'
    template_name = 'documents/documents-list.html'


class DocumentDownloadView(View):
    def get(self, request, pk, *args, **kwargs):
        document = get_object_or_404(DocumentsModel, pk=pk)

        if not document.file:
            raise Http404("File not found.")

        return FileResponse(
            document.file.open(),
            as_attachment=True,
            filename=document.file.name.split("/")[-1]
        )

class DocumentCreateView(SuccessMessageMixin, CreateView):
    template_name = 'documents/documents-create.html'
    form_class = DocumentsForm
    success_message = "Данните бяха успешно добавени!"
    success_url = reverse_lazy('documents-list')


class DocumentDeleteView(UpdateDeleteMessageMixin, DeleteView):
    model = DocumentsModel
    template_name = 'documents/document-delete.html'
    delete_message = "Документа беше успешно изтрит!"
    success_url = reverse_lazy('documents-list')


