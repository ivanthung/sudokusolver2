import sdkvalid
import numpy as np

def simple_recursion(sdk, iterations=0):
    iterations = 0

    for x in range (0,9):
        for y in range (0,9):
            if sdk[x,y] == 0:
                iterations +=1
                for n in range(1,10):
                    if sdkvalid.is_possible((x,y), n, sdk):
                        sdk[x,y] = n
                        simple_recursion(sdk, iterations)
                        sdk[x,y] = 0
                return
    print(iterations, sdk)
    input("more")
