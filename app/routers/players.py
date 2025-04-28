from fastapi import APIRouter, Depends, status, Query
from sqlmodel import Session
from ..database import get_session
from ..models import Player, Event, PlayerRead, PlayerCreate, EventCreate
from .. import crud

router = APIRouter(
    prefix="/players",
    tags=["players"]
)


@router.get("/", response_model=list[Player], status_code=status.HTTP_200_OK)
def get_players(session: Session = Depends(get_session)):
    return crud.get_players(session)


@router.post("/", response_model=Player, status_code=status.HTTP_201_CREATED)
def create_player(player_in: PlayerCreate, session: Session = Depends(get_session)):
    return crud.create_player(session, player_in.name)


@router.get("/{player_id}", response_model=PlayerRead, status_code=status.HTTP_200_OK)
def get_player(player_id: int, session: Session = Depends(get_session)):
    return crud.get_player_by_id(session, player_id)


@router.get("/{player_id}/events", response_model=list[Event])
def get_player_events(
    player_id: int,
    type: str = Query(default=None),
    session: Session = Depends(get_session)
):
    return crud.get_player_events(session, player_id, type)


@router.post("/{player_id}/events", response_model=Event, status_code=status.HTTP_201_CREATED)
def create_player_event(
    player_id: int,
    event_in: EventCreate,
    session: Session = Depends(get_session)
):
    return crud.create_event_for_player(session, player_id, event_in.type, event_in.detail)
