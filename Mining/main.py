from hashlib import sha256

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

print( (10 > 5)   (2 > 1) )