import pytest
from pawpal_system import Task, Pet, Owner, Scheduler

def test_task_completion():
    task = Task("Feed", "08:00", "Buddy")
    task.mark_complete()
    assert task.is_completed == True

def test_task_sorting():
    scheduler = Scheduler()
    t1 = Task("Dinner", "18:00", "Buddy")
    t2 = Task("Breakfast", "08:00", "Buddy")
    sorted_tasks = scheduler.sort_tasks([t1, t2])
    assert sorted_tasks[0].scheduled_time == "08:00"

def test_conflict_detection():
    scheduler = Scheduler()
    t1 = Task("Walk", "10:00", "Buddy")
    t2 = Task("Meds", "10:00", "Misty")
    conflicts = scheduler.detect_conflicts([t1, t2])
    assert len(conflicts) == 1
    assert "10:00" in conflicts[0]
