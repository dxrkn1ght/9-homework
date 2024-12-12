from django.db import models
from django.shortcuts import reverse


class Music(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    date = models.DateField()
    genre = models.TextField()

    def get_detail_url(self):
        return reverse('musics:detail', args=[self.pk])

    def get_delete_url(self):
        return reverse('musics:delete', args=[self.pk])

    def get_update_url(self):
        return reverse('musics:update', args=[self.pk])