from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import delete
from sqlalchemy.sql.functions import count
from mysite.database.models import Country
from mysite.database.schema import CountryOutSchema,CountryInputSchema
from mysite.database.db import SessionLocal
from sqlalchemy.orm import Session
from typing import List

country_router = APIRouter(prefix='/country',tags=['Country'])

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@country_router.post('/',response_model=CountryOutSchema)
async def create_country(country: CountryInputSchema,db: Session = Depends(get_db)):
    country_db = Country(**country.dict())
    db.add(country_db)
    db.commit()
    db.refresh(country_db)
    return country_db


@country_router.get('/',response_model=List[CountryOutSchema])
async def list_country(db: Session = Depends(get_db)):
     return db.query(Country).all()

@country_router.get('/{country.id}/',response_model=CountryOutSchema)
async def detail_country(country_id: int,db: Session = Depends(get_db)):
    country_db = db.query(Country).filter(Country.id==country_id).first()
    if not country_db:
        raise HTTPException(detail='Туура жассан жонле жаза бербей',status_code=400)

    return country_db

@country_router.put('/{country.id}/',response_model=dict)
async def update_country(country_id: int, country: CountryInputSchema ,
                          db: Session = Depends(get_db)):
    country_db =  db.query(Country).filter(Country.id==country_id).first()
    if not country_db:
        raise HTTPException(detail='Туура жассан жонле жаза бербей', status_code=400)

    for country_key,country_value in country.dict().items():
        setattr(country_db,country_key,country_value)

        db.commit()
        db.refresh(country_db)
        return {'message': 'Кате    гори озгорулду'}


@country_router.delete('/{country.id}/',response_model=dict)
async def delete_country(country_id: int,db: Session = Depends(get_db)):
    country_db = db.query(Country).filter(Country.id==country_id).first()
    if not country_db:
        raise HTTPException(detail='Туура жассан жонле жаза бербей', status_code=400)

    db.delete(country_db)
    db.commit()
    return {'massage': 'категории удален'}


