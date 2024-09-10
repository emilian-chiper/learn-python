def make_album(artist, title, songs=None):
    """Returns a dictionary contianing info about the album"""
    album = {"artist": artist, "title": title}
    if songs:
        album["songs"] = songs
    return album

while True:
    print("\nTell me about your new favorite album:")
    print("(press 'q' at any time to quit)")

    artist_name = input("Who wrote the album? ")
    if artist_name == 'q':
        break

    album_name = input("And what's it called? ")
    if album_name == 'q':
        break

    num_songs = input("How many songs are there on it? ")
    if num_songs == 'q' or num_songs == '':
        break

    print(make_album(artist_name, album_name, num_songs))