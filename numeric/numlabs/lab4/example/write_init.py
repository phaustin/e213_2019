"""
   write the initial condition file for the simple oscillator
   example
"""

import json

initialVals = {
    "yinitial": [0.0, 1.0],
    "t_beg": 0.0,
    "t_end": 40.0,
    "dt": 0.1,
    "c1": 0.0,
    "c2": 1.0,
}
initialVals["comment"] = "written Sep. 29, 2015"
initialVals["plot_title"] = "simple damped oscillator run 1"

with open("run_1.json", "w") as f:
    f.write(json.dumps(initialVals, indent=4))
