from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel

from autoslug import AutoSlugField

# Create your models here.
class Category(models.Model):
    name = models.CharField("Category name", max_length=255)
    slug = AutoSlugField("Category Address",
                         unique=True,
                         always_update=False,
                         populate_from="name")

    def __str__(self):
        return self.name
                         

class Review(TimeStampedModel):
    title = models.CharField("Review title", max_length=255)
    description = models.TextField("Review", blank=True)
    slug = AutoSlugField("Review Address",
                         unique=True,
                         always_update=False,
                         populate_from="title")
                         
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.CASCADE,
        # limit_choices_to={'is_author': True},
    )

    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.PROTECT,

    )

    def __str__(self):
        return self.title

