"""
View of the CV module.
All these views are based on the same template : themaintemplate.html and are
only a way to load it differently, namely :
* In its default state, showing all the hashtags
* With a hashtag loaded
* With a feature loaded in a hashtag
"""
import json
from cv.models import Hashtag
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

#The Main Template's utils
def get_maintemplate_context():
    """Used by all the following function to get the context basic context for
       The Main Template"""
    hashtags = Hashtag.objects.all()
    return Context({"hashtags" : hashtags})

def maintemplate_loader(hashtag=None, feature=None):
    """Render The Main Template with the given Hashtag, possibly at a precise 
       Feature open"""
    ctx = get_maintemplate_context()
    if hashtag != None:
        ctx['hashtag'] = hashtag

    if feature != None:
        ctx['feature'] = feature
    elif hashtag != None:
        ctx['feature'] = hashtag.features.all()[0]
    template = get_template("themaintemplate.html")
    return template.render(ctx)

#The views
def mainpage(request):
    """Returns The Main Template in its default state"""
    return HttpResponse(maintemplate_loader())

def hashtag(request, hashtag_id):
    """Returns The Main Template with a hashtag open"""
    try:
        hashtag = Hashtag.objects.get(id=hashtag_id)
    except Hashtag.DoesNotExist:
        return mainpage(request)
    if request.is_ajax():
        response = dict()
        response['id'] = hashtag.id
        response['first_feature'] = hashtag.features.all()[0].id

        response_json = json.dumps(response)
        return HttpResponse(response_json, content_type='application/json')
    else:
        return HttpResponse(maintemplate_loader(hashtag))

def feature(request, hashtag_id, feature_id):
    """Returns The Main Template with the given Hashtag at a precise Feature 
       open"""
    try:
        hashtag = Hashtag.objects.get(id=hashtag_id)
    except Hashtag.DoesNotExist:
        return mainpage(request)
    feature = None
    next_feature = None

    #search for the feature
    #and the one after it
    for feature_itr in hashtag.features.all():
        if feature_itr.id == feature_id:
            feature = feature_itr
        elif feature is not None and next_feature is None:
            next_feature = feature_itr

    if feature is None:
        return mainpage(request)

    if request.is_ajax():
        response = dict()
        response['id'] = feature.id
        response['representation'] = (
            feature.link_set.get(hashtag=hashtag).getrepresentation()
        )
        if next_feature != None:
            response['next_feature_id'] = next_feature.id
        else:
            response['next_feature_id'] = "CLOSE"

        response_json = json.dumps(response)
        return HttpResponse(response_json, content_type='application/json')
    else:
        return HttpResponse(maintemplate_loader(hashtag, feature))
