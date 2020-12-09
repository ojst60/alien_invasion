import math
# function to find the simutaneous equation
a = float(input("Enter the value of a : "))
b = float(input("Enter the value of b:  "))
c = float(input("Enter the value of c:  "))
sol=float(input("Enter the value of solution: "))
real_c=c - sol
def square_root(a, real_c, b):
    num=(b**2)-4 *(a) * (real_c)
    sol_square_root=math.sqrt(num)
    print(sol_square_root)
    return sol_square_root

def positive_num(b ):
    pos = square_root(a,real_c, b)
    sol_positive_num =- b + pos
    return sol_positive_num

def negative_num(b):
    neg = square_root(a, real_c, b)
    sol_negative_num =- b - neg
    return sol_negative_num

def deno(a):
    soln_den = 2 * a
    return soln_den

def solution():
    pos_num = positive_num(b)
    neg_num = negative_num(b)
    deno_num =deno(a)
    first_x = pos_num/deno_num
    second_x = neg_num/deno_num
    print("The first solution is {}".format(first_x))
    print("The second solution is {}".format(second_x))

solution()

