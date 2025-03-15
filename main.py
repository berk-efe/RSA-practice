import math
import time

LIMIT = 9999

def main():
    keys = generate_keys(limit=LIMIT)
    print(keys)
    plain_text = input("Give Message: \n") # ABC
    start_time_enc = time.time() # start time
    cypher_text = encrypt_data(plain_text, keys["public_key"])
    encryption_time = time.time() - start_time_enc # end time
    print(f"cypher text: {cypher_text}")
    
    start_time_dec = time.time()
    old_plain_text = decrypt_data(cypher_text, keys["private_key"])
    decryption_time = time.time() - start_time_dec
    print(f"old plain text: {old_plain_text}")
    print(f"Encryption: {encryption_time} seconds \n Decryption: {decryption_time} seconds")
    
    pass


# convert string into int
def string2int(s:str) -> list[int]:
    result = []
    for i in s:
        result.append(ord(i))
    return result


# convert int into string
def int2string(list_of_dec:list[int]) -> str:
    result = []
    for i in list_of_dec:
        result.append(chr(i))
    return "".join(result)

# generate prime numbers
def is_prime(num:int) -> bool:
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(limit:int) -> list[int]:
    primes = []
    for num in range(limit, 1, -1):
        if is_prime(num) and len(primes) < 2:
            primes.append(num)
    return primes


# generating keys
def generate_keys(limit:int) -> dict:
    primes = generate_primes(limit=limit)
    print(primes)
    
    p = primes[0]
    q = primes[1]
    
    # p=2, q=7
    N = p*q # 14
    phiN = (p-1)*(q-1) # 6
    
    # THESE EXAMPLES ONLY WORK FOR SMALL NUMBERS AS PLAIN TEXT!
    # THEY WONT WORK IF THE NUMBER YOU ARE TRYING TO ENCRYPT IS BIGGER THAN THE MOD!!!
    
    # 1 < e < phiN (6)
    E = 0
    print("N", N, phiN)
    for i in range(phiN, 3, -1):
        if N % i != 0 and phiN % i != 0:
            print(f"coprime with N and phiN: {i}")
            E = i
            break

    
    # d*e % phiN == 1
    D = phiN*2-1
    print("D", D)

    public_key = (E, N)
    private_key = (D, N)
    
    return {
        'public_key': public_key,
        'private_key': private_key
    }

# encryption
def encrypt_data(t:str, public_key:tuple) -> list[int]:
    data = string2int(t) # [65, 66, 67] "ABC"
    print(data)
    E = public_key[0]
    N = public_key[1]
    
    
    cypher_data = []
    for i in data:
        # cypher_i = i**E % N <- WRONG! so slow
        cypher_i = pow(i, E, N)
        cypher_data.append(cypher_i)
    
    
    return cypher_data

# decryption
def decrypt_data(l_i:list[int], private_key:tuple) -> str:
    D = private_key[0]
    N = private_key[1]
    
    refined_data = []
    for i in l_i:
        # refined_i = i**D % N <- WRONG! so slow
        refined_i = pow(i, D, N)
        refined_data.append(refined_i)
    
    print(f"[DEBUG_2] {refined_data}")
    result = int2string(refined_data)
    
    return result


if __name__ == "__main__":
    main()
