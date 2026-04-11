import glob
import os

desc = '<meta name="description" content="South Cafe sets the standard for premium dining, specializing in authentic shawarma, luxury parfaits, and refreshing fruit drinks. Experience the best of Calabar and Uyo with our world-class delivery and modern dining ecosystem.">'

os.chdir(r'c:\Users\USER\Desktop\anti-gravity')
files = glob.glob('*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<meta name="description"' not in content:
        content = content.replace('<title>', desc + '\n    <title>')
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
