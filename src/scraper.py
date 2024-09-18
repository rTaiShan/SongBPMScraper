import requests
from lxml import html

from songinfo import SongInfo

def get_song_info(title: str) -> list[SongInfo]:
    '''
    Search for song info on songbpm.com
    '''
    response = requests.post(
        'https://songbpm.com/searches',
        data=dict(query=title),
    )

    tree = html.fromstring(response.content)
    song_cards = tree.xpath('/html/body/div/main/div/div/div/div/a')
    
    results = []
    for song_card in song_cards:
        divs = song_card.findall('div')
        artist, title = (p.text for p in divs[0].findall('div')[1].findall('p'))
        key, duration, bpm = (e.findall('span')[1].text for e in divs[1].findall('div'))
        results.append(SongInfo(title, artist, bpm, duration, key))

    return results
