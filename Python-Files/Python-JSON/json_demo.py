""" JavaScript Object Notation """

import json
from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / "states.json"


with open(file_location) as f:
    data = json.load(f)
    # print(data)

for state in data["states"]:
    # print(state["name"], state["abbreviation"])
    print(state)
    del state["area_codes"]

# add a new state
data["states"].append(
    {
        "name": "Puerto Rico",
        "abbreviation": "PR",
        # "area_codes": ["787", "939"],
    }
)

# add id to each state
for i, state in enumerate(data["states"]):
    state["id"] = i + 1

new_file_location = script_location / "new_states.json"
with open(new_file_location, "w") as f:
    json.dump(data, f, indent=2)
