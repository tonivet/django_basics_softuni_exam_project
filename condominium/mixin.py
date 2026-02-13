from django.contrib import messages

class UpdateMessageMixin:
    update_message = None

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.update_message:
            # obj is a class
            messages.warning(self.request, self.update_message.format(obj=self.object))
        return response


class DeleteMessageMixin:
    delete_message = None

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.delete_message:
            messages.error(self.request, self.delete_message.format(obj=self.object))
        return response


class DisableFormFieldsMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name in self.fields:
            self.fields[name].disabled = True

