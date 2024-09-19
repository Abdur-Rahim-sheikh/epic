import math
class diaphantine:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def has_integer_solution(self):
        return self.c % math.gcd(self.a, self.b) == 0
    def solve(self)->tuple:
        if not self.has_integer_solution():
            return "No solution"
        x, y = self.extended_gcd(self.a, self.b)
        x *= self.c
        y *= self.c
        return (x, y)
    
    def extended_gcd(self, a, b)->tuple:
        if b == 0:
            return 1, 0
        x1, y1 = self.extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return x, y
    

if __name__ == "__main__":
    a = [2, 3, 4, 5, 6]
    b = [3, 4, 5, 6, 7]
    c = [5, 6, 7, 8, 9]
    for i in range(5):
        d = diaphantine(a[i], b[i], c[i])
        print(f"for {a[i]}x + {b[i]}y = {c[i]}, (x,y) = {d.solve()}")