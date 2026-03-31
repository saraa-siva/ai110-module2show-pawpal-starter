# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?
- My initial UML design centered on a modular approach using four main classes: Owner: The top-level manager responsible for holding a collection of pets. Pet: A data container for specific pet information and their unique task lists. Task: A definition of a single activity, including its description, time, and completion status. Scheduler: The "engine" of the app, responsible for cross-pet logic like sorting and conflict detection.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.
- During implementation, I shifted from having the Pet class manage its own sorting to moving that logic into the Scheduler. I made this change to follow the Single Responsibility Principle; it makes more sense for a dedicated scheduling entity to handle algorithmic processing while the Pet class remains a clean data structure.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?
- The scheduler primarily considers time (HH:MM format) and recurrence (Daily vs. Once). I decided that chronological order was the highest priority because, for a pet owner, knowing what needs to happen next in their day is the most critical information for maintaining a routine.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?
- One major tradeoff is that the conflict detection only flags exact time matches (e.g., two tasks at 08:00). It does not account for the duration of a task. This is reasonable for an MVP because most pet tasks (feeding, medication) are point-in-time events rather than long-duration blocks.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?
- I used AI for design brainstorming (generating the initial Mermaid.js UML), scaffolding the logic in pawpal_system.py using Python Dataclasses, and generating a pytest suite. The most helpful prompts were those where I provided the class skeletons and asked the AI to implement specific algorithms like "lambda-based sorting for time strings."

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?
- I rejected an AI suggestion to use the Pandas library for task management. While efficient for large datasets, it added unnecessary complexity to a simple OOP project. I verified the alternative—standard Python list comprehensions—by running the main.py demo script to ensure the output remained identical.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?
- I tested three core behaviors: Task Completion: Ensuring the status actually flips to True. Sorting: Verifying that a task added for 6:00 PM appears after a task for 8:00 AM. Conflict Detection: Ensuring a warning is generated when two tasks share a time slot. These were important to ensure the "Brain" of the app was reliable before connecting it to the UI.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?
- I am very confident (5/5 stars) in the core logic. If I had more time, I would test edge cases like "midnight rollovers" for daily tasks and handling empty pet profiles to ensure the UI doesn't crash.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
- I am most satisfied with the Scheduler's recurrence logic. Seeing a "Daily" task automatically regenerate for the next day after clicking "Done" makes the app feel genuinely "smart."

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
- I would redesign the Task class to use Python datetime objects instead of strings for time. This would allow for more advanced features like "reminders" or calculating the time remaining until the next task.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
- The most important thing I learned is that being a "Lead Architect" means using AI to generate the bricks, but manually ensuring the blueprint (system state and class relationships) is followed strictly to prevent technical debt.
