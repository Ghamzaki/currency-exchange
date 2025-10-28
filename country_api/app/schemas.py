from pydantic import BaseModel, Field
from typing import Optional

class CountryBase(BaseModel):
    name: str = Field(..., example="United States")
    capital: Optional[str] = Field(None, example="Washington D.C.")
    region: Optional[str] = Field(None, example="Americas")
    population: Optional[int] = Field(None, example=331000000)
    flag: Optional[str] = Field(None, example="https://flagcdn.com/us.svg")
    currency_code: Optional[str] = Field(None, example="USD")

class CountryCreate(CountryBase):
    pass

class CountryUpdate(CountryBase):
    pass

class CountryResponse(CountryBase):
    id: int = Field(..., example=1)

    class Config:
        orm_mode = True
