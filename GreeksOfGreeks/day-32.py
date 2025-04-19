
# Queue Using Array

#INPUT : 
# (i) 1 x   (a query of this type means  pushing 'x' into the stack)
# (ii) 2   (a query of this type means to pop an element from the stack and print the popped


class MyQueue:
    def __init__(self):
        self.queue = [] 

    def push(self, x):
        self.queue.append(x)  
    def pop(self):
        if not self.queue:
            return -1  
        else:
            return self.queue.pop(0)  


input_str = input("Enter your commands (e.g. 1 4 1 5 2 2): ")
commands = list(map(int, input_str.strip().split()))

queue = MyQueue()

output = []

i = 0
while i < len(commands):
    if commands[i] == 1:
        i += 1
        queue.push(commands[i])
    elif commands[i] == 2:
        result = queue.pop()
        if result != -1:
            output.append(result)
    i += 1

print("Pop results:", " ".join(map(str, output)))
