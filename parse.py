# return the index of the last character before the curly braces containing the current z-index start
# e.g. would return 'r' here:
#   selector{
#       ...
#   }
def get_curly_braces_start(stylesheet, z_index_start):
    reverse_index = z_index_start
    while reverse_index > 0 and stylesheet[reverse_index] != '{':
        reverse_index = reverse_index - 1

    # return 1 index before the '{'
    return reverse_index - 1


# removing any leading new lines, as they are not needed
# new lines in rest of the selector are needed, e.g. for multiline selectors
def remove_trailing_newlines(str):
    start_index = 0
    while str[start_index] == "\n":
        start_index = start_index + 1
        
    return str[start_index:]


# add characters to the selector until a previous rule '}' or comment '/' is encountered
def get_selector(stylesheet, z_index_start):
    selector = ""
    reverse_index = get_curly_braces_start(stylesheet, z_index_start)
    while reverse_index > 0 and stylesheet[reverse_index] != '}' and stylesheet[reverse_index] != '/':
        selector = stylesheet[reverse_index] + selector
        reverse_index = reverse_index - 1
    
    return remove_trailing_newlines(selector)


def get_z_index(str):
    return str


import re

# todo: parse through every file in /stylesheets
with open('stylesheets/outsystemsui.css') as file:
    stylesheet = file.read()

pattern = re.compile('(?:{|\s|;|\/)z-index:(.*?)(?:;|\n|\/|\})')

selectors_with_z_index = {}
start_index = 0
while True:
    result = pattern.search(stylesheet, start_index)
    if result is None:
        break

    z_index = get_z_index(result.group(1))
    selector = get_selector(stylesheet, result.span()[0])
    selectors_with_z_index[selector] = z_index

    start_index = result.span()[1]

# sorts alphabetically currently
selectors_with_z_index = dict(sorted(selectors_with_z_index.items(), key=lambda x: x[1]))

for selector, z_index in selectors_with_z_index.items():
    print(f'z-index: {z_index}; \n{selector}\n')
    assert stylesheet.find(selector) != -1

print("\n" + "Total results: " + str(len(selectors_with_z_index)))


