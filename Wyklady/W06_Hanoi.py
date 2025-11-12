from msvcrt import getch

# three towers
A = 'A'
B = 'B'
C = 'C'

pathOfRecursionTree = []
numberOfRecCall = 0

BEGINNING = 0
AFTER_FIRST_CALL = 1
AFTER_SECOND_CALL = 2
END_OF_CALL = 3

def recursionStart():
    global pathOfRecursionTree
    global numberOfRecCall
    numberOfRecCall += 1
    pathOfRecursionTree.append(numberOfRecCall)
    print(f"The actual path in the recursion tree: {pathOfRecursionTree}")
    getch()

def recursionEnd():
    global pathOfRecursionTree
    global numberOfRecCall
    x = pathOfRecursionTree.pop()
    print(f"The end of recursion call nr.: {x}")
    #print(f"The actual path in the recursion tree: {pathOfRecursionTree}")
    getch()

def hanoiRec(n, source, target, aux):
    recursionStart()
    print(n,source,target,aux)
    if n<=0:
        recursionEnd()
        return
    if n == 1:
        print(f'Move disk from tower {source} to tower {target}')
        recursionEnd()
        return
    # Move n - 1 disks from source to auxiliary
    hanoiRec(n - 1, source, aux, target)
    # Move the biggest disk from source to target
    print(f'Move disk from tower {source} to tower {target}')
    # Move the n - 1 disks that we left on auxiliary to target
    hanoiRec(n - 1, aux, target, source)
    recursionEnd()

def hanoiRecClean(n, source, target, aux):
    print(n,source,target,aux)
    if n<=0:
        return
    if n == 1:
        print(f'Move disk from tower {source} to tower {target}')
        return
        # Move n - 1 disks from source to auxiliary
    hanoiRecClean(n - 1, source, aux, target)
    # Move the biggest disk from source to target
    print(f'Move disk from tower {source} to tower {target}')
    # Move the n - 1 disks that we left on auxiliary to target
    hanoiRecClean(n - 1, aux, target, source)

def printStack(s):
    print('Stack\n')
    for i in reversed(s):
        print(i)


def hanoiIter(n, source, target, aux):
    stack = [(n, source, target, aux)]
    while stack:
        printStack(stack)
        getch()
        n, source, target, aux = stack.pop()
        if n<=0:
            continue
        if n == 1:
            print(f'Move a disk from {source} to {target}')
            continue
        stack.append((n - 1, aux, target, source))
        stack.append((1, source, target, aux))
        stack.append((n - 1, source, aux, target))

def hanoiIter2(n,source, target,aux):
    #stack = [(BEGINNING, n, source, target, aux)]
    stack = []
    whereToStart = BEGINNING
    while True:
        print(stack)
        print("Computing: ", end="")
        print(whereToStart,n, source, target,aux)
        getch()
        if whereToStart <= BEGINNING:
            if n<=0:
                whereToStart = END_OF_CALL
            if n == 1:
                print(f'Move disk from tower {source} to tower {target}')
                whereToStart = END_OF_CALL
            # Move n - 1 disks from source to auxiliary
        if whereToStart <=BEGINNING:
            stack.append((AFTER_FIRST_CALL, n, source, target, aux))
            #hanoiRec(n - 1, source, aux, target)
            whereToStart, n, source, target, aux = BEGINNING, n-1,source, aux, target
            continue
        if whereToStart <=AFTER_FIRST_CALL:
            # Move the biggest disk from source to target
            print(f'Move disk from tower {source} to tower {target}')
            # Move the n - 1 disks that we left on auxiliary to target
            stack.append((AFTER_SECOND_CALL, n, source, target, aux))
            # hanoiRec(n - 1, aux, target, source)
            whereToStart, n, source, target, aux = BEGINNING, n-1, aux, target, source
            continue
        if whereToStart <= END_OF_CALL:
            if not stack:
                return
            whereToStart, n, source, target, aux = stack.pop()

# Ackermann function
# A(2,1) = 5
# A(3,4) = 125
# A(4,3) = 2^(2^65536) - 3
def Ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return Ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        return Ackermann(m - 1, Ackermann(m, n - 1))

# test the function
def main():
    #hanoiIter2(3, A, C, B)
    input("Hanoi Recursive")
    hanoiRecClean(3, A, C, B)
    input("Hanoi Recursive")
    hanoiRec(3, A, C, B)

if __name__ == '__main__':
    main()