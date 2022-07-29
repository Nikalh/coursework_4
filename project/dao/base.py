from typing import Generic, List, Optional, TypeVar

from flask import current_app
from flask_sqlalchemy import BaseQuery
from sqlalchemy.orm import scoped_session
from werkzeug.exceptions import NotFound
from project.setup.db.models import Base

T = TypeVar('T', bound=Base)


class BaseDAO(Generic[T]):
    __model__ = Base

    def __init__(self, db_session: scoped_session) -> None:
        self._db_session = db_session

    @property
    def _items_per_page(self) -> int:
        return current_app.config['ITEMS_PER_PAGE']

    def get_by_id(self, pk: int) -> Optional[T]:
        return self._db_session.query(self.__model__).get(pk)

    def get_all(self, page: Optional[int] = None) -> List[T]:
        stmt: BaseQuery = self._db_session.query(self.__model__)
        if page:
            try:
                return stmt.paginate(page, self._items_per_page).items
            except NotFound:
                return []
        return stmt.all()

    def get_by_email(self, email: str) -> Optional[T]:
        return self._db_session.query(self.__model__).get(email)

    def get_all_order_by(self, page: int, filter: Optional[str]):
        ...
        # filter = request.args.get('status')
        # if filter != None and filter == 'new':
        #     return movie_service.get_all(filter=filter, **page_parser.parse_args())
        # else:
        #     return movie_service.get_all(**page_parser.parse_args())




