from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime


class EventBase(SQLModel):
    type: str
    detail: str


class EventCreate(EventBase):
    pass


class Event(EventBase, table=True):
    id: int = Field(default=None, primary_key=True)
    timestamp: datetime = Field(default_factory=datetime.now)
    player_id: int = Field(foreign_key="player.id")

    player: "Player" = Relationship(back_populates="events")


class PlayerBase(SQLModel):
    name: str


class PlayerCreate(PlayerBase):
    pass


class Player(PlayerBase, table=True):
    id: int = Field(default=None, primary_key=True)

    events: list[Event] = Relationship(back_populates="player")


class PlayerRead(PlayerBase):
    id: int
    events: list[Event] = []
