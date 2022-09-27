import re

# todo: parse through every file in /stylesheets
with open('stylesheets/outsystemsui.css') as f:
    lines = f.readlines()

# dict with {selector : z-index value}
selectors_with_z_index = {}
current_selector = ""
for line in lines:
    if "{" in line:
        line = line.rstrip()
        current_selector = line[0 : len(line) - 2]   # remove '{' from selector
    if "z-index:" in line and not "-servicestudio-z-index:" in line:
        result = re.search('z-index:(.*);', line)   # change to only look for [0-9] +/-
        selectors_with_z_index[current_selector] = int(result.group(1))

for selector, z_index in selectors_with_z_index:
    print(z_index)
    print(selector)