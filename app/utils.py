import cv2
import pytesseract
import os

def process_receipt(image_path):
    
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"The file {image_path} does not exist.")

    # Load the image
    image = cv2.imread(image_path)

    # Convert to grayscale for better OCR results
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Perform OCR on the grayscale image
    extracted_text = pytesseract.image_to_string(gray)

    return extracted_text
