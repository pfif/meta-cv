import 'dart:html';

//Take care of switching between the states
class StateManager{
  Element div_state_close;
  Element div_state_open;
  
  StateManager(Element div_state_close, Element div_state_open){
    this.div_state_close = div_state_close;
    this.div_state_open = div_state_open;
  }

  //Show element if it is equal to e
  void _showelementif(Element e, Element element){
    if(e == element){
      element.classes.remove("hidden");
    } else {
      element.classes.add("hidden");
    }
  }

  void close(){
    _showelementif(div_state_close, div_state_close);
    _showelementif(div_state_close, div_state_open);
  }

  void open(){
    _showelementif(div_state_open, div_state_close);
    _showelementif(div_state_open, div_state_open);
  }

  bool isOpened(){
      return !this.div_state_open.classes.contains("hidden");
  }
}

