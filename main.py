# string, integer, bool, float, double, char

# --------------Data types--------------
skaicius = 0
zodis = "zodis"
flag = False
floatas = 0.000000002222222222

# --------------Data structures--------------
phone_list = ["iphone 12", "samsung 20", "nokia 3310"]
tv_list = ["lg22222", "samsungtv22222", "silelis22"]
phone_list1 = ["stringas", "stringas", 1, 1, 2, 3, 4, 5, False, False]
number_list = [1, 2, 3, 4, 5, 6, 7]
no_duplicate_set_from_list = set(phone_list1)

# We can change records that are in the list
mutable = ["iphone12", "samsung20"]
mutable[0] = "iphone13"

# We can't change, delete any tuple records
immutable = ("iphone12", "samsung20")

# In other languages it is called hash map
dictionary = {"mobile_phones": phone_list, "tv": tv_list}

# --------------printing--------------
print(phone_list)
print(immutable)
print(dictionary.values())

# --------------if logic gates--------------

if zodis == skaicius:
    print("zodis lygus skaiciui")
else:
    print("padaryta kazka kito")

if len(phone_list) == len(immutable):
    print("Sitie listai yra lygus")
elif phone_list == immutable:
    print("lygus listai")
else:
    print("Neivyko funcionalumas")

# Bad logic statement example (Most of the time this is the wrong approach)
# if len(phone_list) == len(immutable):
#     print("Sitie listai yra lygus")
# if phone_list == immutable:
#     print("lygus listai")
# else:
#     print("Neivyko funcionalumas")

# --------------loops--------------
for i in phone_list:
    print(i)

count = 0
while (flag == False):
    count += 1
    if count > 5:
        flag = True
        print("flag was changed")


# --------------Functions/Methods--------------
def funcija(sarasas, sarasas1):
    print(phone_list)
    print(tv_list)


class User:
    def method(self, sarasas, sarasas1):
        print(sarasas)
        print(sarasas1)


# --------------Fuction call/Method call--------------
# --------------Function call--------------
funcija(phone_list, tv_list)

# --------------Method call--------------
# Creates instance
user = User()
user.method(phone_list, tv_list)

# --------------Access data structures--------------
# --------------List index access--------------
pirmas_indeksas = phone_list[1]
print(pirmas_indeksas)

# --------------Dictionary access--------------
print(dictionary["mobile_phones"])
print(dictionary.values())


# --------------Bubble sort--------------
# [7,3,2,8,2,1,5,3,2,1,7,3,2] -> Bubble sort -> [1,1,2,2,2,2,3,3,3,5,7,7,8]
# 1: while loop
# 2: 7,3 -> is 7 higher number than 3 if yes switch places (temp variable)

def bubble_sort():
    bubble_sort_list = [1, 2, 3, 4, 5, 6, 7, 9, 8]
    is_sorting_finished = False
    iteration_counter = 0
    while is_sorting_finished == False:
        did_sort_happen = False
        for i in range(len(bubble_sort_list) - 1):
            if bubble_sort_list[i] > bubble_sort_list[i + 1]:
                temp = bubble_sort_list[i]
                bubble_sort_list[i] = bubble_sort_list[i + 1]
                bubble_sort_list[i + 1] = temp
                did_sort_happen = True
            iteration_counter += 1
        iteration_counter += 1
        if did_sort_happen == False:
            is_sorting_finished = True
    print(bubble_sort_list)
    print(iteration_counter)


# 9*9 = 81
bubble_sort()


# --------------Fibonacci--------------
def fibonacci(fibonacci_index):
    n1 = 0
    n2 = 1
    fibonacci_sequence = [n1, n2]

    for i in range(fibonacci_index - 2):
        n1 = fibonacci_sequence[-2]
        n2 = fibonacci_sequence[-1]
        new_number = n1 + n2
        fibonacci(fibonacci_index)
        fibonacci_sequence.append(new_number)
    print(fibonacci_sequence)


# Task for who want to try and solve this
def fibonacci_recursive(n):

    if n <= 0:
        print("unable to return fibonacci")

    elif n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1

    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

print(fibonacci_recursive(0))
