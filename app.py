import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾")

# Phase 3: Manage Application Memory
if 'owner' not in st.session_state:
    st.session_state.owner = Owner("User")
if 'scheduler' not in st.session_state:
    st.session_state.scheduler = Scheduler()

st.title("🐾 PawPal+ Smart Scheduler")

# Sidebar for Adding Pets
with st.sidebar:
    st.header("Add a Pet")
    pet_name = st.text_input("Pet Name")
    pet_species = st.selectbox("Species", ["Dog", "Cat", "Bird", "Other"])
    if st.button("Add Pet"):
        if pet_name:
            new_pet = Pet(name=pet_name, species=pet_species)
            st.session_state.owner.add_pet(new_pet)
            st.success(f"Added {pet_name}!")

# Main Area: Adding Tasks
st.header("Schedule a Task")
if not st.session_state.owner.pets:
    st.info("Add a pet in the sidebar to start scheduling.")
else:
    with st.form("task_form"):
        target_pet = st.selectbox("Select Pet", [p.name for p in st.session_state.owner.pets])
        task_desc = st.text_input("What needs to be done?")
        task_time = st.time_input("At what time?")
        task_freq = st.selectbox("Frequency", ["Once", "Daily"])
        
        if st.form_submit_button("Add to Schedule"):
            time_str = task_time.strftime("%H:%M")
            new_task = Task(description=task_desc, scheduled_time=time_str, pet_name=target_pet, frequency=task_freq)
            for pet in st.session_state.owner.pets:
                if pet.name == target_pet:
                    pet.add_task(new_task)
            st.rerun()

# Phase 4 & 6: Display Sorted Schedule & Conflicts
st.divider()
st.header("Today's Plan")

all_tasks = st.session_state.scheduler.get_all_tasks(st.session_state.owner)
sorted_tasks = st.session_state.scheduler.sort_tasks(all_tasks)

# Show Conflicts
conflicts = st.session_state.scheduler.detect_conflicts(sorted_tasks)
for conflict in conflicts:
    st.warning(conflict)

# Display Tasks
for i, task in enumerate(sorted_tasks):
    cols = st.columns([1, 3, 2, 1])
    cols[0].write(f"**{task.scheduled_time}**")
    cols[1].write(f"{task.pet_name}: {task.description}")
    cols[2].write(f"Freq: {task.frequency}")
    if not task.is_completed:
        if cols[3].button("Done", key=f"btn_{i}"):
            task.mark_complete()
            st.session_state.scheduler.handle_recurrence(task, st.session_state.owner)
            st.rerun()
    else:
        cols[3].write("✅")
