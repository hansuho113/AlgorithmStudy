lines = int(input())
for line in range(lines):
    spaces = (lines) - (line+1)
    print(" "*spaces + "*"*(line+1))