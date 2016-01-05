from django.shortcuts import render
from video.models import VideoIntroduction

# Create your views here.

class TheMainTemplateHTMLGenerator():
    def __init__(self, kwargs):
        self.kwargs = kwargs

    def generate_html(self):
        return VideoIntroduction.objects.get(current=True).representation
