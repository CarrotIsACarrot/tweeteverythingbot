# first code!!!
import time
characters = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ")

# Which character is selected.
selected_Char = -1
# Ammount of characters. 1 = a, 3 = aaa, 280 = aaaaaaaaaaaaaaaaaaaaaaaAAAAAAAAAAAAAAAAAAAAAAAAa!!!!!!!!
level = 1

# counts from a - " ", gives error after last entry. will be fixing soon. Edit: Fixed

while True:
    if selected_Char == 26:
        level = level + 1
        selected_Char = -1
    selected_Char = selected_Char + 1 
    ammount = selected_Char
    final_Tweet = characters[selected_Char]
    print(final_Tweet)
    # This should write to the file whatever letter this is on. Doesn't work currently. Might fix. Might steal code.
    with open ("/home/carrot/Desktop/everytweet/countsave.txt", "a+") as file:
        selcharfile = file.read()
        file.write(str(final_Tweet))
    time.sleep(1)
        

