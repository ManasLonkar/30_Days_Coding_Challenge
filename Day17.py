class PrimeFactorization:
    def factorize(self, n):
        i = 2
        factors = []
        while n > 1:
            if n % i == 0:
                factors.append(i)
                n //= i
            else:
                i += 1
        return factors