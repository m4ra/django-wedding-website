from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Photo(models.Model):
    image = models.ImageField(_('image'),
                              max_length=200, upload_to='images/',
                              blank=False, help_text=_('required'))

class Gallery(models.Model):
    class Meta:
        verbose_name_plural = 'Galleries'
    title = models.CharField('Title', max_length=20)

    def __str__(self):
        return self.title


class Image(models.Model):
    file = models.FileField('File', upload_to='images/')
    gallery = models.ForeignKey('Gallery', related_name='images', blank=True, null=True)

    def __str__(self):
        return self.filename

    @property
    def filename(self):
        return self.file.name.rsplit('/', 1)[-1]
