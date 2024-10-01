# Passwords should never be stored in plain text. 
# Hash is a one-way function to obscure plain text
# Minimum, passwords should be stored in hash, if not more complex

# Library: bcrypt
# ----------------------- Install bycrypt
# $ pip3 install --upgrade pip -U
# $ pip install bcrypt
# -----------------------
import bcrypt

# --------------------------------------------------------------
# What is salt?
# Allows random bits to camouflage your hash even more
pw = "Password123"
# bcrypt only works with bytes (encoded strings, not plain string)
hashed = bcrypt.hashpw(pw.encode(), bcrypt.gensalt()) # results in bytes, must decode to see it in string format

# print(hashed.decode())

given = input('Please enter a password ')
if bcrypt.checkpw(given.encode(), hashed):
    print('Access Granted')
else:
    print('Axess DENIED')

