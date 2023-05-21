mark = [45,20,69, 80,55]
name = ["d", "c", "b", "e", "a"]
temp_name = ""
temp_mark = 0
swap = True
n = 3
while swap:
    swap = False
    for index in range(0, n + 1):
        if name[index] > name[index + 1]:
            temp_name = name[index]
            name[index] = name[index + 1]
            name[index + 1] = temp_name
            temp_mark= mark[index]
            mark[index] = mark[index + 1]
            mark[index + 1] = temp_mark
            swap = True
    n -= 1
print (name, " ",mark)