from PIL import Image

def encrypt_image(input_image_path, output_image_path, key):
    image = Image.open(input_image_path)
    pixels = image.load()

    width, height = image.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

    image.save(output_image_path)
    print("Image encrypted and saved as", output_image_path)

def decrypt_image(input_image_path, output_image_path, key):
    encrypt_image(input_image_path, output_image_path, -key)

# Example usage
key = 50  
input_image = "sample.png"   
encrypted_image = "encrypted_image.png"
decrypted_image = "decrypted_image.png"

encrypt_image(input_image, encrypted_image, key)
decrypt_image(encrypted_image, decrypted_image, key)
                  
