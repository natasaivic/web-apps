import hashlib

def md5(input):
    return hashlib.md5(input.encode()).hexdigest()