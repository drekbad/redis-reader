#!/usr/bin/env python3

import re

with open('file.txt', 'r') as file:
    data = file.read()

def decode_hex(encoded_text):
    return re.sub(r"\\x([0-9a-fA-F]{2})", lambda m: chr(int(m.group(1), 16)), encoded_text)

def format_text(decoded_text):
    lines = re.split(r'[\x0d\x0a]+', decoded_text)
    formatted_lines = []

    for line in lines:
        line = line.strip()
        if line:
            if ':' in line:
                formatted_lines.append(f" {line}")
            else:
                formatted_lines.append(line)
    return "\n".join(formatted_lines)

decoded = decode_hex(data)
formatted_output = format_text(decoded)

with open('cleaned.txt', 'w') as file:
    file.write(formatted_output)

print("Cleaned output saved to cleaned.txt")

