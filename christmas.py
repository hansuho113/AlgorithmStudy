from colorama import init

init()

from colorama import Fore, Back, Style

size = 11

for i in range(0, size):
    if i == 0:
        print(Fore.YELLOW + "  ⭐️ ".center(size, " "))
    elif i % 2 == 0 and i > 0:
        if i < 3:
            print(Fore.LIGHTWHITE_EX + "❄︎ ☼" + Fore.GREEN + ("*" * i).center(size - 5, " ")+Fore.LIGHTWHITE_EX + "❄︎ ☼")
        elif i < 5:
            print(Fore.LIGHTWHITE_EX+"☼"+ Fore.GREEN + ("*" * i).center(size -2, " ")+Fore.LIGHTWHITE_EX+"☼")
        else:
            print(Fore.GREEN + ("*" * i).center(size+1, " "))
    else:
        if i == 1:
            print(Fore.LIGHTWHITE_EX+"  ☼"+Fore.RED + ("\'" * (i + 1)).center(size -6, " ")+Fore.LIGHTWHITE_EX+" ☼  ")
        elif i == 3:
            print(Fore.LIGHTWHITE_EX+" ☼"+Fore.RED + ("\'" * (i + 1)).center(size - 4," ") + Fore.LIGHTWHITE_EX + " ☼  ")
        else:
            print(Fore.RED + ("\'" * (i + 1)).center(size + 1, " "))

init(autoreset=True)

print("")
print(Back.RED + "Merry".center(size + 2, ' '))
print(Back.GREEN + "Christmas !".center(size + 2, ' '))
print("")