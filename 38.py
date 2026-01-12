def check_for_line():
    word = "1"
    data = True
    line_no = 1
    with open("Practice.txt", "r") as f:
        while data:
            data = f.readline()
            data = data.split(',')
            if word in data:
                freq = data.count("1")
                return freq

            line_no += 1


print(check_for_line())
