import os
import argparse
from PIL import Image
from src.image_processing import enhance_image
from src.ocr_processing import correct_ocr_errors, process_text_to_df

def process_image_to_df(image_path, output_dir):
    image = Image.open(image_path)
    enhanced_image = enhance_image(image)
    resized_image = enhanced_image.resize((enhanced_image.width * 2, enhanced_image.height * 2))
    custom_config = r'--oem 3 --psm 6'
    languages_ = "eng+tha"
    extracted_text = pytesseract.image_to_string(resized_image, config=custom_config, lang=languages_)
    extracted_text = correct_ocr_errors(extracted_text)
    df = process_text_to_df(extracted_text)
    output_path = os.path.join(output_dir, f'{os.path.basename(image_path).split(".")[0]}.csv')
    df.to_csv(output_path, index=False)
    print(f'Saved {output_path}')

def main():
    parser = argparse.ArgumentParser(description="Process images to extract text using OCR and save as CSV.")
    parser.add_argument('images_dir', type=str, help='Directory containing the images to process')
    parser.add_argument('output_dir', type=str, help='Directory to save the processed CSV files')

    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    for filename in os.listdir(args.images_dir):
        if filename.endswith('.png') or filename.endswith('.jpeg'):
            image_path = os.path.join(args.images_dir, filename)
            process_image_to_df(image_path, args.output_dir)

if __name__ == "__main__":
    main()
