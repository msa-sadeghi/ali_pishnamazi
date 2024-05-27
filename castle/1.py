# def f(k = 0):
#     return 10 + k

# print(f(12))
# def f(*args):
#     res = 1
#     for n in args:
#         res *= n
#     return res

# print(f(12,13,14))



def f(**kwargs):
  
    return f'{kwargs.get("name")} {kwargs.get("family")}'

print(f(family="pishnamaz", name="ali"))