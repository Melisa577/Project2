def main():
    n , m = input()
    result = eratosthenes(n, m)
    return result

def input();
    n = input()
    n = int(n)
    m = input()
    m = int(m)
    return n , m

def is_prime(numbers):
    if number <= 1:
        return false
    for i in range(2 , numbers):
        if numbers % i== 0:
            return false
        return true

def least_factor(numbers):
    if numbers <= 1:
        return 1
    for i in range(2,numbers):
        if numbers % i == 0:
            return i

def eratosthenes(n , m):
    if is_prime(m):
        return -1
    count = 0
    for r in range(m):
        if not is_prime(r) and least_factor(r) <= least_factor(m):
            count += 1
    for r in range(m+1, n+1):
        if not is_prime(r) and least_factor(r) < least_factor(m):
            count += 1
        return count
if__name__ == '__main__':
    print(main())