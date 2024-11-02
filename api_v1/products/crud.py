from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Product
from sqlalchemy.engine import Result

from .schemas import ProductCreate



# возращаем все ПРОДУКТЫ
async def get_products(session: AsyncSession) ->list[Product]:
    stmt = select(Product).order_by(Product.id)
    result: Result = await session.execute(stmt)
    products = result.scalars().all()
    return list(products)


# Возращаем по айдишнику продукты
async def get_product(session: AsyncSession, product_id: int) -> Product | None:
    return await session.get(Product, product_id)



async def create_product(session: AsyncSession, product_in: ProductCreate) -> Product | None
    Product(product_in.model_dump())