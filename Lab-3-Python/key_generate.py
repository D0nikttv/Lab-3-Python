from random import choice, shuffle
def key_generate(lenght=5):
    alph = '1234567890ABCDF'
    full_alph = '1234567890qwertyuiopasdfghjklzxcvbnm'
    
    s_hex = ''
    for _ in range(lenght):
        s_hex += choice(alph)
    s_dec = str(int(s_hex,16))

    key = []
    count = 0
    while len(key) < 3:

        block = f'{s_dec[count]}'
        for _ in range(4):
            block += choice(full_alph)
        block = list(block)    
        shuffle(block)
        block = ''.join(block)
        key.append(block)

        count += 1
    
    return f'{'-'.join(key)} {s_dec[-2:]}'

