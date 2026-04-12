import re
import os

os.chdir(r'c:\Users\USER\Desktop\anti-gravity')

# 1. Fix app.js
js = open('js/app.js', 'r', encoding='utf-8').read()

new_auth = '''function updateAuthUI() {
    const loginBtn = document.getElementById('nav-login-btn');
    if(!loginBtn) return;
    
    if (currentUser) {
        const formattedBalance = new Intl.NumberFormat('en-NG', { style: 'currency', currency: 'NGN' }).format(walletBalance);
        loginBtn.innerHTML = `
            <a href="wallet.html" class="wallet-badge" style="text-decoration:none;">👛 ${formattedBalance}</a>
            <a href="settings.html" class="btn btn-outline" style="padding: 5px 15px; margin-left:10px; border-color:rgba(255,255,255,0.2); color:inherit; text-decoration:none;">⚙️ Settings</a>
        `;
    } else {
        loginBtn.innerHTML = `<a href="login.html" class="btn btn-outline" style="padding: 5px 15px;">Login</a>`;
    }
}
updateAuthUI();'''

start = js.find('function updateAuthUI()')
end = js.find('// --- CHECKOUT & PAYMENTS ---')
if start != -1 and end != -1:
    js = js[:start] + new_auth + '\n\n' + js[end:]
    open('js/app.js', 'w', encoding='utf-8').write(js)

# 2. Fix login.html mailbox simulator
login = open('login.html', 'r', encoding='utf-8').read()

new_reset = '''function sendResetLink() {
            const email = document.getElementById('forgot-email').value;
            if(!email) return alert("Please enter your email.");
            
            document.getElementById('forgot-modal').style.display = 'none';
            
            const inbox = document.createElement('div');
            inbox.style.cssText = "position:fixed; bottom:20px; right:20px; background:#fff; color:#111; padding:20px; border-radius:12px; box-shadow:0 10px 30px rgba(0,0,0,0.5); z-index:9999; max-width:300px; border-left:5px solid #25D366;";
            inbox.innerHTML = `
                <div style="font-weight:bold; font-size:0.9rem; color:#666; margin-bottom:5px;">📧 New Mail: ${email}</div>
                <div style="font-weight:bold; font-size:1.1rem; margin-bottom:10px;">Password Reset Request</div>
                <p style="font-size:0.9rem; color:#555; margin-bottom:15px;">Click the secure link below to reset your South Cafe password.</p>
                <button onclick="alert('Password securely reset to default! You may login normally.'); this.parentElement.remove()" style="background:#00a651; color:#fff; border:none; padding:8px 15px; border-radius:5px; cursor:pointer; width:100%;">🔗 Reset Password</button>
                <div style="position:absolute; top:10px; right:15px; cursor:pointer; color:#999;" onclick="this.parentElement.remove()">✕</div>
            `;
            document.body.appendChild(inbox);
        }'''

login = re.sub(r'function sendResetLink\(\) \{.*?(?=\<\/script\>)', new_reset + '\n    ', login, flags=re.DOTALL)
open('login.html', 'w', encoding='utf-8').write(login)
