from fastapi import FastAPI
import uvicorn
from mysite.api import user,country,city,hotel,review,room,service,booking,hotel_image,room_image,auth
from mysite.admin.setup import setup_admin

shop_app = FastAPI(title="sadirov")

shop_app.include_router(user.user_router)
shop_app.include_router(country.country_router)
shop_app.include_router(city.city_router)
shop_app.include_router(hotel.hotel_router)
shop_app.include_router(review.review_router)
shop_app.include_router(room.room_router)
shop_app.include_router(service.service_router)
shop_app.include_router(booking.booking_router)
shop_app.include_router(hotel_image.hotel_image_router)
shop_app.include_router(room_image.room_image_router)
shop_app.include_router(auth.auth_router)
setup_admin(shop_app)


if __name__ == '__main__':
    uvicorn.run(shop_app,host='127.0.0.1',port=8000)


