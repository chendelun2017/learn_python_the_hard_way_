# i = 0
# numbers = []

# while i < 6:
#     print("At the top i is %d" % i)
#     numbers.append(i)
#
#     i = i + 1
#     print("Numbers now:", numbers)
#     print("At the bottom i is %d" % i)
#
# print("The numbers: ")
# for num in numbers:
#     print(num)
#

# def make_list(ran, step):
#     i = 0
#     numbers = []
#     ran1 = range(0, ran)
#     for i in ran1:
#         print("At the top i is %d" % i)
#         numbers.append(i)
#
#         print("Numbers now:", numbers)
#         print("At the bottom i is %d" % i)
#     return numbers
#
# numbers = make_list(6, 1)
# print("The numbers:")
#
# for num in numbers:
#     print(num)


i = 0
numbers = []

for i in range(0,6):
    print("At the top i is %d" % i)
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print("At the bottom i is %d" % i)

print("The numbers: ")

for num in numbers:
    print(num)