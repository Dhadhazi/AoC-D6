with open("input.txt") as file:
    data = file.read().split("\n\n")


def char_counter(line):
    return len(set(list(line)))


sum_of_counts = 0


for d in data:
    sum_of_counts += char_counter(d.replace("\n", ""))

print(f"Sum of all Part one counts: {sum_of_counts}")


def all_char_counter(line):
    chars = {}
    separate_lines = line.split("\n")
    if len(separate_lines) == 2:
        if separate_lines[1] == "":
            separate_lines.pop()

    for i in range(len(separate_lines)):
        for char in separate_lines[i]:
            if char in chars:
                chars[char] += 1
            elif i > 0:
                pass
            else:
                chars[char] = 1

    char_everywhere = 0
    for key in chars:
        if chars[key] == len(separate_lines):
            char_everywhere += 1

    return char_everywhere


counter = 0


for d in data:
    counter += all_char_counter(d)

print(f"Sum of all Part two counts: {counter}")