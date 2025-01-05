def count(num):
    count = 0
    while count <= num:
        yield count
        count += 1

for n in count(5):
    print(n)


list = [1, 2, 3]
string = "HELLO"

for num in list:
    print(num)

for letter in string:
    print(letter)

iter_list = iter(list)
iter_string = string.__iter__()

# print(dir(iter_list))
for att in dir(iter_list):
    print(att)
# print(dir(iter_string))

if "__next__" in dir(iter_list):
    print(True)
else:
    print(False)

print(next(iter_list))
print(next(iter_list))
print(next(iter_string))
print(next(iter_string))
print(next(iter_string))
print(next(iter_string))
print(next(iter_string))