from typing import Generic, Optional, TypeVar

from bson import ObjectId
from pydantic.generics import GenericModel


T = TypeVar("T")


# https://jsonapi.org/format/#fetching-pagination
class JsonApiLinks(GenericModel, Generic[T]):
    first: str
    last: str
    next: Optional[str] = None
    prev: Optional[str] = None

    class Config:
        populate_by_name = True


class JsonApiMeta(GenericModel, Generic[T]):
    total: int
    count: int

    class Config:
        allow_population_by_field_name = True


class Pagination(GenericModel, Generic[T]):
    items: list[T]
    links: JsonApiLinks
    meta: JsonApiMeta

    class Config:
        allow_population_by_field_name = True
