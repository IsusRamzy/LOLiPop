import pickle
import pathlib
import base64

print('Welcome to LOLiPop')

meme = []
while True:
    action = input('Type (save exit add remove): ').lower().replace(' ', '')
    
    if action == 'save':
        file_path = input('Meme path (without extension): ')+'.lol'
        with open(file_path, 'wb') as f:
            pickle.dump(meme, f)
    elif action == 'exit':
        print('PROGRAM TERMINATED')
        exit()
    elif action == 'add':
        element_type = input('Type (txt img): ').lower().replace(' ', '')
        if element_type == 'txt':
            txt = input('Text (Press Enter to exit): ')
            if txt == '':
                continue
            meme.append({'type': 'txt', 'data': txt})
            print('TEXT ELEMENT ADDED')
        elif element_type == 'img':
            img_path = input('Path to image: ')
            img = pathlib.Path(img_path).read_bytes()
            img =  base64.b64encode(img).decode("utf-8")
            img_format = ''
            format_included = False
            for char in img_path:
                if format_included:
                    img_format += char
                if char == '.':
                    format_included = True
            base64_link = f"data:image/{img_format};base64,{img}"
            meme.append({'type': 'img', 'data': base64_link})
    elif action == 'remove':
        index = int(input('Index to element (index starts with 1): '))+1
        meme.pop(index)