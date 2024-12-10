#!/usr/bin/env python3
def isWinner(x, nums):
    # Helper function to generate primes up to a maxim
    def sieve(n):
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False  # 0 and 1 are not primes
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return primes

    if x < 1 or not nums:
        return None

    # Find the maximum n to precompute primes
    max_n = max(nums)
    primes = sieve(max_n)
    # Precompute the number of primes up to each number
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    # Evaluate each round
    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1  # Maria wins if the number of primes is odd
        else:
            ben_wins += 1  # Ben wins if the number of primes is even

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
