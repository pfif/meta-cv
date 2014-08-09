import 'dart:js';
import 'themaintemplate.dart';
import 'dart:html';
//A file linked to the HTML to change the state at start up.
void main(){
  //Initialisation of the page
  OpenHashtagManager hashtagmanager = OpenHashtagManager.getInstance();
  
  //Every hashtag links allow to load hashtag.
  for(Element link in querySelectorAll("#state_mainpage a")){
    link.onClick.listen((Event e){
      e.preventDefault();
      hashtagmanager.showHashtag(link.text.substring(1));
    });
  }

  querySelector("#next_hashtag").onClick.listen((Event e){
    e.preventDefault();
    hashtagmanager.nextFeature();
    });

  querySelector("a[href='/']").onClick.listen((Event e){
    e.preventDefault();
    hashtagmanager.closeHashtag();
  });
  
  String hashtag_id = context['HASHTAG_ID'];
  String feature_id = context['FEATURE_ID'];
  if(hashtag_id != null && feature_id != null)
  hashtagmanager.showHashtag_noajax(hashtag_id, feature_id);
}
