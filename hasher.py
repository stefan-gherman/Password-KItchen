import bcrypt

def hash_pw(plain_text):
    hashed_bytes = bcrypt.hashpw(plain_text.encode('utf-8'), bcrypt.gensalt())
    return hashed_bytes.decode('utf-8')


def check_pw(plain_text, hashed_pw):
    hashed_pw_encoded = hashed_pw.encode('utf-8')
    return bcrypt.checkpw(plain_text.encode('utf-8'), hashed_pw_encoded)