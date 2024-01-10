from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from services import product as ProductService
from dto import product as ProductDTO

router = APIRouter()

@router.post('/', tags=['product'])
async def create(data: ProductDTO.Product = None, db: Session = Depends(get_db)):
    return ProductService.create_product(data, db)


@router.get('/{id}', tags=['product'])
async def get(id: int = None, db: Session = Depends(get_db)):
    return ProductService.get_product(id, db)


@router.put('/{id}', tags=['product'])
async def update(id: int = None, data: ProductDTO.Product = None, db: Session = Depends(get_db)):
    return ProductService.update_product(id, data, db)


@router.delete('/{id}', tags=['product'])
async def remove(id: int = None, db: Session = Depends(get_db)):
    return ProductService.remove_product(id, db)

