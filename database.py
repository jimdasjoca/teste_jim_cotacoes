from sqlalchemy import create_engine, Column, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

DATABASE_URL = "sqlite:///./cotacoes.db"  
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()



# tabela
class Cotacao(Base):
    __tablename__ = "cotacoes"
    id = Column(String, primary_key=True, index=True)
    moeda = Column(String, index=True)
    valor = Column(Float) #valor
    data = Column(DateTime, default=datetime.utcnow)





Base.metadata.create_all(bind=engine)
