from fastapi import APIRouter, HTTPException, status
from models.events import Event
from typing import List

event_router = APIRouter()
events = []

@event_router.get("/", response_model=List[Event])
async def retrieve_all_events() -> List[Event]:
    return events


@event_router.post("/new")
async def create_event(body: Event) -> dict:
    events.append(body)
    return {
        "message": "Event created successfully"
    }


@event_router.delete("/{id}")
async def delete_single_event(id: int) -> dict:
    for event in events:
        if event.id == id:
            events.remove(event)
            return {
                "message": "Event removed successfully"
            }
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )


@event_router.get("/{id}", response_model=Event)
async def get_single_event(id: int) -> Event:
    for event in events:
        if event.id == id:
            return event
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )


@event_router.delete("/")
async def delete_all_events() -> dict:
    events.clear()
    return {
        "message": "All events removed successfully"
    }
