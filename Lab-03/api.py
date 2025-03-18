from flask import Flask, jsonify, request
from cipher.rsa import RSACipher
import rsa
app = Flask(__name__)

rsa_cipher = RSACipher()

@app.route('/api/rsa/generate_keys', methods=['GET'])
def rsa_generate_keys():
    rsa_cipher.generate_keys()
    return jsonify({'message': 'Keys generated successfully'})

@app.route('/api/rsa/encrypt', methods=['POST'])
def rsa_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    private_key, public_key = rsa_cipher.load_keys()
    if key == 'public':
        key = public_key
    elif key == 'private':
        key = private_key
    else:
        return jsonify({'message': 'Invalid key type'})
    encrypted_text = rsa_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text.hex()})

@app.route('/api/rsa/decrypt', methods=['POST'])
def rsa_decrypt():
    data = request.json
    cipher_text = data['ciphertext']
    key = data['key']
    private_key, public_key = rsa_cipher.load_keys()
    if key == 'public':
        key = public_key
    elif key == 'private':
        key = private_key
    else:
        return jsonify({'message': 'Invalid key type'})
    ciphertext = bytes.fromhex(cipher_text)
    decrypted_text = rsa_cipher.decrypt(ciphertext, key)
    return jsonify({'decrypted_message': decrypted_text})

@app.route('/api/rsa/sign', methods=['POST'])
def rsa_sign():
    data = request.json
    message = data['message']
    private_key, _ = rsa_cipher.load_keys()
    signature = rsa_cipher.sign(message, private_key)
    return jsonify({'signature': signature.hex()})

@app.route('/api/rsa/verify', methods=['POST'])
def rsa_verify():
    data = request.json
    message = data['message']
    signature_hex = data['signature']
    public_key, _ = rsa_cipher.load_keys()
    signature = bytes.fromhex(signature_hex)
    verified = rsa_cipher.verify(message, signature, public_key)
    return jsonify({'verified': verified})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)