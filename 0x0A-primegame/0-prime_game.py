#!/usr/bin/python3
"""
Prime Game module
"""

def isWinner(x, nums):
    """
    Determines the winner of a series of
    prime number games played by Maria and Ben.

    Each game consists of consecutive integers
    from 1 to n, where players take turns
    picking a prime number and removing it
    along with its multiples from the set.
    The player unable to make a move loses.

    Parameters:
    x (int): The number of rounds played.
    nums (List[int]): A list containing the values
    of n for each round.

    Returns:
    str or None: The name of the player who won
                the most rounds ('Maria' or 'Ben').
                If there is a tie, returns None.
    """

    def generate_primes(n):
        """
        Generates a list of prime numbers up to n using
        the Sieve of Eratosthenes.

        Parameters:
        n (int): The upper limit to generate prime numbers.

        Returns:
        List[int]: A list of prime numbers up to n.
        """
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if (is_prime[p]):
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, n + 1) if is_prime[p]]

    def simulate_game(n):
        """
        Simulates the game for a given n and determines the winner.

        Parameters:
        n (int): The upper limit of the set of integers.

        Returns:
        str: The winner of the game ('Maria' or 'Ben').
        """
        if n < 2:
            return 'Ben'  # No primes available, Ben wins by default.
        primes = generate_primes(n)
        prime_count = len(primes)

        # The winner is determined by the count of primes
        return 'Maria' if prime_count % 2 == 1 else 'Ben'

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = simulate_game(n)
        if winner == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
