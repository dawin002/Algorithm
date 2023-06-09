
count = 0

def hi():
    global count
    count += 1
    if count == 100:
        return
    print(count)
    hi()


hi()