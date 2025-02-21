import random, string

alphabet = string.ascii_letters + string.digits
def passgen(l: int = 15):
    key = ''
    for i in range(l):
        key += random.choice(alphabet)
    return key