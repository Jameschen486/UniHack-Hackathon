import jwt
import re
from datetime import datetime
import hashlib

#
# TOKEN RELATED FUNCTIONS
#
SECRET = 'OKCKFCUFCLAKERSIN5'
# Given a user id and session count, generate a session token for the user
def generate_token(u_id, session_count):
    # add session to session tracker
    payload = {
        'u_id': u_id,
        'iat': datetime.utcnow(),
        'session_id':session_count
    }
    # encode token using jwt 
    token = jwt.encode(payload, SECRET, algorithm='HS256')
    return token

def fetch_u_id(token):
    return jwt.decode(token, SECRET, algorithms=['HS256'])['u_id']

#
# AUTH RELATED FUNCTIONS
#

def generate_new_id():
    conn, cursor = make_connection()
    cursor.execute(f"""
    select count(*) from Users  
    """)
    new_id = cursor.fetchone()[0] + 1
    end_connection(conn, cursor)
    return new_id
    
# Checking if user_details is valid given email is in use
def is_valid_user(email, password_hash):
    valid = False
    conn, cursor = make_connection()
    cursor.execute(f"""
    select * from Users where email = %s and password_hash = %s
    """, (email, password_hash))
    if cursor.fetchone() is not None:
        valid = True
    end_connection(conn, cursor)
    return valid

def is_valid_user_id(u_id):
    valid = False
    conn, cursor = make_connection()
    cursor.execute(f"""
    select * from Users where id = %s
    """, (u_id,))
    if cursor.fetchone() is not None:
        valid = True
    end_connection(conn, cursor)
    return valid