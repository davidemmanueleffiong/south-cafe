import glob
import os

js = open('js/app.js', 'r', encoding='utf-8').read()

new_voice = '''// WhatsApp Style AI Voice Logic
let aiRecording = false;
let aiRecordTimer;
let aiRecordSeconds = 0;
let aiRecognition;

window.toggleVoiceAI = function() {
    const input = document.getElementById('ai-message-input');
    const micBtn = document.querySelector('.ai-mic');
    
    if(!aiRecording) {
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        if(!SpeechRecognition) return showToast("Voice AI not supported.", "error"); // Ignore if not supported
        
        aiRecognition = new SpeechRecognition();
        aiRecognition.lang = 'en-US';
        aiRecognition.interimResults = true;
        
        aiRecording = true;
        aiRecordSeconds = 0;
        micBtn.innerHTML = "🛑";
        micBtn.style.color = "#ff4444";
        input.readOnly = true;
        input.value = "Recording... 00:00";
        input.style.color = "#ff4444";
        
        aiRecordTimer = setInterval(() => {
            aiRecordSeconds++;
            const mins = Math.floor(aiRecordSeconds / 60).toString().padStart(2, '0');
            const secs = (aiRecordSeconds % 60).toString().padStart(2, '0');
            input.value = `Recording... ${mins}:${secs}`;
        }, 1000);
        
        let finalTranscript = "";
        aiRecognition.onresult = function(event) {
            finalTranscript = Array.from(event.results).map(res => res[0].transcript).join('');
        };
        
        aiRecognition.onend = function() {
            if(aiRecording) { // Ended naturally due to silence pausing
                stopVoiceAI(finalTranscript);
            }
        };
        
        aiRecognition.start();
    } else {
        // Manually Stop
        aiRecognition.stop(); 
        // Note: calling stop triggers onend, but we can actively clean it up here to be safe
    }
}

function stopVoiceAI(transcript) {
    aiRecording = false;
    clearInterval(aiRecordTimer);
    const micBtn = document.querySelector('.ai-mic');
    const input = document.getElementById('ai-message-input');
    
    micBtn.innerHTML = "🎤";
    micBtn.style.color = "inherit";
    input.readOnly = false;
    input.style.color = "inherit";
    
    if(transcript) {
        input.value = transcript;
        input.placeholder = "Type here... (Ready to send)";
    } else {
        input.value = "";
        input.placeholder = "Failed to transcribe. Type here...";
    }
}
'''

start = js.find('window.startVoiceAI = function()')
end = js.find('window.runAIProfiler = function()')
if start != -1 and end != -1:
    js = js[:start] + new_voice + '\n' + js[end:]
    open('js/app.js', 'w', encoding='utf-8').write(js)

# Inject WhatsApp click handlers into HTML files (replace startVoiceAI with toggleVoiceAI)
files = glob.glob('*.html')
for file in files:
    content = open(file, 'r', encoding='utf-8').read()
    content = content.replace('startVoiceAI()', 'toggleVoiceAI()')
    x = '<body'
    if 'data-theme' not in content:
        content = content.replace('<body', '<body data-theme="light" ')
    open(file, 'w', encoding='utf-8').write(content)
