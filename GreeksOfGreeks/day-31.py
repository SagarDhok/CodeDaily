
# Implement stack using array

#INPUT : 
# (i) 1 x   (a query of this type means  pushing 'x' into the stack)
# (ii) 2     (a query of this type means to pop an element from the stack and print the popped

class MyStack:
    
    def __init__(self):
        self.arr = []

    def push(self, data):
        self.arr.append(data)

    def pop(self):
        if not self.arr:
            return -1
        return self.arr.pop()


input_str = input("Enter your commands (e.g. 1 2 1 3 2 1 4 2): ")
commands = list(map(int, input_str.strip().split()))

stack = MyStack()

output = []

i = 0
while i < len(commands):
    if commands[i] == 1:
        i += 1
        stack.push(commands[i])
    elif commands[i] == 2:
        result = stack.pop()
        if result != -1:
            output.append(result)
    i += 1

print("Pop results:", " ".join(map(str, output)))
