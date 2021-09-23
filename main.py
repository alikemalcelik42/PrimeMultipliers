# Asal Çarpanlar

def FindPrimeMultipliers(num):
    multipliers = []
    for interimNum in range(1, num+1):    
        if num % interimNum == 0 and CheckPrime(interimNum):
            multipliers.append(interimNum)
    return multipliers

def CheckPrime(num):
    count = 0
    for interimNum in range(2, num):
        if num % interimNum == 0:
            count += 1
    if count != 0:
        return False
    return True

number = int(input("Enter Number: "))
primeMultipliers = FindPrimeMultipliers(number)
print(primeMultipliers)