from django.db import models
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe

from django.urls import reverse
from os import listdir
from os.path import isfile, join, isdir
import markdown
from shop.settings import DATA_DIR, VIDEO_DIR
import os

# Create your models here.
def parse_md(txt):
    try:
        txt = txt.decode('UTF-8')
    except:
        pass
    return mark_safe(markdown.markdown(txt,extensions=['extra', 'smarty'], output_format='html5'))

class Course(models.Model):
    name = models.CharField(max_length=250, verbose_name=_(u'Name'), blank=True, null = True)
    desc = models.TextField(verbose_name=_(u'Description'), blank=True, null = True)
    image = models.ImageField(verbose_name=_(u'Image'), upload_to='course_images', blank=True, null = True)
    meta_keywords = models.TextField(blank=True, null = True)
    meta_title = models.CharField(max_length=255, blank=True, null = True)
    meta_description = models.TextField(blank=True, null = True)
    name_slug = models.CharField(verbose_name='Name slug',max_length=250, blank=True, null = True)
    is_active = models.BooleanField(verbose_name=_('Is published?'), default=False)



    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'slug': self.name_slug })


    @property
    def image_tag(self):
        return mark_safe('<img width="60" src="%s" />' % self.image.url)

class Lesson(models.Model):
    title = models.CharField(max_length=250, blank=True, verbose_name=_(u'Name'))
    number = models.IntegerField(default=0, verbose_name=_(u'Number'))
    is_active = models.BooleanField(verbose_name=_('Is main?'), default=False)
    image = models.ImageField(blank=True, verbose_name=_(u'Image'), upload_to='lessons_images', null=True)
    course = models.ForeignKey(Course, verbose_name=_(u'Course'), on_delete=models.CASCADE)
    name_slug = models.CharField(verbose_name='Name slug', max_length=250, blank=True)

    def get_absolute_url(self):
        return reverse('lesson_detail', kwargs={'slug': self.name_slug })

    