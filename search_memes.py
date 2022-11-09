import os
import json
import re
import subprocess
FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')

index_path = "data_index.json"
# check if index dict exists
if not os.path.exists(index_path):
    print("Index does not exist. Creating now...")
    # run index python ehre
    import index_memes
    index_memes.main()


# get search input
print("(note, only first word in search string will be searched)")
text_search = input("enter your meme search text here: ")
search_args = text_search.split()
print(search_args)

# import index file
with open('data_index.json', 'r') as infile:
    img_text_dict = json.load(infile)

    print(f"imported {len(img_text_dict)} memes.")

    search_term = search_args[0]

    opt_count = 0
    opt_arr = []

    for meme_path,meme_text in img_text_dict.items():
        if meme_text.find(search_term) != -1:
            print(f"[{opt_count}] FOUND '{search_term}' in {meme_path}")
            opt_arr.append(meme_path)
            opt_count += 1

    inp_max = len(opt_arr) - 1
    inp_range = f"0 to {inp_max}"
    

    while True:
        inp = input(f"To open image, enter a number from {inp_range}. type 'q' to exit: ").lower()

        # quit on 'q'
        if inp == 'q': break

        # extract nums from inp text
        nums_extracted = re.findall(r'\d+', inp)
        if len(nums_extracted) <= 0:
            print("no number entered. try again.")
            continue
        
        # get first num
        num = int(nums_extracted[0])
        if num < 0:
            print(f"entered number to small. enter from range {inp_range}")
            continue
        elif num > inp_max:
            print(f"entered number to large. enter from range {inp_range}")
            continue
        
        chosen_path = opt_arr[num]
        print(f"opening meme [{num}]: {chosen_path}")

        # open windows explorer at location
        path = os.path.normpath(chosen_path)
        if os.path.isdir(path):
            subprocess.run([FILEBROWSER_PATH, path])
        elif os.path.isfile(path):
            subprocess.run([FILEBROWSER_PATH, '/select,', os.path.normpath(path)])


        

