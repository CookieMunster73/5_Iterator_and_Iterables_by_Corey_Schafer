# Iterables are objects that can be iterated
# Iterators can hold the state during iterations
# Generators return values that have to be worked with before iterating

nums = [1, 2, 3, 4, 5]
letters = "ABCDEFG"
dir_list = dir(nums)

# for num in nums:
#     print(num)

# for letter in letters:
#     print(letter)

# for att in dir_list:
#     print(att)



# i_nums = nums.__iter__()
i_nums = iter(nums)

# print(dir(i_nums))
# print(i_nums)

# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))

# while True:
#     try:
#         item = next(i_nums)
#         print(item)
#     except StopIteration:
#         break

#---------------------------------------------------------#

class MyRange:

    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current
    
def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1

# def my_range_inf(start):
#     current = start
#     while True:
#         yield current
#         current += 1

nums = my_range(1, 10)
# nums = my_range_inf(1)

print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))

for num in nums:
    print(num)
