#!/usr/bin/python3
"""
Prime Game module
"""


def isWinner(x: int, nums: list[int]) -> str:
    """
    Determines the winner of a prime number removal game between Maria and Ben.

    Args:
        x: The number of rounds to play.
        nums: A list of consecutive integers starting from 1 up to and
            including n (where n varies for each round).

    Returns:
        A string indicating the winner ("Maria", "Ben", or "None" if a winner
        cannot be determined).

    This function simulates a game where Maria and Ben take turns removing
    prime numbers and their multiples from a set of consecutive integers.
    The player who cannot make a move loses the round. The function plays
    x rounds and returns the name of the player who wins the most rounds.
    If both players win an equal number of rounds, the function
    returns "None".

    Assumptions:
        - n and x are less than or equal to 10000.
        - No external libraries are imported.
    """
    def find_primes(numbers: set[int]) -> set[int]:
        """
        Finds prime numbers within a set of integers.

        Args:
            numbers: A set of integers.

        Returns:
            A set containing the prime numbers from the input set.
        """
        primes = set()
        for num in numbers:
            if num > 1 and is_prime(num):
                primes.add(num)
        return primes

    def is_prime(num: int) -> bool:
        """
        Checks if a number is prime.

        Args:
            num: An integer.

        Returns:
            True if the number is prime, False otherwise.
        """
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def remove_multiples(nums: list[int], prime: int):
        """
        Removes multiples of a prime number from a list of integers.

        Args:
            nums: A list of integers.
            prime: The prime number to remove multiples of.
        """
        nums[:] = [num for num in nums if num % prime != 0]

    maria_wins, ben_wins = 0, 0
    for _ in range(x):
        # Simulate each round
        available_primes = find_primes(set(nums))
        while available_primes:
            prime = available_primes.pop()
            remove_multiples(nums, prime)
            if not available_primes:
                # Ben wins if Maria can't choose a prime
                ben_wins += 1
                break
        nums.clear()  # Reset nums for the next round
    # Determine winner based on round wins
    return "Maria" if maria_wins > ben_wins else ("Ben" if ben_wins > maria_wins else "None")
