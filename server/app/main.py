from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, Query
from sqlalchemy import select
from sqlalchemy.orm import Session

from . import models, schemas
from .database import Base, engine, get_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="Arena Survival API", lifespan=lifespan)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/scores", response_model=schemas.ScoreOut, status_code=201)
def submit_score(payload: schemas.ScoreCreate, db: Session = Depends(get_db)):
    score = models.Score(**payload.model_dump())
    db.add(score)
    db.commit()
    db.refresh(score)
    return score


@app.get("/leaderboard", response_model=list[schemas.ScoreOut])
def leaderboard(limit: int = Query(10, ge=1, le=100), db: Session = Depends(get_db)):
    query = (
        select(models.Score)
        .order_by(models.Score.score.desc(), models.Score.created_at)
        .limit(limit)
    )
    return db.scalars(query).all()