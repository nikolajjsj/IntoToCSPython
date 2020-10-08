def printMove(from_stack, to_stack):
    print('Move from ' + str(from_stack) + ' to ' + str(to_stack))

def towers_of_hanoi(n, from_stack, to_stack, spare_stack):
    if n == 1:
        printMove(from_stack, to_stack)
    else:
        towers_of_hanoi(n-1, from_stack, spare_stack, to_stack)
        towers_of_hanoi(n, from_stack, to_stack, spare_stack)
        towers_of_hanoi(n-1, spare_stack, to_stack, from_stack)