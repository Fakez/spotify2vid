	
function runYt() {
	
	songs = document.getElementsByClassName('song-row');
	idList = [];
	  var fetches = [];

	for (let song of songs) {
		songName = song.getElementsByClassName('track-name')[0].innerText.split('-')[0];
		artistName = song.getElementsByClassName('artist-name')[0].innerText;
		queryString = songName + ' ' + artistName + ' live';
		fetches.push(
			fetch('/playlists/api/search/' + queryString)
			.then((response) => {
				if (response.ok) {
					return response.json();
				} else {
					throw new Error('Something went wrong');
				}
			})
			.then((json) => {
				insertYoutubeUrlInRow(song, json['video_id']); idList.push(json['video_id'])
			})
		);
	}

	Promise.all(fetches).then(function() {
		console.log ();
		my_elem = document.getElementById('playslist_data_container');
		var span = document.createElement('span');
		span.innerHTML = '<iframe width="720" height="405" src="https://www.youtube.com/embed/VIDEO_ID?playlist=' + idList.join(',') + '"frameborder="0" allowfullscreen>';
		my_elem.parentNode.insertBefore(span, my_elem);
		//y_elem.innerHTML += '<iframe width="720" height="405" src="https://www.youtube.com/embed/VIDEO_ID?playlist=' + idList.join(',') + '"frameborder="0" allowfullscreen>';
	});
}

function insertYoutubeUrlInRow(element, videoId) {
	youtubeBaseUrl = 'https://www.youtube.com/watch?v=';
	element.innerHTML += '<span> | </span>';
	element.innerHTML += '<a href=' + youtubeBaseUrl + videoId + '>' + videoId + '</span>';
}

