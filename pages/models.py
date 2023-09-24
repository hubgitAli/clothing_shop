from django.db import models
from django.urls import reverse

from ckeditor.fields import RichTextField

from django.utils.translation import gettext_lazy as _
from accounts.models import CustomUser


class Package(models.Model):
    """ PRODUCT MODEL """
    class Meta:
        verbose_name = _("Package")
        verbose_name_plural = _("Packages")

    title = models.CharField(max_length=300, verbose_name=_('title'))
    price = models.PositiveIntegerField(blank=True, verbose_name=_('price'))
    image = models.ImageField(blank=True, upload_to='image', verbose_name=_('image'))
    description = RichTextField(blank=True, verbose_name=_('description'))
    data_created = models.DateTimeField(auto_now_add=True, verbose_name=_('date created'))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('package_detail_view', args=[self.pk])


class Comment(models.Model):
    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    author = models.ForeignKey(CustomUser, related_name='author', on_delete=models.CASCADE, verbose_name=_("author"))
    package_name = models.ForeignKey(Package, related_name='package', on_delete=models.CASCADE,
                                     verbose_name=_('package name'))
    text = models.TextField(verbose_name=_("text"))
    data_created = models.DateTimeField(auto_now_add=True, verbose_name=_("date created"))
    data_modified = models.DateTimeField(auto_now=True, verbose_name=_("date modified"))
    # is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.text
