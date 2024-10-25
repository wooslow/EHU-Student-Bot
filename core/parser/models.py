from pydantic import BaseModel, Field


class CourseMember(BaseModel):
    name: str
    image_url: str | None


class Course(BaseModel):
    id: int
    name: str
    complete: str | None = Field(default=None)
    image_url: str | None = Field(default=None)
    members: list[CourseMember] | None = Field(default=None)

