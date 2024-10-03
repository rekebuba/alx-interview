#!/usr/bin/python3
"""Prime game module.
"""


def is_winner(rounds: int, nums: list[int]) -> str | None:
    """Determines the winner of a prime game session with `rounds` rounds.

    Args:
        rounds (int): The number of rounds to play.
        nums (list[int]): A list of integers representing
                        the upper limits for each round.

    Returns:
        str | None: The name of the winner ('Maria' or 'Ben'),
                    or None if there is a tie or invalid input.
    """
    if rounds < 1 or not nums:
        return None

    marias_wins = 0
    bens_wins = 0
    max_number = max(nums)

    # Generate primes using the Sieve of Eratosthenes
    primes = [True] * (max_number + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime numbers

    for i in range(2, int(max_number**0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_number + 1, i):
                primes[j] = False

    # Count wins based on the number of primes up to each number in nums
    for upper_limit in nums[:rounds]:
        prime_count = sum(primes[:upper_limit])
        if prime_count % 2 == 0:
            bens_wins += 1
        else:
            marias_wins += 1

    if marias_wins == bens_wins:
        return None

    return 'Maria' if marias_wins > bens_wins else 'Ben'
