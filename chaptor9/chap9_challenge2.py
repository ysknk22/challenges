a = input("What is your favorite food?: ")

with open("answer.txt", "w") as f:
    f.write(a)