"""
Models for the CV

Contains three models :
- Feature : One of my experiences or characteristics
- Hashtag : Hashtags are used to categorized Features
- Link : Materialise the relationship between Features and Hashtags and provide
         an explanation for it
"""
from django.db import models
from django.template import Context
from django.template.loader import get_template
from django.contrib import admin

class Feature(models.Model):
    """A feature describe one of my experiences or characteristics.
    A feature provide its representation in HTML.
    """
    id = models.SlugField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField()

    @property
    def representation(self):
        """Return the basic HTML representation of the Feature"""
        ctx = Context({"feature" : self})
        return get_template("textfeature.html").render(ctx)

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
    """A hashtag is linked to several feature.
    A Link materialise this relation while providing an explanation for it.

    A link provide the HTML representation of its explanation.
    The HTML representation of the Feature in relation is also provided by a
    Link
    """

    feature = models.ForeignKey(Feature)
    hashtag = models.ForeignKey(Hashtag)

    explanation = models.TextField()

    @property
    def explanationrepresentation(self):
        """Get the representation of the explanation to the link only"""
        ctx = Context({"representation": self.explanation})
        return get_template("textlink.html").render(ctx)

    @property
    def representation(self):
        """Return the Feature's representation in relation to the Hashtag."""
        ctx = Context(
            {'main_representation' : self.feature.representation,
             'explanation' : self.explanationrepresentation}
        )
        return get_template("representation_feature.html").render(ctx)

    def __str__(self):
        return self.hashtag.__str__()+"=>"+self.feature.__str__()
admin.site.register(Link)
