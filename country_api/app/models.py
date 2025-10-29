from app.database import Base

class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), unique=True, index=True)
    capital = Column(String(200))
    region = Column(String(100))
    population = Column(BigInteger)
    flag = Column(String(500))
    currency_code = Column(String(10))
