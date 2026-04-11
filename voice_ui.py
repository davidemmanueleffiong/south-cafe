import glob
import os

btn_replace = '<button class="ai-mic" onclick="startVoiceAI()" style="background:transparent; border:none; font-size:1.5rem; cursor:pointer;" title="Hold to Speak">🎤</button>\n                <button class="ai-send" onclick="sendAIMessage()">➤</button>'

os.chdir(r'c:\Users\USER\Desktop\anti-gravity')
files = glob.glob('*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'ai-mic' not in content:
        content = content.replace('<button class="ai-send" onclick="sendAIMessage()">➤</button>', btn_replace)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
