from fastapi import APIRouter, HTTPException, status, Depends
from models.events import Event, EventUpdate
from typing import List
from database.connection import get_session
from sqlmodel import Session, select, delete
from auth.authenticate import authenticate

event_router = APIRouter()
events = []

@event_router.put("/event-update/{id}")
async def update_event(
    id: int, event_update: EventUpdate,
    session: Session = Depends(get_session),
    user: str = Depends(authenticate)
) -> dict:
    event = session.get(Event, id)

    if event:
        event_data = event_update.model_dump(exclude_unset=True) # remove undefined attributes
        for key, value in event_data.items():
            setattr(event, key, value)

        session.add(event) # session.add() for insert and update
        session.commit()
        session.refresh(event)

        return {
            "message": "Event updated successfully"
        }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )


@event_router.get("/", response_model=List[Event])
async def retrieve_all_events(session: Session = Depends(get_session), user: str = Depends(authenticate)) -> List[Event]:
    statement = select(Event)
    return session.exec(statement=statement).all()


@event_router.get("/{id}", response_model=Event)
async def get_single_event(id: int, session: Session = Depends(get_session), user: str = Depends(authenticate)) -> Event:
    event = session.get(Event, id)

    if event:
        return event
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )


# Depends() will run first before anything else
@event_router.post("/new")
async def create_event(new_event: Event, session: Session = Depends(get_session), user: str = Depends(authenticate)) -> dict:
    """Exclude 'id' in request body as it is incremented automatically"""
    session.add(new_event)
    session.commit()
    session.refresh(new_event) # session.refresh() repopulates the object
    return {
        "message": "Event created successfully"
    }


@event_router.delete("/{id}")
async def delete_single_event(id: int, session: Session = Depends(get_session), user: str = Depends(authenticate)) -> dict:
    event = session.get(Event, id)

    if event:
        session.delete(event)
        session.commit()
        return {
            "message": "Event removed successfully"
        }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )


@event_router.delete("/")
async def delete_all_events(session: Session = Depends(get_session), user: str = Depends(authenticate)) -> dict:

    statement = delete(Event)
    session.exec(statement=statement)
    session.commit()

    return {"message": "All events successfully deleted"}
