#!/usr/bin/python3
"""
Maria & Ben are playing a game. given integers
make list then determine winner when can't play next round.
"""


def isWinner(x, nums):
    """
    checks to find the winner of the game
    """
    # checks if num is prime
    def is_prime(num):
        """
        checks if num is a prime
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    # makes a list of primes
    def get_primes(n):
        """
        Gathers Prime Numbers and returns list
        """
        primes = []
        for i in range(n+1):
            if is_prime(i):
                primes.append(i)
        return primes

    # Remove prime and multiples
    def p_n_m(prime, numbers):
        """
        Removes the prime number and its multiples
        """
        # using shallow copy for iteration
        for num in numbers.copy():
            if num % prime == 0:
                numbers.remove(num)
        return numbers

    # main code
    maria_win = 0
    ben_win = 0

    for _ in range(x):
        if _ >= len(nums):
            _ %= len(nums)
        maria_turn = True
        primes = get_primes(nums[_])
        turn = [*range(nums[_] + 1)]

        while primes:  # while list not empty
            prime = min(primes)
            primes.remove(prime)
            p_n_m(prime, turn)
            maria_turn = not maria_turn

        if maria_turn:
            ben_win += 1
        else:
            maria_win += 1

    # determine overall winner
    if maria_win > ben_win:
        return "Maria"
    elif ben_win > maria_win:
        return "Ben"
    else:
        return None
