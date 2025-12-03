password = 0
pos = 50
with open("data.in", "r") as infile:
    for line in infile:
        dir = line[0]
        count = int(line[1:])
        if dir == "L":
            pos -= count
        else:
            pos += count
        pos %= 100
        if pos == 0:
            password += 1
    print(password)
