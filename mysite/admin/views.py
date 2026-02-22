from sqladmin import ModelView
from mysite.database.models import (
    UserProfile, RefreshToken, Country, City, Service,
    Hotel, HotelImage, Room, RoomImage, Review, Booking
)

class UserProfileAdmin(ModelView, model=UserProfile):
    column_list = ['user_name', 'last_name']


class RefreshTokenAdmin(ModelView, model=RefreshToken):
    column_list = ['id', 'user_id', 'token']


class CountryAdmin(ModelView, model=Country):
    column_list = ['country_name']


class CityAdmin(ModelView, model=City):
    column_list = ['city_name']


class ServiceAdmin(ModelView, model=Service):
    column_list = ['service_name']


class HotelAdmin(ModelView, model=Hotel):
    column_list = ['hotel_name', 'street']


class HotelImageAdmin(ModelView, model=HotelImage):
    column_list = ['id', 'hotel_id']


class RoomAdmin(ModelView, model=Room):
    column_list = ['room_number', 'room_type', 'room_status']


class RoomImageAdmin(ModelView, model=RoomImage):
    column_list = ['id', 'room_id']


class ReviewAdmin(ModelView, model=Review):
    column_list = ['id', 'user_id', 'hotel_id', 'rating']


class BookingAdmin(ModelView, model=Booking):
    column_list = ['id', 'user_id', 'room_id', 'check_in', 'check_out']
