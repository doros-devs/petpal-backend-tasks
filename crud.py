# crud.py
from sqlalchemy.orm import Session
import models
import schemas


def get_tasks(db: Session):
    return db.query(models.Task).all()

def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(description=task.description, date=task.date)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_vet_visits(db: Session):
    return db.query(models.VetVisit).all()

def create_vet_visit(db: Session, vet_visit: schemas.VetVisitCreate):
    db_vet_visit = models.VetVisit(date=vet_visit.date, notes=vet_visit.notes)
    db.add(db_vet_visit)
    db.commit()
    db.refresh(db_vet_visit)
    return db_vet_visit

def update_task_completion(db: Session, task_id: int, completed: bool):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task:
        db_task.completed = completed
        db.commit()
        db.refresh(db_task)
        return db_task
    else:
        return None

# crud.py
def create_task_completion(db: Session, task_completion: schemas.TaskCompletionCreate):
    db_task_completion = models.TaskCompletion(
        task_id=task_completion.task_id,
        date=task_completion.date
    )
    db.add(db_task_completion)
    db.commit()
    db.refresh(db_task_completion)
    return db_task_completion

def get_task_by_id(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def get_task_completions(db: Session, task_id: int):
    return db.query(models.TaskCompletion).filter(models.TaskCompletion.task_id == task_id).all()