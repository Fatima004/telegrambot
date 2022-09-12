from decouple import config

password = config("PASSWORD", default="fghds324")
pin = config("PIN", cast=int)

print(password)
print(pin, type(pin))