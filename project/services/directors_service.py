from typing import Optional

from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.models import Director


class DirectorsService:
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Director:
        if direcror := self.dao.get_by_id(pk):
            return direcror
        raise ItemNotFound(f'Genre with pk={pk} not exists.')

    def get_all(self, page: Optional[int] = None) -> list[Director]:
        return self.dao.get_all(page=page)

    # def create(self, direcror_d):
    #     return self.dao.create(direcror_d)
    #
    # def update(self, direcror_d):
    #     self.dao.update(direcror_d)
    #     return self.dao
    #
    # def delete(self, rid):
    #     self.dao.delete(rid)