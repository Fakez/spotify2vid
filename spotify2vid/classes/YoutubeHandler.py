import requests
import json
from youtubesearchpython import VideosSearch


class YoutubeHandler():

    def search(self, song_info):
        base_url ='https://www.youtube.com/results?search_query='

        #url = base_url + f'{song_title} {artist} {is_live}'
        url = base_url + song_info

        response = requests.get(url).text.split('ytInitialData = ')[1].split(';</script>')[0]
        search_results = json.loads(response)["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"]["sectionListRenderer"]["contents"][0]["itemSectionRenderer"]["contents"]
        first_video_id = search_results[0]["videoRenderer"]['videoId']
        return first_video_id

    def youtubesearchpython(self, song_info):
        videosSearch = VideosSearch(song_info, limit = 1)
        return videosSearch.result()['result'][0]['id']
