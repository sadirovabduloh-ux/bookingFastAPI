from typing import Optional
from pydantic import BaseModel,EmailStr
from datetime import date,datetime
from mysite.database.models import StatusChoices,RoomTypeChoices,RoomStatusChoices


class UserprofileInputSchema(BaseModel):
    first_name: str
    last_name: str
    user_name: str
    email:EmailStr
    password: str
    age: Optional[int]
    phone_number:Optional[str]

class UserProfileOutSchema(BaseModel):
    id:int
    first_name: str
    last_name: str
    user_name: str
    email: EmailStr
    age: Optional[int]
    phone_number: Optional[str]
    status: StatusChoices
    data_registered: date

class CountryInputSchema(BaseModel):
    country_image:str
    country_name: str

class CountryOutSchema(BaseModel):
    id: int
    country_image:str
    country_name: str

class CityInputSchema(BaseModel):
    city_image: str
    city_name:str

class CityOutSchema(BaseModel):
    id: int
    city_image: str
    city_name:str


class ServiceInputSchema(BaseModel):
    service_image: str
    service_name: str

class ServiceOutSchema(BaseModel):
    id: int
    service_image: str
    service_name: str

class HotelInputSchema(BaseModel):
    id:int
    hotel_name:str
    country_id:int
    city_id:int
    street:str
    postal_code:int
    hotel_stars:str
    description:str
    service_id:int

class HotelOutSchema(BaseModel):
    id:int
    hotel_name:str
    country_id:int
    city_id:int
    street:str
    postal_code:int
    hotel_stars:str
    description:str
    service_id:int

class HotelImageInputSchema(BaseModel):
    id:int
    hotel_id:int


class HotelImageOutSchema(BaseModel):
    id:int
    hotel_id:int

class RoomInputSchema(BaseModel):
    hotel_id: int
    price:int
    room_number:int
    room_type:RoomTypeChoices
    room_status:RoomStatusChoices

class RoomOutSchema(BaseModel):
    id:int
    hotel_id: int
    price:int
    room_number:int
    room_type:RoomTypeChoices
    room_status:RoomStatusChoices
    text:str



class RoomImageInputSchema(BaseModel):
    id: int
    room_id:int

class RoomImageOutSchema(BaseModel):
    id: int
    room_id:int


class ReviewInputSchema(BaseModel):
    id:int
    user_id:int
    hotel_id:int
    rating:int
    comment:str
    created_date:datetime


class ReviewOutSchema(BaseModel):
    id: int
    user_id: int
    hotel_id: int
    rating: int
    comment: str
    created_date: datetime


class BookingInputSchema(BaseModel):
    user_id:int
    created_date:datetime

class BookingOutSchema(BaseModel):
    id:int
    user_id:int
    check_in:datetime
    check_out:datetime
    created_date:datetime

class UserLoginShema(BaseModel):
    user_name:str
    password: str
