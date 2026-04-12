import glob
import os

os.chdir(r'c:\Users\USER\Desktop\anti-gravity')
for file in glob.glob('*.html'):
    content = open(file, 'r', encoding='utf-8').read()
    
    # Strip any hardcoded body themes
    content = content.replace('<body data-theme="light" >', '<body>')
    content = content.replace('<body data-theme="light">', '<body>')
    content = content.replace('<body data-theme="dark">', '<body>')
    
    open(file, 'w', encoding='utf-8').write(content)
