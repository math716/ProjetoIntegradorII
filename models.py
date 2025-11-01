from sqlalchemy import Column, Integer, String, Date
from database import Base

class Pessoa(Base):
    __tablename__ = "pessoas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    cpf = Column(String)
    rg = Column(String)
    data_nascimento = Column(String)
    arquivo = Column(String)  # nome do arquivo PDF salvo