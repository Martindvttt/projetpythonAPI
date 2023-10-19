from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Artist(Base):
    __tablename__ = 'artists'
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String(100))
    albums = relationship("Album", back_populates="artist")

class Album(Base):
    __tablename__ = 'albums'
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String(160))
    ArtistId = Column(Integer, ForeignKey('artists.ArtistId'))
    artist = relationship("Artist", back_populates="albums")
    tracks = relationship("Track", back_populates="album")

class Track(Base):
    __tablename__ = 'tracks'
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String(200))
    AlbumId = Column(Integer, ForeignKey('albums.AlbumId'))
    album = relationship("Album", back_populates="tracks")
