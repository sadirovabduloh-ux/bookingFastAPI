from .db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Enum, Date, ForeignKey, DateTime
from enum import Enum as PyEnum
from typing import Optional, List
from datetime import date, datetime



class StatusChoices(str, PyEnum):
    gold = "Gold"
    silver = "Silver"
    bronze = "Bronze"
    simple = "Simple"


class RoomTypeChoices(str, PyEnum):
    Luxury = "Luxury"
    JuniorSuite = "Junior Suite"
    Family = "Family"
    Economy = "Economy"
    Single = "Single"


class RoomStatusChoices(str, PyEnum):
    Occupied = "Occupied"
    Reserved = "Reserved"
    Available = "Available"



class UserProfile(Base):
    __tablename__ = 'profile'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    user_name: Mapped[str] = mapped_column(String, unique=True)
    email: Mapped[str] = mapped_column(String, unique=True)
    password: Mapped[str] = mapped_column(String)
    age: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    phone_number: Mapped[Optional[str]] = mapped_column(String, unique=True)
    status: Mapped[StatusChoices] = mapped_column(Enum(StatusChoices), default=StatusChoices.simple)
    data_registered: Mapped[date] = mapped_column(Date, default=date.today())

    profile_review: Mapped[List['Review']] = relationship("Review", back_populates='profile', cascade='all,delete-orphan')
    user_booking: Mapped[List['Booking']] = relationship("Booking", back_populates='user_book', cascade='all,delete-orphan')
    user_token: Mapped[List['RefreshToken']] = relationship("RefreshToken", back_populates='token_user', cascade='all,delete-orphan')


    def __repr__(self):
        return f'{self.first_name},{self.last_name}'

class RefreshToken(Base):
    __tablename__ = 'refresh_token'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('profile.id'))
    token_user: Mapped[UserProfile] = relationship("UserProfile", back_populates='user_token')
    token: Mapped[str] = mapped_column(String)
    created_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)



class Country(Base):
    __tablename__ = 'country'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    country_image: Mapped[str] = mapped_column(String)
    country_name: Mapped[str] = mapped_column(String(50), unique=True)

    country_hotel: Mapped[List['Hotel']] = relationship("Hotel", back_populates='country', cascade='all, delete-orphan')

    def __repr__(self):
        return f'{self.country_name}'

class City(Base):
    __tablename__ = 'city'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    city_image: Mapped[str] = mapped_column(String)
    city_name: Mapped[str] = mapped_column(String(50))

    city: Mapped[List['Hotel']] = relationship("Hotel", back_populates='city', cascade='all,delete-orphan')

    def __repr__(self):
        return f'{self.city_name}'

class Service(Base):
    __tablename__ = 'service'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    service_image: Mapped[str] = mapped_column(String)
    service_name: Mapped[str] = mapped_column(String(50))

    service_hotel: Mapped[List['Hotel']] = relationship("Hotel", back_populates='service', cascade='all,delete-orphan')

    def __repr__(self):
        return f'{self.service_name}'

class Hotel(Base):
    __tablename__ = 'hotel'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    hotel_name: Mapped[str] = mapped_column(String)
    country_id: Mapped[int] = mapped_column(ForeignKey('country.id'))
    city_id: Mapped[int] = mapped_column(ForeignKey('city.id'))
    street: Mapped[str] = mapped_column(String(30))
    postal_code: Mapped[int] = mapped_column(Integer)
    hotel_stars: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String)
    service_id: Mapped[int] = mapped_column(ForeignKey('service.id'))

    country: Mapped[Country] = relationship("Country", back_populates='country_hotel')
    city: Mapped[City] = relationship("City", back_populates='city')
    service: Mapped[Service] = relationship("Service", back_populates='service_hotel')
    hotel_images: Mapped[List['HotelImage']] = relationship("HotelImage", back_populates='hotel', cascade='all,delete-orphan')
    hotel_rooms: Mapped[List['Room']] = relationship("Room", back_populates='hotel_room', cascade='all,delete-orphan')
    hotel_review: Mapped[List['Review']] = relationship("Review", back_populates='hotels', cascade='all,delete-orphan')

    def __repr__(self):
        return f'{self.hotel_name},{self.hotel_stars},{self.hotel_images}'

class HotelImage(Base):
    __tablename__ = 'hotel_image'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    hotel_id: Mapped[int] = mapped_column(ForeignKey('hotel.id'))
    hotel: Mapped[Hotel] = relationship("Hotel", back_populates='hotel_images')


class Room(Base):
    __tablename__ = 'room'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    hotel_id: Mapped[int] = mapped_column(ForeignKey('hotel.id'))
    price: Mapped[int] = mapped_column(Integer)
    room_number: Mapped[int] = mapped_column(Integer)
    room_type: Mapped[RoomTypeChoices] = mapped_column(Enum(RoomTypeChoices))
    room_status: Mapped[RoomStatusChoices] = mapped_column(Enum(RoomStatusChoices))
    text: Mapped[Optional[str]] = mapped_column(String, nullable=True)

    hotel_room: Mapped[Hotel] = relationship("Hotel", back_populates='hotel_rooms')
    rooms: Mapped[List['RoomImage']] = relationship("RoomImage", back_populates='room', cascade='all,delete-orphan')
    room_booking: Mapped[List['Booking']] = relationship("Booking", back_populates='room_book', cascade='all,delete-orphan')


class RoomImage(Base):
    __tablename__ = 'room_image'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    room_id: Mapped[int] = mapped_column(ForeignKey('room.id'))
    room: Mapped[Room] = relationship("Room", back_populates='rooms')



class Review(Base):
    __tablename__ = 'review'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('profile.id'))
    hotel_id: Mapped[int] = mapped_column(ForeignKey('hotel.id'))
    rating: Mapped[int] = mapped_column(Integer)
    comment: Mapped[str] = mapped_column(String)
    created_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    profile: Mapped[UserProfile] = relationship("UserProfile", back_populates='profile_review')
    hotels: Mapped[Hotel] = relationship("Hotel", back_populates='hotel_review')



class Booking(Base):
    __tablename__ = 'booking'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('profile.id'))
    room_id: Mapped[int] = mapped_column(ForeignKey('room.id'))
    check_in: Mapped[datetime] = mapped_column(DateTime)
    check_out: Mapped[datetime] = mapped_column(DateTime)
    created_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    user_book: Mapped[UserProfile] = relationship("UserProfile", back_populates='user_booking')
    room_book: Mapped[Room] = relationship("Room", back_populates='room_booking')
