import webbrowser
import pickle

print('Welcome to LOLiPop')

path = input('Meme path (Without the LOL): ')

with open(path+'.lol', 'rb') as f:
    meme = pickle.load(f)

html = """<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LOLiPop</title>
    <style>
        body {
            font-family: Arial, Helvetica, sans-serif;
            text-align: center;
        }
    </style>
</head>
<body>
"""

for element in meme:
    if element['type'] == 'txt':
        html += f'<p>{element["data"]}</p>\n'
    elif element['type'] == 'img':
        html += f'''<img src="{element["data"]}">\n'''
    else:
        print(f'ELEMENT OF TYPE ({element["type"]}) IS NOT SUPPORTED')

with open(path+'.renderedhtml.html', 'w') as f:
    f.write(html)
html += '</body>'
webbrowser.open(path+'.renderedhtml.html')