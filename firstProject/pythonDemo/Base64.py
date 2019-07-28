import base64
# Base64
result = base64.b64encode(b'binary\x00string')
print(result)