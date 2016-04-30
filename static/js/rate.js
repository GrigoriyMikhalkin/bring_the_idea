function negativeScore(){
    score = $(".rate-box");
    if ( score.text() < 0) {
	score.css("background","red");
	score.show();
    }
    else {
	score.css("background","#66CC33");
	score.show();
    }
};

function vote_idea_up(id){
    $.get('/rate/idea/up/'+id, function(content){
        //onSuccess
        var ideaRating = $("#idea-rating");
        ideaRating.text(content.content.result);
	ideaRating.show();
	negativeScore();
    });
};

function vote_idea_down(id){
    $.get('/rate/idea/down/'+id, function(content){
        //onSuccess
        var ideaRating = $("#idea-rating");
        ideaRating.text(content.content.result);
	ideaRating.show();
	negativeScore();
    });
};

negativeScore();
