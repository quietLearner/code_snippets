my_list = [1, 2, 3, 4, 5]


for i in my_list:
    print(i)
    if i == 3:
        break
else:  # no break will trigger this else statement
    print("Hit the For/Else Statement!")


for i in my_list:
    if i == 3:
        print("Item found!")
        break
else:
    print("Item not found!")
