from typing import Annotated, Optional
from pydantic import BaseModel, EmailStr, Field, StringConstraints, ConfigDict

class AuthorCreate (BaseModel)
    id: int
    name: NameStr
    email: EmailStr
    year_started: Yearint

class AuthorRead (BaseModel)
model_config = ConfigDict(from_attributes = True)
    id: int
    name: NameStr
    email: EmailStr
    year_started: Yearint

class BookCreate (BaseModel)
    id: int
    title: TitleStr
    pages: PagesInt
    author_id: Author_idInt

class BookRead (BaseModel)
model_config = ConfigDict(from_attributes = True)
    id: int
    title: TitleStr
    pages: PagesInt
    author_id: Author_idInt
    

