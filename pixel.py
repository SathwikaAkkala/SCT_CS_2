from PIL import Image
import random

class ImageEncryptor:
    def __init__(self, image_path):
        self.image = Image.open(image_path)
        self.pixels = self.image.load()

    def swap_pixels(self, coord1, coord2):
        """
        Swap the pixel values at coord1 and coord2.
        coord1 and coord2 should be tuples of (x, y) coordinates.
        """
        temp = self.pixels[coord1]
        self.pixels[coord1] = self.pixels[coord2]
        self.pixels[coord2] = temp

    def apply_math_operation(self, value):
        """
        Add a constant value to each pixel's RGB values.
        The value should be an integer.
        """
        for x in range(self.image.width):
            for y in range(self.image.height):
                r, g, b = self.pixels[x, y]
                self.pixels[x, y] = ((r + value) % 256, (g + value) % 256, (b + value) % 256)

    def save_image(self, output_path):
        """
        Save the modified image to the specified path.
        """
        self.image.save(output_path)

# Example usage:
if __name__ == "__main__":
    encryptor = ImageEncryptor("input_image.png")
    
    # Swap two random pixels
    width, height = encryptor.image.size
    coord1 = (random.randint(0, width - 1), random.randint(0, height - 1))
    coord2 = (random.randint(0, width - 1), random.randint(0, height - 1))
    encryptor.swap_pixels(coord1, coord2)

    # Apply a mathematical operation to all pixels
    encryptor.apply_math_operation(50)

    # Save the encrypted image
    encryptor.save_image("encrypted_image.png")
