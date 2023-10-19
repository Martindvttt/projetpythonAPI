from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from . import models

SQLALCHEMY_DATABASE_URL = "sqlite:///./chinook.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_artist_by_id(db: Session, artist_id: int):
    return db.query(models.Artist).filter(models.Artist.ArtistId == artist_id).first()

def get_all_artists(db: Session):
    return db.query(models.Artist).all()

def search_artist_by_name(db: Session, artist_name: str):
    return db.query(models.Artist).filter(models.Artist.Name.contains(artist_name)).all()

def get_albums_by_artist_id(db: Session, artist_id: int):
    return db.query(models.Album).filter(models.Album.ArtistId == artist_id).all()

def get_tracks_by_album_id(db: Session, album_id: int):
    return db.query(models.Track).filter(models.Track.AlbumId == album_id).all()