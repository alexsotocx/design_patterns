from builders.morse_code_builder import MorseCodeBuilder
from builders.bit_builder import BitBuilder


def build(builder, text):
    for char in text:
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
            builder.transform_letter(char)
        elif ('0' <= char <= '9'):
            builder.transform_number(char)
        else:
            builder.transform_symbol(char)
    return builder.result()


print(build(MorseCodeBuilder(), "The quick brown fox jumps over the lazy dog"))
print(build(MorseCodeBuilder(), "12345!ABC"))
print("----------------------")
print(build(BitBuilder(), "The quick brown fox jumps over the lazy dog"))
print(build(BitBuilder(), "12345!ABC"))
