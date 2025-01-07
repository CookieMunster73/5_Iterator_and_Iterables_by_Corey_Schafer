ten = [1,2,3,4,5,6,7,8,9,10]

def topten():
    global ten
    ten = ten.__iter__()
    try:
        while True:
            yield next(ten)
    except StopIteration:
        print("End of list.")

# values = topten()

# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))

for num in topten():
    print(num)

print("Hi there.")
