def py_challenge_1(encoded_string, shift_right=2):
    z_code = 122
    a_before_code = 96
    decoded_list = []
    for symbol in encoded_string:
        if symbol.isalpha():
            shifted_code = ord(symbol) + shift_right
            if z_code - shifted_code >= 0:
                new_symbol = chr(shifted_code)
            else:
                new_symbol = chr(a_before_code + shifted_code - z_code)
        else:
            new_symbol = symbol
        decoded_list.append(new_symbol)

    return "".join(decoded_list)
