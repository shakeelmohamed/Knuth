"""
1.1E: Greatest common factor of m & n, 2 positive integers:

  1. check that m >= n, swap if not
  2. m / n, set r to the remainder
  3. if r == 0, then n is the solution; else m = n, n = r, then repeat step 1

"""

def gcf(m, n):
    if m < n:
        temp = m
        m = n
        n = temp

    r = m % n

    if r == 0:
        return n
    return gcf(n, r)

def gcf_min(m, n):
    if m < n:
        m, n = n, m

    return n if (m % n == 0) else gcf_min(n, r)
