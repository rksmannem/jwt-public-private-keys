import jwt
import os


#secret_key = "a random, long, sequence of characters that only the server knows"

def create_jwt(payload, alg):
    secret_key = os.getenv("SECRET_KEY", "DEFAULT")
    token = jwt.encode(payload, secret_key, algorithm=alg).decode('utf-8')
    #print("token= ", token)
    return token


def validate_jwt(token, algs):
    secret_key = os.getenv("SECRET_KEY", "DUMMY")
    payload = jwt.decode(token, secret_key, algorithms=algs)
    #print("payload: ", payload)
    return payload


def main():
    payload={
        "user_id": 123,
        "username": 'rama',
        "roles":  ['developer', 'engineer']
    }

    token=create_jwt(payload, 'HS256')
    print("jwt-token: ", token)

    data=validate_jwt(token, ['HS256'])
    print("payload: ", data)

if __name__ == "__main__":
    main()
