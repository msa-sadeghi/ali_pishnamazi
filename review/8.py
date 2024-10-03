# x = (1,2)
# n = int(input(":> "))
# x += (n,)
# print(x)
# x1 = (1,2)
# x2 = (4,5)
# print(id(x1))
# x1 +=  x2
# print(x1)
# print(x2)

# print(id(x1))


chars = ("a", "b", "a", "a", "c")
# print(chars.index("a", 0, len(chars)))
# j = ()
# for i in range(len(chars)):
#     if chars[i] == "a":
#         j += (i,)
# print(j)

# j = ()
# for i, val in enumerate(chars):
#     if val == "a":
#         j += (i,)
# print(j)
        


# x = [1,2,3,4,5,6]

# print(x[1:3:1])


# persons = {
# 1 : {"name": "ali", "age":12, "sports":["football", "basketball"]},
# 2 : {"name": "sara", "age":12, "sports":["football", "basketball"]},
# }

# print(persons[1]['name'])
# print(persons[1]['sports'][0])


all_p = {
    4251 : 'ali',
    2341:"reza"
    }
res = None
for person in all_p:
    if all_p[person] == "ali":
        res = person
print(list(all_p.keys()))

