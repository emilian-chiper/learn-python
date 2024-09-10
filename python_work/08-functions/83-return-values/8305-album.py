def make_album(artist, title, songs=None):
    """Returns a dictionary contianing info about the album"""
    album = {"artist": artist, "title": title}
    if songs:
        album["songs"] = songs
    return album

print(make_album('bolzer', 'the archer'))
print(make_album('michael jackson', 'thriller'))
print(make_album('the ruins of beverast', 'rain upon the impure', 7))