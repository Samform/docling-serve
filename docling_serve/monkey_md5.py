# Vi patcher inn en overstyring for hashlib.md5 for å jobbe
# rundt en problemstilling i vårt Markdown API, som kjører på
# CUDA i Azure Container app med GPU. MD5 er ikke godkjent brukt
# i FIPS-miljøer

import hashlib
original_md5 = hashlib.md5

def md5_non_security(*args, **kwargs):
    kwargs['usedforsecurity'] = False
    return original_md5(*args, **kwargs)

hashlib.md5 = md5_non_security
