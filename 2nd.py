
class User:
    def __init__(self, username, password, first_name, last_name):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name


user1 = User("asd", "asd", "asd", "asd")
user2 = User("asd", "asd", "asd", "asd")

print(user1.first_name)



def carry_solver(n1, n2):
    longer_number = max(len(str(n1)), len(str(n2)))
    c = 0
    carry = 0
    for i in range(longer_number):
        carry = n1 % 10 + n2 % 10 + carry
        if carry >= 10:
            carry = 1
        else:
            carry = 0
        c += carry
        n1 = n1 // 10
        n2 = n2 // 10
    if c == 0:
        print("no carry")
    else:
        print("carry counter: " + str(c))

carry_solver(6549846165, 516886513)

