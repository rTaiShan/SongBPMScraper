from sys import argv
from scraper import get_song_info

def main():    
    title = input('Song title: ') if len(argv) < 2 else " ".join(argv[1:])

    for song in get_song_info(title):
        print(song)

if __name__ == '__main__':
    main()
