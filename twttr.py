s = input("Word: ")
for c in s:
    match c:
        case "a" | "A":
            print("", end="")
        case "e" | "E":
            print("", end="")
        case "i" | "I":
            print("", end="")
        case "o" | "O":
            print("", end="")
        case "u" | "C":
            print("", end="")
        case _:
            print(c, end="")



