import random
import os
x = [1,2,3]

score = 0
if os.path.exists("result.txt"):
    with open("result.txt", "r") as f:
        high_score = int(f.read())
else:
    high_score = 0
while True:
    s = random.choice(x)
    g = int(input("> a number or 0 to exit"))
    if g == 0:
        with open("result.txt","w") as f:
            f.write(str(high_score))
        break
    if g == s:
        score += 1
        if score > high_score:
            high_score = score
    print("score:", score)
    print("high_score:", high_score)
        
    