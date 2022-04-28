from django.db import models


class MemberCategory(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Member Category'
        verbose_name_plural = 'Member Categories'

    def __str__(self):
        return '{}'.format(self.title)


class Member(models.Model):
    category = models.ForeignKey(MemberCategory, on_delete=models.CASCADE, related_name='members')
    image = models.ImageField(upload_to='content/member/image/')
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'

    def __str__(self):
        return '{}'.format(self.name)
