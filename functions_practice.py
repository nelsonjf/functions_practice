def hello():
    return print("Hello, User!")

def pack(a, b, c):
    pack_list = [a, b, c]
    return print(pack_list)

def eat_lunch(list):
    if len(list) > 0 :
        print("First I eat", list[0])
        i = 1
        while i < len(list):
            print("Next I eat", list[i])
            i = i + 1
    else:
        print("My lunch box is empty!")

hello()
pack("Milk", "Eggs", "Butter")
eat_lunch([])
eat_lunch(["Sandwich", "Chips", "Fruit"])