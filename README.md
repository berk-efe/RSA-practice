# RSA-Encryption

#### url
#### This code is a simple implementation of RSA encryption method in python. I am quite interested in math and encryption, so I decided to implement this code.

### Resources
I have used the following resources to understand the RSA encryption method:
https://www.geeksforgeeks.org/rsa-algorithm-cryptography/
https://www.youtube.com/watch?v=AQDCe585Lnc

These two are must watch, they are made by eddie woo and they are everything you need!
https://www.youtube.com/watch?v=4zahvcJ9glg
https://www.youtube.com/watch?v=oOcTVTpUsPQ

### Special Thanks
Really special thanks to Eddie Woo.

## How to use
Of course he explains it in a much better way than I can, so I recommend you to watch his videos but i have to explain this program too.

### Math part

So i will start with the math behind the RSA encryption method.

> RSA encryption method is based on the fact that it is easy to multiply large prime numbers, but it is very difficult to factorize the product of two large prime numbers.

There are two types of keys in RSA.

Public key which encrypts the message.
Private key which decrypts the message.

And there is a very VERY specific way to generate these keys.

Let me explain the process of generating the keys in 4 simple steps:

1. Choose two prime numbers p and q.
2. Get product of p and q, N = p*q.
3. Get their phi value, which means the count of coprime numbers of N. There is this simple formula to get phi value of N: phi(N) = (p-1)*(q-1).
4. Now we will choose a number which we will call "E" this number will be in our public key to encrypt. This number should be coprime with N and phi(N). This number should be greater than 1 and less than phi(N).
5. Now we will find the number "D" which will be in our private key to decrypt. This number should satisfy the following equation: (E*D) % phi(N) = 1.

Public key = (E, N)
Private key = (D, N)

So this is basicly what RSA is!

When we use this function x^E % N to encrypt the message, we will use x^D % N to decrypt the message. (X is our message)

### Code part

So our code is quite simple. First we generate keys (The LIMIT constant is for the range of prime numbers we will choose from)

Inside the generate_keys function we choose two prime numbers, p and q. Then we calculate N and phi(N). Then we choose E and find D.

Then we have two functions, encrypt and decrypt. Encrypt function takes the message and public key as input and returns the encrypted message. Decrypt function takes the encrypted message and private key as input and returns the decrypted message.

Additionally we have supporting functions to check if a number is prime and to get the greatest common divisor of two numbers. They are fairly simple functions.

Each function has their documantation inside the code. Feel free to read them. (You better read them :D)

### Some problems/bugs

There have been 2 problems i have encountered.

You see, in my code i switch chars with their ascii values. When i pick a Modular (N) value that is too small, the mod of the ascii value of the char will be greater than the ascii value of the char. So you better pick a big N value.

Second problem is, do you remember the `i^E % N` function? Well when you just enter this function as it is it will take so much time to compute. So there is a better way. `pow()` function which comes built-in with python. It is much faster than the `i^E % N` function. So i recommend you to use `pow()` function. Same goes for decryption too.



