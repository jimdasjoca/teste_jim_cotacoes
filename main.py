from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import requests
import datetime
from database import SessionLocal, Cotacao

app = FastAPI()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/buscar_cotacoes/")
def buscar_cotacoes(db: Session = Depends(get_db)):
    url = "https://api.vatcomply.com/rates?base=USD"
    response = requests.get(url)
    dados = response.json()

    moedas = ["BRL", "EUR", "JPY"]

    for moeda in moedas:
        cotacao = Cotacao(
            id=f"{moeda}-{datetime.date.today()}",
            moeda=moeda,
            valor=dados["rates"].get(moeda, 0),
            data=datetime.date.today()
        )
        db.add(cotacao)

    db.commit()
    return {"message": "Cotações salvas com sucesso!"}




@app.get("/cotacoes/")
def listar_cotacoes(db: Session = Depends(get_db)):
    return db.query(Cotacao).all()
