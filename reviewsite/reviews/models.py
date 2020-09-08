from django.db import models
from django.conf import settings
from django.urls import reverse
from model_utils.models import TimeStampedModel
from vote.models import VoteModel
from autoslug import AutoSlugField

from .utils import hot


# Create your models here.
class Category(models.Model):
    name = models.CharField("Category name", max_length=255)
    slug = AutoSlugField(
        "Category Address", unique=True, always_update=False, populate_from="name"
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Return absolute URL to a filtered Review List page"""
        return reverse("reviews:list") + "?category=" + str(self.id)


class Review(VoteModel, TimeStampedModel):
    class Meta:
        ordering = ["-hotscore"]

    title = models.CharField("Review title", max_length=255)
    description = models.TextField("Review", blank=True)
    slug = AutoSlugField(
        "Review Address", unique=True, always_update=False, populate_from="title"
    )
    hotscore = models.FloatField("hot rating", default=0)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE,
    )

    category = models.ForeignKey(Category, related_name='reviews', null=True, on_delete=models.PROTECT,)

    def get_hotscore(self):
        return hot(self.num_vote_up, self.num_vote_down, self.created)

    def save(self, *args, **kwargs):
        self.hotscore = self.get_hotscore()
        super(Review, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_author_name(self):
        if self.author.name:
            return self.author.name
        else:
            return self.author.username

    def get_author_url(self):
        """Return complete URL to the Review Detail page"""
        domain = '127.0.0.1:8000'
        return 'http://%s%s' % (domain, self.author.get_absolute_url())

    def get_absolute_url(self):
        """Return absolute URL to the Review Detail page"""
        return reverse("reviews:detail", kwargs={"slug": self.slug})

    def get_complete_url(self):
        """Return complete URL to the Review Detail page"""
        domain = '127.0.0.1:8000'
        return 'http://%s%s' % (domain, self.get_absolute_url())
