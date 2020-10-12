def genPrimes():
    primes = []
    recent = 1
    while True:
        recent += 1
        for p in primes:
            if recent % p == 0:
                break
        else:
            primes.append(recent)
            yield recent
