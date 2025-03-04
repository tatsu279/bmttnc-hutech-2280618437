from flask import Flask, request, jsonify
from cipher.ceasar import CaesarCipher
app = Flask(__name__)
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayfairCipher
from cipher.transposition import TranpositionCipher


#CEASAR
caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt(plain_text, key)
    return jsonify({"encrypted_text": encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt(cipher_text, key)
    return jsonify({"decrypted_text": decrypted_text})

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)

#VIGENERE
vigenere_cipher = VigenereCipher()

@app.route('/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.get_json()
    plaintext = data['plaintext']
    key = data['key']
    encrypted_text = vigenere_cipher.encrypt(plaintext, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.get_json()
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

#RAILFENCE
railfence_cipher = RailFenceCipher()

@app.route('/railfence/encrypt', methods=['POST'])
def encrypt():
    data = request.get_json()
    plaintext = data['plaintext']
    key = int(data['key'])
    encrypted_text = railfence_cipher.rail_fence_encrypt(plaintext, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/railfence/decrypt', methods=['POST'])
def decrypt():
    data = request.get_json()
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

#PLAYFAIR
playfair_cipher = PlayfairCipher()

@app.route('/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.get_json()
    plaintext = data['plaintext']
    key = data['key']
    matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(plaintext, matrix)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.get_json()
    cipher_text = data['cipher_text']
    key = data['key']
    matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, matrix)
    return jsonify({'decrypted_text': decrypted_text})

#TRANSPOSITION
transposition_cipher = TranpositionCipher()

@app.route('/transposition/encrypt', methods=['POST'])
def tranposition_encrypt():
    data = request.get_json()
    plaintext = data['plaintext']
    key = int(data['key'])
    encrypted_text = transposition_cipher.encrypt(plaintext, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/transposition/decrypt', methods=['POST'])
def tranposition_decrypt():
    data = request.get_json()
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = transposition_cipher.decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})
