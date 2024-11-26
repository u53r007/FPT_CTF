def generate_license_key():
    # The two hardcoded arrays from the C code
    v7 = [168, 193, 122, 172, 158, 108, 206, 153, 175, 175, 194, 189, 141, 127, 101, 202,
          208, 116, 149, 160, 146, 179, 114, 143, 187, 159, 126, 109, 174, 156, 185, 120,
          164, 189, 112, 120, 123, 145]
    v8 = [53, 87, 22, 73, 48, 1, 91, 53, 58, 62, 89, 74, 35, 28, 1, 92,
          99, 17, 41, 45, 29, 79, 10, 44, 68, 58, 11, 12, 72, 38, 83, 2,
          67, 74, 12, 5, 23, 45]

    # Calculate the middle part of the license key
    middle_part = ''.join(chr(v7[i] - v8[i]) for i in range(38))

    # Add the "FUSec{" prefix and "}" suffix
    license_key = "FUSec{" + middle_part + "}"
    
    return license_key

if __name__ == "__main__":
    generated_key = generate_license_key()
    print(f"Generated License Key: {generated_key}")
