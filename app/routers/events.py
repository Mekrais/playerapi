from fastapi import APIRouter, Depends, Query, status
from sqlmodel import Session
from ..database import get_session
from ..models import Event
from .. import crud


router = APIRouter(prefix="/events", tags=["events"])


@router.get("/", response_model=list[Event], status_code=status.HTTP_200_OK)
def get_events(type: str = Query(default=None), session: Session = Depends(get_session)):
    return crud.get_events(session, type)
