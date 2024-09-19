from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    date = Column(DateTime, nullable=True)
    completed = Column(Boolean, default=False)
    is_daily = Column(Boolean, default=False)

class TaskCompletion(Base):
    __tablename__ = 'task_completions'

    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey('tasks.id'))
    date = Column(DateTime)
    task = relationship("Task", back_populates="completions")

Task.completions = relationship("TaskCompletion", back_populates="task")

class VetVisit(Base):
    __tablename__ = 'vet_visits'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime)
    notes = Column(String)