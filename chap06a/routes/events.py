from fastapi import APIRouter, HTTPException, status
from models.events import Event
from typing import List
from database.connection import get_connection
import json

event_router = APIRouter()
events = []

@event_router.put("/event-update/{id}")
async def update_event(id: int, event: Event) -> dict:
    conn = get_connection()
    cursor = conn.cursor()

    sql = f"SELECT * FROM event WHERE id = {id}"
    row = cursor.execute(sql).fetchone()

    if row:
        sql = f"""
                UPDATE event SET
                    title = '{event.title}',
                    image = '{event.image}',
                    description = '{event.description}',
                    tags = '{json.dump(event.tags)}',
                    location = '{event.location}',
                WHERE id = {id}
              """
        cursor.execute(sql)
        conn.commit()

        cursor.close()
        conn.close()
        return {
            "message": "Event successfully updated"
        }
    else:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    ) 

@event_router.get("/", response_model=List[Event])
async def retrieve_all_events() -> List[Event]:
    conn = get_connection()
    cursor = conn.cursor()

    sql = "SELECT * FROM event"
    rows = cursor.execute(sql).fetchall()

    events = [
        Event(
            id=row[0],
            title=row[1],
            image=row[2],
            description=row[3],
            tags=list(row[4]),
            location=row[5]
        ) for row in rows
    ]
    cursor.close()
    conn.close()

    return events


@event_router.get("/{id}", response_model=Event)
async def get_single_event(id: int) -> Event:
    conn = get_connection()
    cursor = conn.cursor()

    sql = f"""
           SELECT id, title, image, description, tags, location FROM event
           WHERE id == {id}
           """
    print(sql)
    
    cursor.execute(sql)
    row = cursor.fetchone()

    cursor.close()
    conn.close()

    if row:
        return Event(
            id=row[0],
            title=row[1],
            image=row[2],
            description=row[3],
            tags=json.loads(row[4]),
            location=row[5]
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )


@event_router.post("/new")
async def create_event(event: Event) -> dict:
    conn = get_connection()
    cursor = conn.cursor()

    sql = f"""
            INSERT INTO event (title, image, description, tags, location)
            VALUES('{event.title}', '{event.image}', '{event.description}', '{json.dumps(event.tags)}', '{event.location}')
            """
    print(sql)
    cursor.execute(sql)
    conn.commit()

    cursor.close()
    conn.close()
    return {
        "message": "Event created successfully"
    }


@event_router.delete("/{id}")
async def delete_single_event(id: int) -> dict:
    conn = get_connection()
    cursor = conn.cursor()

    sql = f"DELETE FROM event WHERE id = {id}"
    cursor.execute(sql)
    conn.commit()

    count = cursor.rowcount

    cursor.close()
    conn.close()

    if count > 0:
        return {
            "message": "Event removed successfully"
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )


@event_router.delete("/")
async def delete_all_events() -> dict:
    conn = get_connection()
    cursor = conn.cursor()

    sql = f"DELETE FROM event WHERE id > 0"
    cursor.execute(sql)
    conn.commit()

    count = cursor.rowcount
    cursor.close()
    conn.close()

    if count > 0:
        return {"message": f"{count} Event successfully deleted"}
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No event deleted"
        )
