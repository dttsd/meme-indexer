# meme-indexer
A tool that uses OCR to catalogue and help you find that one meme you really really need right now, in your vast swathes of folders.

# install instructions
- made on python 3.10. install requirements with `python -m pip install -r requirements.txt` (can be done with a `venv`)
- install tesseract from [here](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.2.0.20220712.exe)
(more info: [tesseract git hub page](https://github.com/UB-Mannheim/tesseract/wiki))
- place all the files from inside the `C:\Program Files\Tesseract-OCR` folder into the `tesseract-ocr` folder in the meme-indexer folder here.
![image](https://user-images.githubusercontent.com/99981273/200841337-3609d9f1-a38c-4e00-9e04-a9646bd8fa0f.png)
- place all your memes in the 'memes' folder, and/or add your main meme folder path to `config.txt`
- run `python search_memes.py` !

Whenever you add more memes into folder, remember to run `python index_memes.py`
## Todo:
- [x] Get OCR words from an image
- [x] Dictionary of file path+name to text tags inside image 
- [x] Implement search, select from top selected (0,1,2,...) and it will open windows explorer at that file path
- [ ] Multiprocess / async the OCR step for multiple files
- [ ] Smarter index updating, based on file name updates (to prevent redoing OCR on an entire library)
