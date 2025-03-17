def stack():
    stack = []
    while True:
        command = input().strip().split()
        if not command:
            continue
        elif command[0] == 'push':
            stack.append(int(command[1]))
            print("ok")
        elif command[0] == 'pop':
            poped = stack.pop()
            print(poped)
        elif command[0] == 'back':
            print(stack[-1])
        elif command[0] == 'size':
            print(len(stack))
        elif command[0] == 'clear':
            stack.clear()
            print("ok")
        elif command[0] == 'exit':
            print("bye")
            break

if __name__ == '__main__':
    stack()

