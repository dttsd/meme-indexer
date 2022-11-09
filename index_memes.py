from PIL import Image
import pytesseract as tess
import os
import json
import re

tess.pytesseract.tesseract_cmd = r'./tesseract-ocr/tesseract.exe'
meme_path = r"./memes/"

def main():
    img_text_dict = {}

    # OCR from image
    print("collecting files and scanning text")
    for root, dirs, files in os.walk(meme_path):
        for file in files:
            # calc path
            newpath=os.path.join(root,file)
            print(newpath, end="")

            # get text from inside image
            tess_string = tess.image_to_string(newpath).replace('\n', '').strip()

            # replace so only alphanumeric and spaces
            clean_string = re.sub(r'[^a-zA-Z0-9]+', ' ', tess_string)

            # remove capitals
            clean_string = clean_string.lower()

            print(f" : {clean_string}")

            # add to dict
            img_text_dict[newpath] = clean_string

    # print("printing tessdict")
    # for key,val in img_text_dict.items():
    #     print(key,":",val)

    print("writing index to file")

    # write indexer to file
    with open('data_index.json', 'w') as outfile:
        json.dump(img_text_dict, outfile, indent=2)

    print(f"done scanning {len(img_text_dict)} memes.")

if __name__ == "__main__":
    main()