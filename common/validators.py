from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class MaxFileSizeValidator:
    def __init__(self, max_size_mb):
        self.max_size_mb = max_size_mb
        self.max_size = max_size_mb * 1024 * 1024  # Convert to bytes

    def __call__(self, file):
        if file.size > self.max_size:
            raise ValidationError(
                f"File size must be under {self.max_size_mb}MB."
            )
