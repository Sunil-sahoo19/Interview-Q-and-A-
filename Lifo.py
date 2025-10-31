from queue import LifoQueue

stack = LifoQueue()

stack.put('A')
stack.put('B')

print(stack.get())  # B
print(stack.get())  # A



from queue import LifoQueue
stack = LifoQueue()
stack.put(10)
stack.put(20)
stack.put(30)
stack.put(40)
print("stack size:", stack.qsize())
print("popped:", stack.get())
print("popped:", stack.get())
print("popped:", stack.get())
print("Is empty?", stack.empty())

