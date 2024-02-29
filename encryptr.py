def cryptographicHasher(input_file_location, total_shift_count, total_seed_count, mode):
    INPUT_FILE = input_file_location
    SHIFT_COUNT = total_shift_count
    SEED_COUNT = total_seed_count
    OUTPUT_STRING = ""

    with open(INPUT_FILE, "r") as f:
        INPUT_FILE = f.read()

    for l in INPUT_FILE:
        if l.isalpha():
            if mode == 0:
                a = ord(l)
                i = 0

                while i < total_seed_count:
                    a = a + SHIFT_COUNT
                    i += 1

                OUTPUT_STRING += chr(a)
            elif mode == 1:
                a = ord(l)
                i = 0

                while i < total_seed_count:
                    a = a - SHIFT_COUNT
                    i += 1

                OUTPUT_STRING += chr(a)
            else:
                pass
        else:
            OUTPUT_STRING += l

    with open(input_file_location, "w") as f:
        f.write(OUTPUT_STRING)
