from django.db import models


class StaffCategory(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=1000)
    ordering = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Staff Category'
        verbose_name_plural = 'Staff Categories'
        ordering = ['ordering']
