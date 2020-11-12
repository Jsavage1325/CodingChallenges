# this challenge is to find all prime numbers in a decimal integer
# they then need to be sorted into ascending order
# if number is prime, it is not included
# for example 1717 => { 7, 7, 17, 71 }


# we need a function to check if a number is prime
def is_prime(n):
    if n == 1 or n == 0:
        return False
    for v in range(2, n - 1):
        if n%v == 0:
            return False
    return True


# we now need a function to get all the substrings of the number
def extract_primes(n):
    print("Extracting primes from: " + str(n))
    # convert to string as will be easier to do substrings of a string
    nString = str(n)
    answers = []
    # loop through every digit
    for d in range(len(nString)):
        # skip if 0
        if int(nString[d]) == 0:
            continue
        # loop through all the substrings (subintegers?)
        for ds in range(d, len(nString)):
            val = nString[d:ds + 1]
            if is_prime(int(val)) and int(val) != n:
                answers.append(int(val))
    answers.sort()
    return answers

def run_test(number, expected):
    if extract_primes(number) == expected:
        print("PASSED with 1717")



if __name__ == "__main__":
    print(extract_primes(1717))
    print(extract_primes(1))
    print(extract_primes(7))
    print(extract_primes(73))
    print(extract_primes(103))
    print(extract_primes(1313))