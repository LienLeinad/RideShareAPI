from django.db import models


class BaseModelMixin(models.Model):
    """
    Inherit this Mixin with all models since this has all common attributes
    """

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
