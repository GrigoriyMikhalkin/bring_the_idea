function negativeIdeaScore(){
    score = $("#idea-rating");
    if ( score.text() < 0) {
	score.css("color","red");
	score.show();
    }
    else {
	score.css("color","#66CC33");
	score.show();
    }
};

function negativeCommentScore(id){
    score = $("#comment-"+id+"-rating");
    if ( score.text() < 0) {
	score.css("color","red");
	score.show();
    }
    else {
	score.css("color","#66CC33");
	score.show();
    }
};

function vote_idea_up(id){
    $.get('/rate/idea/up/'+id, function(content){
        //onSuccess
        var ideaRating = $("#idea-rating");
        ideaRating.text(content.content.result);
	ideaRating.show();
	negativeIdeaScore();
    });
};

function vote_idea_down(id){
    $.get('/rate/idea/down/'+id, function(content){
        //onSuccess
        var ideaRating = $("#idea-rating");
        ideaRating.text(content.content.result);
	ideaRating.show();
	negativeIdeaScore();
    });
};

function vote_comment_up(id){
    $.get('/rate/comment/up/'+id, function(content){
	var commentRating = $("#comment-"+id+"-rating");
        commentRating.text(content.content.result);
	commentRating.show();
	negativeCommentScore(id);
    });
};

function vote_comment_down(id){
    $.get('/rate/comment/down/'+id, function(content){
	var commentRating = $("#comment-"+id+"-rating");
        commentRating.text(content.content.result);
	commentRating.show();
	negativeCommentScore(id);
    });
};

negativeIdeaScore();
$(".comment-rating").each( function() {
    var score = $(this);
    if ( score.text() < 0) {
	score.css("color","red");
	score.show();
    }
});
