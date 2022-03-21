from solo.models import SingletonModel
from django.db import models
from tinymce import models as tinymce_models


###
# other
###
class Service(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    text = models.TextField()
    ordering = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        ordering = ['ordering']


###
# pages
###
class WhyToWorkWithUsPage(SingletonModel):
    #
    header_title = models.CharField(verbose_name='Header > Title', max_length=100)
    #
    text_title = models.CharField(verbose_name='Text > Title', max_length=200)
    text_sub = models.CharField(verbose_name='Text > Sub', max_length=200)
    text_left = tinymce_models.HTMLField(verbose_name='Text > Left')
    text_right = tinymce_models.HTMLField(verbose_name='Text > Right')
    text_button = models.CharField(verbose_name='Text > Button', max_length=200)

    def __str__(self):
        return self._meta.verbose_name

    class Meta:
        verbose_name = 'Page > Applicant Why To Work With Us'
