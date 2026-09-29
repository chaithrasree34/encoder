# encoder
import base64

text = input("Enter text to encode: ")

encoded_text = base64.b64encode(text.encode("utf-8")).decode("utf-8")

print("Encoded text:", encoded_text)
