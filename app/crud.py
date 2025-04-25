from fastapi import HTTPException, status
from sqlmodel import Session, select
from .models import Player, Event
from datetime import datetime


ALLOWED_EVENT_TYPES = {"level_started", "level_solved"}


def get_players(session: Session):
    return session.exec(select(Player)).all()


def create_player(session: Session, name: str):
    if not name:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Name must not be empty",
        )

    new_player = Player(name=name)
    session.add(new_player)
    session.commit()
    session.refresh(new_player)
    return {"id": new_player.id, "name": new_player.name}


def get_player_by_id(session: Session, player_id: int):
    player = session.get(Player, player_id)
    if not player:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Player with id {player_id} not found",
        )
    return player


def get_player_events(session: Session, player_id: int, type: str):
    player = session.get(Player, player_id)
    if not player:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Player with id {player_id} not found",
        )

    events_query = select(Event).where(Event.player_id == player_id)

    if type:
        if type not in ALLOWED_EVENT_TYPES:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid event type: {type}",
            )
        events_query = events_query.where(Event.type == type)

    return session.exec(events_query).all()


def create_event_for_player(session: Session, player_id: int, type: str, detail: str):
    player = session.get(Player, player_id)
    if not player:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Player with id {player_id} not found",
        )

    if type not in ALLOWED_EVENT_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid event type: {type}",
        )

    new_event = Event(type=type, detail=detail, player_id=player_id, timestamp=datetime.now())
    session.add(new_event)
    session.commit()
    session.refresh(new_event)
    return new_event


def get_events(session: Session, type: str):
    query = select(Event)

    if type:
        if type not in ALLOWED_EVENT_TYPES:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid event type: {type}",
            )
        query = query.where(Event.type == type)

    return session.exec(query).all()
