#!/usr/bin/python3
"""Prime game module.
"""


def isWinner(rounds, nums):
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

    marias_wins, bens_wins = 0, 0
    # generate primes with a limit of the maximum number in nums
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False

    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False

    # Count wins based on the number of primes up to each number in nums
    for _, n in zip(range(rounds), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1

    if marias_wins == bens_wins:
        return None

    return 'Maria' if marias_wins > bens_wins else 'Ben'
