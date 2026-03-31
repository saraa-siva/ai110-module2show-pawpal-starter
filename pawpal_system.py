from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import List, Optional

@dataclass
class Task:
    description: str
    scheduled_time: str  # Format "HH:MM"
    pet_name: str
    frequency: str = "Once"  # "Once", "Daily"
    is_completed: bool = False

    def mark_complete(self):
        self.is_completed = True

@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        self.tasks.append(task)

class Owner:
    def __init__(self, name: str):
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet):
        self.pets.append(pet)

class Scheduler:
    def get_all_tasks(self, owner: Owner) -> List[Task]:
        all_tasks = []
        for pet in owner.pets:
            all_tasks.extend(pet.tasks)
        return all_tasks

    def sort_tasks(self, tasks: List[Task]) -> List[Task]:
        """Algorithmic sorting by time string 'HH:MM'"""
        return sorted(tasks, key=lambda x: x.scheduled_time)

    def detect_conflicts(self, tasks: List[Task]) -> List[str]:
        """Algorithm to find tasks scheduled at the same time"""
        time_map = {}
        conflicts = []
        for task in tasks:
            if task.scheduled_time in time_map:
                conflicts.append(f"Conflict at {task.scheduled_time}: {task.description} and {time_map[task.scheduled_time]}")
            time_map[task.scheduled_time] = task.description
        return conflicts

    def handle_recurrence(self, task: Task, owner: Owner):
        """If a Daily task is completed, schedule it for tomorrow (simulated)"""
        if task.frequency == "Daily" and task.is_completed:
            new_task = Task(
                description=f"{task.description} (Next)",
                scheduled_time=task.scheduled_time,
                pet_name=task.pet_name,
                frequency="Daily"
            )
            # Find the pet and add the new task
            for pet in owner.pets:
                if pet.name == task.pet_name:
                    pet.add_task(new_task)
