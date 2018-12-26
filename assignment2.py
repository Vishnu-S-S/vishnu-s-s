
def prime(num):
    if num < 2:
        return False

    for i in range(2, num // 2):
        if (num % i) == 0:
            return False

    return True


def factors(no):

    factor_list = [1, no]
    for i in range(2, no // 2):
        if (no % i) == 0:
            factor_list.append(i)

    return factor_list


def primefact(a):

    factor_list = factors(no)

    fact_list = []

    for j in factor_list:
        if prime(j):
            fact_list.append(j)

    return fact_list


print('Prime no')
num = int(input('Enter no for check prime or not'))
prime(num)
if prime(num) is False:
    print(num, 'is not prime')
else:
    print(num, "is prime")

print('Factors')
no = int(input("Enter no for finding factor"))
factor_list = factors(no)
print(' factor list is', factor_list)

print('primeFact')
a = int(input('Enter value for prime factor'))
primefact(a)
fact_list = primefact(a)
print(' factor list is', fact_list)
