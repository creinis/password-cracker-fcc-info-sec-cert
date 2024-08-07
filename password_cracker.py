import hashlib

def crack_sha1_hash(hash, use_salts=False):
    
    with open('top-10000-passwords.txt', 'r') as f:
        passwords = f.read().splitlines()
    
    
    return "PASSWORD NOT IN DATABASE"