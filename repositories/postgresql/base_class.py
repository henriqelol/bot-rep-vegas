from sqlalchemy import Table
from sqlalchemy.ext.declarative import (
    DeclarativeMeta,
    as_declarative,
)


@as_declarative()
class Base:
    __name__: str
    __table__: Table
    metadata: DeclarativeMeta

    def __init__(self, **kw):
        """
        This init is here to teach mypy that the base class accepts arbitrary
        keyword arguments, according to the specified columns of the model
        class.
        """
        super().__init__(**kw)
