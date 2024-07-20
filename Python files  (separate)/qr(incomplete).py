import cv2
from pyzbar.pyzbar import decode

# Function to decode QR codes from an image
def decode_qr_code(image_path):
    # Read the image using OpenCV
    image = cv2.imread(image_path)
    # Decode the QR code using pyzbar
    decoded_objects = decode(image)
    
    for obj in decoded_objects:
        # Print the type of barcode and data
        print(f"Type: {obj.type}")
        print(f"Data: {obj.data.decode('utf-8')}\n")

        # Draw a rectangle around the QR code
        (x, y, w, h) = obj.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the image with the QR code highlighted
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
decode_qr_code('qr_code_image.png')
