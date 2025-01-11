list = [1,2,3,4,5]

# def gen(list):
#     for i in list:
#         yield i

# nums = gen(list)

# for num in nums:
#     print(num)

list = iter(list)
for att in dir(list):
    print(att)

try:
    for num in list:
        print(num)
except StopIteration:
    print("End of Iteration")