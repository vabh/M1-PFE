var items = [];
$.getJSON( "tweets.json", function( data ) {
	
	$.each( data, function( key, val ) {
		row = [];
		row["tweet_id"] = val.tweet_id;
		row["text"] = val.text;
		items.push(row);					
		// items[val.tweet_id] = val.text;
	});
	 
	// $( "<ol/>", {
	// 	"id": "tweet-list",
	//     html: items.join( "" )
	// }).appendTo( "#tweets" );
})
.then(function(){
	$("#tweets").html(items[0]["text"]);
});