import re
pattern = re.compile(r'^1?$|^(11+?)\1+$')

def is_prime(n):
        return False if pattern.search("1"*n) else True
