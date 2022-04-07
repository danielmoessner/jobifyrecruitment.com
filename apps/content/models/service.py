from django.db import models


class Service(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    text = models.TextField()
    ordering = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        ordering = ['ordering']
