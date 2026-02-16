from django.db.models import TextChoices


class DocumentTypeChoices(TextChoices):
    PROTOCOL = "Protocol", "Протокол"
    INVOICE = "Invoice", "Фактура"
    MAIL = "Mail", "Писмо"
    OTHER = "Other", "Друго"
