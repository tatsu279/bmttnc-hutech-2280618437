import sys
from PIL import Image

def decode_image(image_path):
    img = Image.open(image_path)
    width, height = img.size
    binary_message = ""
    
    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            for color_channel in range(3):
                binary_message += str(pixel[color_channel] & 1)
                
    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        if byte == '11111111':  # End of message marker
            break
        message += chr(int(byte, 2))
        
    return message

def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <image_path>")
        sys.exit(1)
    
    image_path = sys.argv[1]
    message = decode_image(image_path)
    
    print("Decoded message:", message)
    
if __name__ == "__main__":
    main()
    