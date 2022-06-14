

def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if not n%2 or not n%3:
        return False
    i = 5
    stop = int(n**0.5)
    while i <= stop:
        if not n%i or not n%(i + 2):
            return False
        i += 6
    return True

class bs:
    def __init__(self, r0: int, r1: int) -> None:
        pass
        self.s = [1, 0]
        self.t = [0, 1]
        self.r = [r0, r1]
        self.r.append(int(r0 % r1)) 
        self.r.append(int(self.r[1] % self.r[2]))
        self.q = [None]

    def ss(self, i: int, q:int):
        # print(self.s[0])
        self.s.append(self.s[i - 2] - q *self.s[i-1])
        
    def tt(self, i: int, q:int):
        self.t.append(self.t[i - 2] - q * self.t[i - 1])
    
    def kq(self):
        while self.r[len(self.r) - 1] != 0:
            self.r.append(self.r[len(self.r) - 2] % self.r[len(self.r) - 1])
        for i in range(2, len(self.r)):
            self.q.append(int(self.r[i - 2] / self.r[i - 1]))
        for i in range(2, len(self.r) - 1):
            # print(i)
            self.ss(i, self.q[i - 1])
        for i in range(2, len(self.r) - 1):
            self.tt(i, self.q[i - 1])
        # print(self.r)
        # print(self.q)
        # print(self.s)
        # print(self.t)
        return self.t[-1]