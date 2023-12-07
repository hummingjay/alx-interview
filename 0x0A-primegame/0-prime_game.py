#!/usr/bin/python3
"""
Maria & Ben are playing a game. Given a set of consecutive
integers starting from 1 up to and including n, they take
turns choosing a prime number from the set & removing that
number and its multiples from the set.
The player that cannot make a move loses the game.

They play x rounds of the game, where n may be different
for each round. Assuming Maria always goes first and both
players play optimally, determine who the winner of each
game is.
"""


def isWinner(x, nums):
    # checks if num is prime
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    # makes a list of primes
    def get_primes(n):
        primes = []
        for i in range(n+1):
            if is_prime(i):
                primes.append(i)
        return primes

    # Remove prime and multiples
    def p_n_m(prime, numbers):
        # using shallow copy for iteration
        for num in numbers.copy():
            if num % prime == 0:
                numbers.remove(num)
        return numbers

    # main code
    maria_win = 0
    ben_win = 0

    for _ in range(x):
        maria_turn = True
        primes = get_primes(nums[_])
        turn = [*range(nums[_] + 1)]

        while primes: # while list not empty
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
