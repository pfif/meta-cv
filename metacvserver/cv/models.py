from django.db import models
from django.template import Context
from django.template.loader import get_template
from django.contrib import admin

class Feature(models.Model):
  """A feature describe one of my experiences or characteristics.
  A feature provide its representation in HTML.
  """
  id = models.SlugField(primary_key=True)
  title = models.CharField(max_length = 50) 
  description = models.TextField()

  def getmainrepresentation(self):
    c = Context({"feature" : self})
    return get_template("textfeature.html").render(c)
  
  def __str__(self):
    return self.id

admin.site.register(Feature)


class Hashtag(models.Model):
  """A hashtag categorize the features

  It is link to them thanks to the link class.
  """
  id = models.SlugField(primary_key=True)
  features = models.ManyToManyField(Feature, through='Link')

  def __str__(self):
    return self.id
admin.site.register(Hashtag)

class Link(models.Model):
  """A hashtag is linked to several feature. A Link is the object materialise this relation. It also contain an explanation to it .
  
  A link provide the HTML representation of its explanation.
  The HTML representation of the Feature in relation is also provided by a Link
  """

  feature = models.ForeignKey(Feature)
  hashtag = models.ForeignKey(Hashtag)

  explanation = models.TextField()

  def getexplanationrepresentation(self):
    c = Context({"representation": self.explanation})
    return get_template("textlink.html").render(c)

  def getrepresentation(self):
    """Return the representation of the Feature in relation to the hashtag."""
    c = Context({'main_representation' : self.feature.getmainrepresentation(), 'explanation' : self.getexplanationrepresentation()})
    return get_template("representation_feature.html").render(c)

  def __str__(self):
    return self.hashtag.__str__()+"=>"+self.feature.__str__()
admin.site.register(Link)
