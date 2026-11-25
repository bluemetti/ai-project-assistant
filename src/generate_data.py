import numpy as np
import pandas as pd

rng = np.random.default_rng(42)

SKILLS = [
    "high_voltage_testing",
    "mechanical_simulation",
    "supplier_management",
    "iec_standards",
]

N_PEOPLE = 12
N_PROJECTS = 10
N_PROJECTS = 10
TASKS_PER_PROJECT = 50
N_TASKS = N_PROJECTS * TASKS_PER_PROJECT
PHASES = ["design", "procurement", "testing", "delivery"]

def generate_team():
    people = [f"P{i:02d}" for i in range(1, N_PEOPLE + 1)]
    data = {}
    for skill in SKILLS:
        data[skill] = rng.integers(1,6, size=N_PEOPLE)
    df = pd.DataFrame(data)
    df.insert(0, "person", people)
    return df

def generate_tasks(team):
    project_names = [f"PRJ{i:02d}" for i in range(1, N_PROJECTS + 1)]
    projects = np.repeat(project_names, TASKS_PER_PROJECT)
    tasks = [f"T{i:04d}" for i in range(1, N_TASKS + 1)]
    phases = rng.choice(PHASES, size=N_TASKS)
    owners = rng.choice(team["person"].to_numpy(), size=N_TASKS)

    base_date = pd.Timestamp("2026-01-05")
    start_offsets = rng.integers(0, 240, size=N_TASKS)
    durations = rng.integers(5, 41, size=N_TASKS)

    planned_start = base_date + pd.to_timedelta(start_offsets, unit="D")
    planned_end = planned_start + pd.to_timedelta(durations, unit="D")

    df = pd.DataFrame({
        "project": projects,
        "task": tasks,
        "phase": phases,
        "owner": owners,
        "planned_start": planned_start,
        "planned_end": planned_end,
        "planned_duration": durations,
    })
    return df
    

if __name__ == "__main__":
    team = generate_team()
    team.to_csv("data/team.csv", index=False)
    tasks = generate_tasks(team)
    tasks.to_csv("data/tasks.csv", index=False)
    print((tasks["planned_end"] > tasks["planned_start"]).all())
    print(tasks.head(10))