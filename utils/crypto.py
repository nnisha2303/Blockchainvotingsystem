from cryptography.hazmat.primitives.asymmetric import rsa, padding 
from cryptography.hazmat.primitives import hashes, serialization 
 
# Generate RSA key pair 
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048) 
public_key = private_key.public_key() 
 
def sign_vote(vote_data): 
    """Sign the vote using the private key.""" 
    signature = private_key.sign( 
        vote_data.encode(), 
        padding.PSS( 
            mgf=padding.MGF1(hashes.SHA256()), 
            salt_length=padding.PSS.MAX_LENGTH 
        ), 
        hashes.SHA256() 
    ) 
    return signature.hex() 

from cryptography.hazmat.primitives.asymmetric import rsa, padding 
from cryptography.hazmat.primitives import hashes, serialization 
 
# Generate RSA key pair 
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048) 
public_key = private_key.public_key() 
 
def sign_vote(vote_data): 
    """Sign the vote using the private key.""" 
    signature = private_key.sign( 
        vote_data.encode(), 
        padding.PSS( 
            mgf=padding.MGF1(hashes.SHA256()), 
            salt_length=padding.PSS.MAX_LENGTH 
        ), 
        hashes.SHA256() 
    ) 
    return signature.hex() 
 
def verify_vote(vote_data, signature): 
    """Verify the vote signature using the public key.""" 
    try: 
        public_key.verify( 
            bytes.fromhex(signature), 
            vote_data.encode(), 
            padding.PSS( 
                mgf=padding.MGF1(hashes.SHA256()), 
                salt_length=padding.PSS.MAX_LENGTH 
            ), 
            hashes.SHA256() 
        ) 
        return True 
    except Exception: 
        return False 
 
def get_public_key_pem(): 
    """Export the public key in PEM format.""" 
    pem = public_key.public_bytes( 
        encoding=serialization.Encoding.PEM, 
        format=serialization.PublicFormat.SubjectPublicKeyInfo 
    ) 
    return pem.decode()
