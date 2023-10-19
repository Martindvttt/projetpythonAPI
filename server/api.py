from fastapi import FastAPI, Depends, HTTPException
from . import database, models
from sqlalchemy.orm import Session

app = FastAPI()

@app.get("/artists/{artist_id}")
def read_artist(artist_id: int, db: Session = Depends(database.get_db)):
    db_artist = database.get_artist_by_id(db, artist_id=artist_id)
    if db_artist is None:
        raise HTTPException(status_code=404, detail="Artist not found")
    return db_artist

@app.get("/artists/")
def read_all_artists(db: Session = Depends(database.get_db)):
    artists = database.get_all_artists(db)
    return artists

@app.get("/artists/search/{artist_name}")
def search_artist_by_name(artist_name: str, db: Session = Depends(database.get_db)):
    artists = database.search_artist_by_name(db, artist_name)
    if not artists:
        raise HTTPException(status_code=404, detail="No artists found with the given name")
    return artists

@app.get("/albums/artist/{artist_id}")
def get_albums_by_artist_id(artist_id: int, db: Session = Depends(database.get_db)):
    albums = database.get_albums_by_artist_id(db, artist_id)
    if not albums:
        raise HTTPException(status_code=404, detail="No albums found for the given artist ID")
    return albums

@app.get("/tracks/album/{album_id}")
def get_tracks_by_album_id(album_id: int, db: Session = Depends(database.get_db)):
    tracks = database.get_tracks_by_album_id(db, album_id)
    if not tracks:
        raise HTTPException(status_code=404, detail="No tracks found for the given album ID")
    return tracks