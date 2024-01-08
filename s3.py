# name = input("enter a name: ")
# age = int(input("enter an age: "))

# if age <= 7:
#     print(f'{name} you are kid')
# elif age >= 8 and age <= 13:
#     print(f'{name} you are junior')
# elif age >= 13 and age <= 18:
#     print(f'{name} you are teenager')
# else:
#     print(f'{name} you are adult')
# username = input("enter the username: ")
# if username == "root" or username == "admin":
#     print(f'{username} is valid')
# else:
#     print(f'{username} is not valid')

"""
برنامه ای بنویس که نام فرد را از ورودی دریافت کند و در صورتی که اولین کاراکتر اسم آن فرد
a
باشد
welcome
و در صورتی که اولین کاراکتر اسمش 
a
و آخرین کاراکتر اسمش 
a
باشد
good
را پرینت نماید

"""
# name = input("enter a name: ")
# print(name[0])
# name[-1]
# name[len(name)-1]

# TODO
"""
برنامه ای بنویس که نام
و نمرات سه درس یک دانش آموز را از ورودی دریافت نماید
و معدل دانش آموز را محاسبه نماید
معدل یعنی مجموع نمرات تقسیم بر تعداشان

اگر معدل دانش آموز از 90 بیشتر بود
A
اگر معدل دانش آموز از 80 بیشتر بود
B
اگر معدل دانش آموز از 70 بیشتر بود
C
اگر معدل دانش آموز از 60 بیشتر بود
D
اگر معدل دانش آموز از 50 بیشتر بود
E
در غیراینصورت
F
را نمایش دهد


"""

name = input("enter a name: ")
print(len(name))
for i in range(len(name)):
    print(name[i])
