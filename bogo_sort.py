def prime_number_v1(numbers):
    prime = []
    for i in range(2, numbers):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime.append(i)
    return prime


# print(prime_number_v1(1000))



def prime_number_v2(number):
    prime = []
    cashe = {}
    for x in range(2, number):
        if cashe.get(x) is False:
            continue
            # break
        else:
            prime.append(x)
            for y in range(x*2, number, x):
                cashe[y] = False
    return prime


print(prime_number_v2(100))
print(dir('i'))
