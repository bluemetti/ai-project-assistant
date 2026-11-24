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

def generate_team():
    people = [f"P{i:02d}" for i in range(1, N_PEOPLE + 1)]
    data = {}
    for skill in SKILLS:
        data[skill] = rng.integers(1,6, size=N_PEOPLE)
    df = pd.DataFrame(data)
    df.insert(0, "person", people)
    return df

if __name__ == "__main__":
    team = generate_team()
    team.to_csv("data/team.csv", index=False)
    print(team)