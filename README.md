# meme-indexer
A tool that uses OCR to catalogue and help you find that one meme you really really need right now, in your vast swathes of folders.

# install instructions
- made on python 3.10. install requirements with `python -m pip install -r requirements.txt` (can be done with a `venv`)
- install tesseract from [here](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.2.0.20220712.exe)
(more info: [tesseract git hub page](https://github.com/UB-Mannheim/tesseract/wiki))
- place all the files from inside the `C:\Program Files\Tesseract-OCR` folder into the `tesseract-ocr` folder in the meme-indexer folder here.
- place all your memes in the 'memes' folder `(custom paths planned for future)`
- run `python search_memes.py` !
## Todo:
- [x] Get OCR words from an image
- [x] Dictionary of file path+name to text tags inside image 
- [x] Implement search, select from top selected (0,1,2,...) and it will open windows explorer at that file path 