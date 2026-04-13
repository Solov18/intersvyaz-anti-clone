from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import AccessKey, KeyEvent

router = APIRouter(prefix="/events")

@router.post("")
def ingest_event(uid: str, panel_id: str, old_counter: int, new_counter: int, raw: str, db: Session = Depends(get_db)):

    event = KeyEvent(
        uid=uid,
        panel_id=panel_id,
        old_counter=old_counter,
        new_counter=new_counter,
        raw_message=raw
    )
    db.add(event)

    key = db.query(AccessKey).filter_by(uid=uid, panel_id=panel_id).first()

    if not key:
        key = AccessKey(uid=uid, panel_id=panel_id, last_counter=new_counter)
        db.add(key)
    else:
        if key.last_counter is not None and old_counter < key.last_counter:
            key.suspicion_count += 1
            key.status = "SUSPECT"
        key.last_counter = new_counter

    db.commit()
    return {"status": "processed"}
