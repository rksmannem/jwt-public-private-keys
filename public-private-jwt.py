import jwt
import os


def create_jwt(payload, priKeyFileName):
    print('PRIVATE_KEY_FILE:',priKeyFileName)
    private_key=open(priKeyFileName).read()
    token = jwt.encode(payload, private_key, algorithm='RS256').decode('utf-8')
    return token

def validate_jwt(token, pubKeyFileName):
    print('PUBLIC_KEY_FILE:',pubKeyFileName)
    pub_key = open(pubKeyFileName).read()
    payload = jwt.decode(token, pub_key, algorithms=['RS256'])
    return payload

def main():
    payload={
        'username':'rama',
        'user_id': 111,
        'email': 'rksmannem@gmail.com',
        'iss':'IEEE'
    }

    print("============(generate jwt by signing using private key)===================\n")
    privateKeyFile=os.getenv("PRIVATE_KEY_FILE",  "DUMMY")
    token=create_jwt(payload, privateKeyFile)
    print("token: ", token)

    print("============(validate jwt using public key)===================\n")
    pubKeyFile=os.getenv("PUBLIC_KEY_FILE", "PUB-KEY-FILE")
    data=validate_jwt(token, pubKeyFile)
    print("payload after validating jwt: ", data)


if __name__ == "__main__":
    main()

