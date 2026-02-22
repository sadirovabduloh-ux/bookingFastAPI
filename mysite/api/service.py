from fastapi import APIRouter, HTTPException, Depends
from mysite.database.models import Service
from mysite.database.schema import ServiceOutSchema,ServiceInputSchema
from mysite.database.db import SessionLocal
from sqlalchemy.orm import Session
from typing import List

service_router = APIRouter(prefix='/service',tags=['Service'])

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@service_router.post('/', response_model=ServiceOutSchema)
async def create_service(service: ServiceInputSchema, db: Session = Depends(get_db)):
    service_db = Service(**service.dict())
    db.add(service_db)
    db.commit()
    db.refresh(service_db)
    return service_db


@service_router.get('/', response_model=List[ServiceOutSchema])
async def list_service(db: Session = Depends(get_db)):
    return db.query(Service).all()


@service_router.get('/{service.id}/', response_model=ServiceOutSchema)
async def detail_service(service_id: int, db: Session = Depends(get_db)):
    service_db = db.query(Service).filter(Service.id == service_id).first()
    if not service_db:
        raise HTTPException(detail='Туура жассан жонле жаза бербей', status_code=400)
    return service_db


@service_router.put('/{service.id}/', response_model=dict)
async def update_service(service_id: int, service: ServiceInputSchema,
                         db: Session = Depends(get_db)):
    service_db = db.query(Service).filter(Service.id == service_id).first()
    if not service_db:
        raise HTTPException(detail='Туура жассан жонле жаза бербей', status_code=400)

    for service_key, service_value in service.dict().items():
        setattr(service_db, service_key, service_value)

    db.commit()
    db.refresh(service_db)
    return {'message': 'Категория успешно обновлена'}


@service_router.delete('/{service.id}/', response_model=dict)
async def delete_service(service_id: int, db: Session = Depends(get_db)):
    service_db = db.query(Service).filter(Service.id == service_id).first()
    if not service_db:
        raise HTTPException(detail='Туура жассан жонле жаза бербей', status_code=400)

    db.delete(service_db)
    db.commit()
    return {'message': 'Категория удалена'}
