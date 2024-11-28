import socket
import struct

# The decipher function applies the Stream cipher decryption algorithm to decrypt the data.
def decipher(k, d):
    S = list(range(256))
    j = 0
    o = []
    for i in range(256):
        j = (j + S[i] + k[i % len(k)]) % 256
        S[i], S[j] = S[j], S[i]
    i = j = 0
    # Pseudo-random generation algorithm (PRGA) to generate the keystream and decrypt the data.
    for c in d:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        o.append(c ^ S[(S[i] + S[j]) % 256])  # XOR the data with the keystream.
    return bytearray(o)  # Return the decrypted data as a bytearray.

# The ip2d function converts a list of IP addresses to a bytearray.
def ip2d(ipa):
    d = bytearray()
    for ip in ipa:
        pd = socket.inet_aton(ip)
        d.extend(pd)
    return d

# The decr function decrypts a list of ciphered IP addresses using the provided key.
def decr(ipa, k):
    d = ip2d(ipa)  # Convert the IP addresses to a bytearray.
    padding_length = d[-1]  # Retrieve the padding length from the last byte.
    ed = decipher(k, d[:-padding_length])  # Decrypt the data excluding the padding.
    return ed.decode('utf-8')  # Decode the decrypted data to a string.


def main():
    key = bytearray('supersecretkey', 'utf-8')
    # List of ciphered IP addresses can change.
    ciphered_ips = ['159.96.34.204', '136.182.188.58', '155.20.31.30', '12.234.113.15', '153.170.118.69', '189.152.240.17', '180.27.111.161', '87.205.101.118', '45.1.136.2', '122.3.3.3']
    plaintext = decr(ciphered_ips, key)
    print("Decoded Plaintext:", plaintext)

if __name__ == "__main__":
    main()
