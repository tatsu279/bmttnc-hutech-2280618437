import hashlib

def blake2(message):
    blake2_hash = hashlib.blake2b(digest_size=64)
    blake2_hash.update(message)
    return blake2_hash.digest()

def main():
    text = input("Enter text to hash: ").encode("utf-8")
    hashed_text = blake2(text)
    
    print(f"BLAKE2 hash of '{text.decode("utf-8")}' is: {hashed_text}")
    
if __name__ == "__main__":
    main()