from django.db import models
from django.shortcuts import reverse


class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    year = models.IntegerField()
    genre = models.TextField()

    def get_detail_url(self):
        return reverse('movies:detail', args=[self.pk])

    def get_delete_url(self):
        return reverse('movies:delete', args=[self.pk])

    def get_update_url(self):
        return reverse('movies:update', args=[self.pk])