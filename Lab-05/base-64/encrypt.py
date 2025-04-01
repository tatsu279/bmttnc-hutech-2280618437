import base64

def main():
    # Get the string to be encoded from the user
    input_string = input("Enter the string to be encoded: ")
    
    encoded_bytes = base64.b64encode(input_string.encode('utf-8'))
    encoded_string = encoded_bytes.decode('utf-8')
    
    with open("data.txt", "w") as file:
        file.write(encoded_string)
        
    print(f"Encoded string: {encoded_string}")
    print("Encoded string has been written to data.txt")
    
if __name__ == "__main__":  
    main()