def checkPrime(x):
    if x > 1:
        for i in range(2, int(x / 2) + 1):
            if (x % i) == 0:
                return False

            else:
                return True


if __name__ == "__main__":
    a = int(input("Enter a Number: "))
    res = checkPrime(a)
