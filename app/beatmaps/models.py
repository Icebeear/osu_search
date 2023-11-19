from django.db import models

class Beatmap(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    mapper = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    
    genre = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    map_type = models.CharField(max_length=255)
    
    total_length = models.IntegerField()
    play_count = models.IntegerField()
    favourite_count = models.IntegerField()
    
    star_difficulty = models.FloatField()
    bpm = models.FloatField()
    ar = models.FloatField()
    od = models.FloatField()
    hp = models.FloatField()
    cs = models.FloatField()

    submit_date = models.DateField()
    song_id = models.IntegerField()

    def __str__(self):
        return f"{self.title} - {self.star_difficulty}"
