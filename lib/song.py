class Song:
    # --- Class Attributes ---
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}  # Fixed to match the test requirement (singular)

    def __init__(self, name, artist, genre):
        # --- Instance Attributes ---
        self.name = name
        self.artist = artist
        self.genre = genre

        # Trigger analytical updates automatically upon creation
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)  # Fixed method name

    # --- Class Methods ---
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        """Increments artist key by 1 in the artist_count dictionary."""
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
