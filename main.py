import base64
import re

def decode_string(encoded: str) -> str:
    raw = base64.b64decode(encoded)
    state = 36883
    out = []
    i = 0

    while i < len(raw):
        state = ((state << 8) | (state >> 8)) & 0xFFFF
        code = raw[i] ^ (state >> 8)
        i += 1

        if code == 0xFF:
            state = ((state << 8) | (state >> 8)) & 0xFFFF
            low = raw[i] ^ (state >> 8)
            i += 1
            state = ((state << 8) | (state >> 8)) & 0xFFFF
            high = raw[i] ^ (state >> 8)
            i += 1
            code = low | (high << 8)

        out.append(chr(code))

    return "".join(out)

print("aB:", decode_string("PPN3/j7zdPk883vxf/x2/nT1PuB/8Wf2fOJ+v3u/"))
print("aC:", decode_string("PPpg9Dz/ffVg+HzkPPYr9HWkd6RyoHD0Jb8jviGgJqYnpCakIqAjoyOjIqgkqiKnKqUioySmIqgp83vyXPMq1V/kfNNM2FqhfMYh2T7+XNkqxn3FUqIqx3j/cKR1o1TSV9ND+zw="))
