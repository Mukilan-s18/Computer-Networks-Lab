import random

def calc_redundant_bits(m):
    for i in range(m):
        if (2**i >= m + i + 1):
            return i

def pos_redundant_bits(data, r):
    j = 0
    k = 1
    m = len(data)
    res = ''
    for i in range(1, m + r + 1):
        if i == 2**j:
            res += '0'
            j += 1
        else:
            res += data[-1 * k]
            k += 1
    return res[::-1]

def calc_parity_bits(arr, r):
    n = len(arr)
    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if j & (2**i) == (2**i):
                val ^= int(arr[-1 * j])
        arr = arr[:n - (2**i)] + str(val) + arr[n - (2**i) + 1:]
    return arr

def detect_error(arr, nr):
    n = len(arr)
    res = 0
    for i in range(nr):
        val = 0
        for j in range(1, n + 1):
            if j & (2**i) == (2**i):
                val ^= int(arr[-1 * j])
        res += val * (10**i)
    return int(str(res), 2)

with open("input_data.txt", "r") as f:
    text = f.read()

binary_data = ''.join(format(ord(i), '08b') for i in text)
m = len(binary_data)
r = calc_redundant_bits(m)
arr = pos_redundant_bits(binary_data, r)
encoded = calc_parity_bits(arr, r)

error_pos = random.randint(0, len(encoded)-1)
encoded_err = list(encoded)
encoded_err[error_pos] = '1' if encoded_err[error_pos] == '0' else '0'
encoded_err = "".join(encoded_err)

with open("channel.txt", "w") as f:
    f.write(encoded_err)

with open("output.txt", "w") as f:
    f.write(f"Original Text: {text}\n")
    f.write(f"Binary Data: {binary_data}\n")
    f.write(f"Encoded Data (Hamming): {encoded}\n")
    f.write(f"Data sent to channel (with error at index {error_pos}): {encoded_err}\n")
    
    received = encoded_err
    error_loc = detect_error(received, r)
    if error_loc != 0:
        f.write(f"Error detected at position: {error_loc} (from right)\n")
        corrected = list(received)
        idx = len(received) - error_loc
        corrected[idx] = '1' if corrected[idx] == '0' else '0'
        corrected = "".join(corrected)
        f.write(f"Corrected Data: {corrected}\n")
    else:
        f.write("No error detected.\n")
