import math
import random


def find_period(a, N):
    """
    Simulates the period-finding result used by Shor's algorithm.

    A real quantum computer would use quantum period finding.
    Here we calculate it classically so that you can understand
    and test the full Shor workflow on a normal laptop.
    """

    value = 1

    for r in range(1, N):
        value = (value * a) % N

        print(
            f"r = {r:2d}   "
            f"{a}^{r} mod {N} = {value}"
        )

        if value == 1:
            return r

    return None


def shor_factor(N):

    print("\n====================================")
    print("         SHOR ALGORITHM DEMO")
    print("====================================")

    print(f"\nNumber to factor: N = {N}")

    # Even numbers are trivial
    if N % 2 == 0:
        return 2, N // 2

    while True:

        # Select random a
        a = random.randint(2, N - 1)

        print("\n------------------------------------")
        print(f"Selected a = {a}")

        # Step 1
        gcd_value = math.gcd(a, N)

        print(f"gcd({a}, {N}) = {gcd_value}")

        # Lucky case
        if gcd_value > 1:
            print("\nWe accidentally found a factor immediately!")

            return gcd_value, N // gcd_value

        print("\nSearching for period r...")
        print("------------------------------------")

        # Step 2
        r = find_period(a, N)

        if r is None:
            print("Period not found.")
            continue

        print(f"\nPeriod found: r = {r}")

        # Period must be even
        if r % 2 != 0:
            print("Period is odd.")
            print("Trying another value of a...")
            continue

        # Calculate a^(r/2)
        x = pow(a, r // 2)

        print(f"\na^(r/2) = {a}^{r // 2}")
        print(f"          = {x}")

        # Bad case
        if (x + 1) % N == 0:
            print("\na^(r/2) ≡ -1 mod N")
            print("Trying another a...")
            continue

        # Step 3
        factor1 = math.gcd(x - 1, N)
        factor2 = math.gcd(x + 1, N)

        print("\nCalculating factors:")

        print(
            f"gcd({x} - 1, {N}) = {factor1}"
        )

        print(
            f"gcd({x} + 1, {N}) = {factor2}"
        )

        if (
            factor1 not in (1, N)
            and factor2 not in (1, N)
        ):

            return factor1, factor2


# --------------------------------------------------
# MAIN PROGRAM
# --------------------------------------------------

N = 15

factor1, factor2 = shor_factor(N)

print("\n====================================")
print("             RESULT")
print("====================================")

print(f"{N} = {factor1} × {factor2}")

print("\nRSA modulus successfully factored.")