"""
Stampa una serie di fibonacci di 10 termini
"""

def fibonacci(n:int):
    if n<=0:
        return 0
    elif n ==1:
        return 1
    else:
        return int(fibonacci(n-1)+fibonacci(n-2))


def main():
    for i in range(10):
        print(fibonacci(i), end=' ')

if __name__ == "__main__":
    main()