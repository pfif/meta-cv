import 'dart:js' show context, JsObject;
import 'dart:html' show Element, Event, querySelectorAll, Node, document;
import 'package:metacvserver_common/openclose.dart' show StateManager;
import 'dart:async' show Timer;

class Video{
    Element root;
    Element button_open;
    Element button_close;
    Element video_container;
    Element countdown;

    JsObject yt_player;
    String youtube_id;
    int end_introduction;

    StateManager statemanager;

    static List<Video> instances = new List<Video>();
    static int youtubescript_state = 0; //0 = none, 1 = requested, 2 = done

    static void createYoutubeScript(){
        if(Video.youtubescript_state == 0){
            Video.youtubescript_state = 1;
            Element script = new Element.tag("script");
            script.attributes['src'] = "https://www.youtube.com/iframe_api";
            
            Node firstscript = querySelectorAll("script")[0];
            firstscript.parentNode.insertBefore(script, firstscript);

            context['onYouTubeIframeAPIReady'] = (){
                Video.youtubescript_state = 2;

                Video.instances.forEach((Video v){
                    v.initializeYTPlayer();  
                });
            };
        }
    }

    Video(Element root){
        Video.instances.add(this);
        this.root = root;
        this.button_open = this.root.querySelector("input.open_btn");
        this.button_close = this.root.querySelector("input.close_btn");
        this.video_container = this.root.querySelector(".video_contener");
        this.countdown = this.root.querySelector(".countdown");

        this.youtube_id = this.video.dataset['ytid'];
        this.end_introduction = int.parse(this.video.dataset['endintroduction']);

        Video.createYoutubeScript();

        this.statemanager = new StateManager(
            this.button_open,
            this.video_container
        );
        this.statemanager.close();

        this.button_open.onClick.listen((Event e){
            e.preventDefault();
            this.statemanager.open();
            this.play();
        });

        this.button_close.onClick.listen((Event e){
            e.preventDefault();
            this.statemanager.close();
            this.stop();
        });
    }

    Element get video => this.video_container.querySelector(".video");

    void play(){
        if(this.yt_player != null && this.statemanager.isOpened()){
            this.yt_player.callMethod('playVideo');
        }
    }

    void stop(){
        if(this.yt_player != null){
            this.yt_player.callMethod('pauseVideo');
        }
    }

    void initializeYTPlayer(){
        this.yt_player = new JsObject(context['YT']['Player'], [
            this.video,
            new JsObject.jsify({
                'videoId': this.youtube_id,
                'events': {
                    'onReady': (JsObject e){ 
                        this.play(); 
                        this.create_timer_endofintroduction();
                    },
                    'onStateChange': (JsObject e){
                        if(e['data'] == context['YT']['PlayerState']['ENDED']){
                            this.statemanager.close();
                        }
                    }
                }
            })
        ]);

    }

    Timer timer_endofintroduction;
    void create_timer_endofintroduction(){
        this.timer_endofintroduction = new Timer.periodic(
            new Duration(milliseconds:100),
            (Timer t){
                int currentTime = this.yt_player.callMethod('getCurrentTime');
                if(this.statemanager.isOpened() &&
                   currentTime < this.end_introduction &&
                   [1, 3].contains(this.yt_player.callMethod('getPlayerState'))){
                    document.body.classes.add("video_only");
                    this.countdown.text = "Introduction ends in "+
                        (this.end_introduction - currentTime).toInt().toString()
                        +" seconds.";
                } else {
                    document.body.classes.remove("video_only");
                    this.countdown.text = "";
                }
            }
        );
    }
}
