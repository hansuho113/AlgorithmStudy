data = list(input())

number_dict = {2: ["A", "B", "C"], 3: ["D", "E", "F"], 4: ["G", "H", "I"],
               5: ["J", "K", "L"], 6: ["M", "N", "O"], 7: ["P", "Q", "R", "S"],
               8: ["T", "U", "V"], 9: ["W", "X", "Y", "Z"]}
time = 0
for a in data:
    for k, v in number_dict.items():
        if a in v:
            time += k+1

print(time)