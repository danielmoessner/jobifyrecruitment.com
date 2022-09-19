from django.db import models


class Review(models.Model):
    customer = models.CharField(max_length=1000)
    text = models.TextField()
    ordering = models.IntegerField(default=0)
    show = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        ordering = ['ordering']
