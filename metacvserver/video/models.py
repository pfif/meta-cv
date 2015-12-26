'''
This will store information about introduction videos, given to Dart who does
all the heavy lifiting.
'''
from django.db import models
from django.template.loader import get_template
from django.template import Context
from django.contrib import admin

# Create your models here.

class VideoIntroduction(models.Model):
    '''
    Stores some informations about a introduction video.
    The 'current' one is the one shown on The Main Template.
    '''
    nickname = models.CharField(max_length=50)
    youtube_id = models.CharField(max_length=11, unique=True)
    end_introduction = models.DurationField()
    current = models.BooleanField()

    def save(self, *args, **kwargs):
        '''
        Make sure that there is only one current video.
        '''
        if self.current:
            VideoIntroduction.objects.all().update(current=False)
        super(VideoIntroduction, self).save(*args, **kwargs)

    @property
    def representation(self):
        '''Return a HTML presentation of the video that can be inserted
          on any page that has video.dart'''
        ctx = Context({'video': self})
        return get_template("video_introduction.html").render(ctx)

    def __str__(self):
        return "{nickname} ({youtube_id})".format(nickname=self.nickname,
                                                  youtube_id=self.youtube_id)
admin.site.register(VideoIntroduction)
