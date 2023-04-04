from pydantic import BaseModel, Field


class BookInputData(BaseModel):
    """"""

    id: str = Field(example="vytxeTZskVKR7C7WgdSP3d")


class BookOutputData(BaseModel):
    """"""

    id: str = Field(example="vytxeTZskVKR7C7WgdSP3d")
    isbn: str = Field(example="978-0321125217")
    title: str = Field(
        example="Domain-Driven Design: Tackling Complexity in the Heart of Softwares"
    )
