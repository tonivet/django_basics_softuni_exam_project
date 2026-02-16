from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import ListView

from .models import DocumentsModel

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
