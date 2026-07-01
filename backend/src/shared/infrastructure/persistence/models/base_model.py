from typing import Annotated

from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, MappedColumn, mapped_column

intpk = Annotated[int, mapped_column(Integer, primary_key=True, autoincrement=True)]

class BaseSQLAlchemyModel(DeclarativeBase):
    id : MappedColumn[intpk]