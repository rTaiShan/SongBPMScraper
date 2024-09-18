class SongInfo:
    def __init__(self, title: str, artist: str, bpm: int, duration: int | str, key: str) -> None:
        self.title = title
        self.artist = artist
        self.bpm = int(bpm)
        self.key = key
        self.duration = self._parse_duration(duration) if isinstance(duration, str) else duration

    def __str__(self) -> str:
        return f'{self.artist} - {self.title} {self._format_duration(self.duration)} {self.bpm} BPM in {self.key}'
    
    def __repr__(self) -> str:
        return self.__str__()
    
    @staticmethod
    def _parse_duration(duration: str) -> int:
        '''
        Given m:ss string, return time in seconds
        '''
        multiplier = 1
        total_time = 0

        for t in duration.split(':')[::-1]:
            total_time += int(t) * multiplier
            multiplier *= 60

        return total_time
    
    @staticmethod
    def _format_duration(duration: int) -> str:
        '''
        Given time in seconds, return m:ss string
        '''
        return f'{duration // 60}:{duration % 60:02}'
