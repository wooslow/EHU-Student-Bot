from pydantic import Field

from .service import DataBaseAdapter
from ..parser import Course
from ..enums import Language


class TelegramUser(DataBaseAdapter):
    id: int = Field(..., alias="_id")
    language: Language = Field(default=Language.NULL)
    group: str | None = Field(default=None)
    courses: list[Course] = Field(default_factory=list)
