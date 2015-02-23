var counter = 0;
var spam = [];
var notSpam = [];
$( window ).keydown(function( event) {
	
	key = event.which;

	if(key == 13){
		saveData();
	}

	if(key == 37 || key == 39 || key == 38 || key == 40){

		var tweet_id = items[counter]["tweet_id"];
		if(key == 37){
			//left
			--counter;
			
		}
		else if(key == 39){
			//right
			++counter;
			
		}
		else if(key == 38){
			//up - not spam
			notSpam.push(tweet_id);
			counter++;
		}
		else if(key == 40){
			//down - spam
			spam.push(tweet_id);
			counter++;
		}
		counter = counter < 0 ? 0 : counter >= items.length ? counter = items.length - 1 : counter;
		$("#tweets").html(items[counter]["tweet_id"] + " : "+ items[counter]["text"]);
	}
		
});

$( "#save-tweets" ).click(function() {
  	saveData();
});

function saveData(){

	spamJSON = JSON.stringify(spam.join(','));
	notSpamJSON = JSON.stringify(notSpam.join(','));			

	var data = '[{ "spam" :' + spamJSON + ',' +
				'"notSpam": ' + notSpamJSON +
				'}]';
	
	$.post( "/update",data, function() {
		
	})
	.done(function() {
	    
	})
	.fail(function() {
	    alert( "error" );
	});
}