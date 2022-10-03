
def prime_numbers(number):
    prime = []
    cache = {}
    for x in range(2, number + 1):
        is_prime = cache.get(x)
        if is_prime is False:
            continue
        prime.append(x)
        cache[x] = True
        for y in range(x*2, number+1, x):
            cache[y] = False
    return prime, cache

print(prime_numbers(100))