with open("input.txt") as file:
    data = file.read().split("\n\n")


def char_counter(line):
    return len(set(list(line)))


sum_of_counts = 0


for d in data:
    sum_of_counts += char_counter(d.replace("\n", ""))

print(sum_of_counts)
