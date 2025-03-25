from Crypto.Hash import SHA3_256

def sha3(message):
    sha3_hash = SHA3_256.new()
    sha3_hash.update(message)
    return sha3_hash.hexdigest()

def main():
    text = input("Enter text to hash: ").encode("utf-8")
    hashed_text = sha3(text)
    
    print(f"SHA-3 hash of '{text.decode("utf-8")}' is: {hashed_text}")    
    
if __name__ == "__main__":
    main()