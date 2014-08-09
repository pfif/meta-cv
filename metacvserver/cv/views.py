from django.shortcuts import render
from cv.models import Hashtag
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.utils import simplejson

#The Main Template's utils
def get_maintemplate_context():
  hashtags = Hashtag.objects.all()
  return Context({"hashtags" : hashtags})

def maintemplate_loader(hashtag=None, feature=None):
  c = get_maintemplate_context()
  if hashtag != None:
    c['hashtag'] = hashtag

  if feature != None:
    c['feature'] = feature
  elif hashtag != None:
    c['feature'] = hashtag.features.all()[0]
  t = get_template("themaintemplate.html")
  return t.render(c)

#The views
def mainpage(request):
  return HttpResponse(maintemplate_loader())

def hashtag(request, hashtag_id):
  print(request.META)
  try:
    hashtag = Hashtag.objects.get(id=hashtag_id)
  except Hashtag.DoesNotExist:
    return mainpage(request)
  if request.is_ajax() :
    response = dict()
    response['id'] = hashtag.id
    response['first_feature'] = hashtag.features.all()[0].id
    
    response_json = simplejson.dumps(response)
    return HttpResponse(response_json, content_type='application/json')
  else:
    return HttpResponse(maintemplate_loader(hashtag))

def feature(request, hashtag_id, feature_id):
  try:
    hashtag = Hashtag.objects.get(id=hashtag_id)
  except Hashtag.DoesNotExist:
    return mainpage(request)
  feature = None
  next_feature = None

  #search for the feature
  #and the one after it
  for f in hashtag.features.all():
    if(f.id == feature_id):
      feature = f
    elif(feature != None and next_feature == None):
      next_feature = f
  
  if feature == None:
    return mainpage(request)  

  if request.is_ajax() :
    response = dict()
    response['id'] = feature.id
    response['representation'] = feature.link_set.get(hashtag=hashtag).getrepresentation()
    if next_feature != None :
      response['next_feature_id'] = next_feature.id
    else :
      response['next_feature_id'] = "CLOSE"

    response_json = simplejson.dumps(response)
    return HttpResponse(response_json, content_type='application/json')
  else:
    return HttpResponse(maintemplate_loader(hashtag, feature))
