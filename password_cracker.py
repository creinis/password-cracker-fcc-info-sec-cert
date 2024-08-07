import hashlib

def crack_sha1_hash(hash, use_salts=False):
    
    with open('top-10000-passwords.txt', 'r') as f:
        passwords = f.read().splitlines()
    
    if use_salts:
        with open('known-salts.txt', 'r') as f:
            salts = f.read().splitlines()
    else:
        salts = ['']
    
    return "PASSWORD NOT IN DATABASE"