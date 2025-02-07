#!/usr/bin/env python

import sys
import re

if len(sys.argv) < 2:
    print("Usage: post_process.py <gcode_file>")
    sys.exit(1)

gcode_file = sys.argv[1]

with open(gcode_file, 'r') as file:
    lines = file.readlines()

modified_lines = []
in_T1_to_T0 = False  # Tracks section between T1 and T0
in_T0_to_T1 = False  # Tracks section between T0 and T1

for line in lines:
    # Detect tool changes
    if "T1" in line:  
        in_T1_to_T0 = True
        in_T0_to_T1 = False
    elif "T0" in line:  
        in_T1_to_T0 = False
        in_T0_to_T1 = True

    # Modify X to A **only** in the T1 to T0 block
    if in_T1_to_T0:
        line = re.sub(r'X', 'A', line)

    # Modify X# values **only in the T0 to T1 block**
    if in_T0_to_T1 and line.startswith("G1"):
        match = re.search(r'X([-+]?\d*\.?\d+)', line)  # Find X followed by a number
        if match:
            x_value = float(match.group(1))  # Extract number
            if 100 <= x_value <= 250:  # Check range
                mirrored_x = 350 - x_value  # Mirror about 175
                line = re.sub(r'X[-+]?\d*\.?\d+', f'X{mirrored_x:.3f}', line)  # Replace with new X

    modified_lines.append(line)

# Save modified G-code (overwrite the original file)
with open(gcode_file, 'w') as file:
    file.writelines(modified_lines)

print(f"Post-processing completed for {gcode_file}")
