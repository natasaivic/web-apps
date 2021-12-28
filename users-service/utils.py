import hashlib

def md5(input):
    """
    Returns a MD5 hash of the string.
        md5("nata1") -> 2ecface7be4ff3017ac0989971fb7e69
    """
    return hashlib.md5(input.encode()).hexdigest()