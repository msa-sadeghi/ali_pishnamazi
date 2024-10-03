class Dog:
    def __init__(self, name) -> None:
        self.name = name
    # def __str__(self) -> str:
    #     return self.name
    
    
d1 = Dog("jessi")
d2 = d1
print("before")
print(d1)
print(d2)



d2.name = "mmmmmmmmmmmmm"
print("after")
print(d1)
print(d2)