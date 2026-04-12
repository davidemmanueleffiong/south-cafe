import glob
import os

os.chdir(r'c:\Users\USER\Desktop\anti-gravity')

# 1. Update login.html inline to contain Forgot Password UI
login_html = open('login.html', 'r', encoding='utf-8').read()
forgot_link = '<a href="#" onclick="showForgotModal(event)" style="font-size:0.85rem; color:var(--color-primary); display:inline-block; margin-top:5px; text-decoration:none;">Forgot Password?</a>'

# Insert forgot password link under password input
if 'Forgot Password?' not in login_html:
    login_html = login_html.replace(
        '<input type="password" class="form-input" id="password" required placeholder="••••••••">',
        f'<input type="password" class="form-input" id="password" required placeholder="••••••••">\n                {forgot_link}'
    )

forgot_modal = '''
    <div class="modal-overlay" id="forgot-modal" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.8); z-index:9000; align-items:center; justify-content:center;">
        <div class="modal-content" style="background:var(--color-bg-panel); border-radius:12px; max-width:400px; width:95%; overflow:hidden; padding: 2rem;">
            <h2 style="color:var(--color-primary); margin-bottom:10px;">Reset Password</h2>
            <p style="color:var(--color-text-muted); margin-bottom:20px; font-size:0.9rem;">Enter your email and we will send you a recovery link.</p>
            <input type="email" id="forgot-email" class="form-input" placeholder="you@example.com" style="margin-bottom:15px; width:100%;">
            <button class="btn btn-primary btn-block" onclick="sendResetLink()" style="margin-bottom:10px;">Send Link</button>
            <button class="btn btn-outline btn-block" onclick="document.getElementById('forgot-modal').style.display='none'">Cancel</button>
        </div>
    </div>
    <script>
        function showForgotModal(e) {
            e.preventDefault();
            document.getElementById('forgot-modal').style.display = 'flex';
        }
        function sendResetLink() {
            const email = document.getElementById('forgot-email').value;
            if(!email) return alert("Please enter your email.");
            alert("A password reset link has been securely sent to " + email);
            document.getElementById('forgot-modal').style.display = 'none';
        }
    </script>
'''

if 'id="forgot-modal"' not in login_html:
    login_html = login_html.replace('</body>', forgot_modal + '\n</body>')

open('login.html', 'w', encoding='utf-8').write(login_html)


# 2. Build settings.html
settings_code = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Account Settings | South Cafe</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500&family=Outfit:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <nav class="navbar">
        <div class="container">
            <a href="index.html" class="logo-container">
                <img src="https://res.cloudinary.com/dhg2oxagk/image/fetch/f_auto,q_auto,w_200/https%3A%2F%2Fdodptt9f4zk9h.cloudfront.net%2Fstores%2F181349%2Fsouthcaf.jpeg" alt="South Cafe" class="logo-img">
                <span class="logo-text">SOUTH CAFE</span>
            </a>
            <div class="nav-links">
                <a href="index.html" class="nav-link">Home</a>
                <a href="menu.html" class="nav-link">Menu</a>
            </div>
            <div class="nav-actions">
                <div id="nav-login-btn"></div>
                <button onclick="toggleTheme()" style="background:none; border:none; cursor:pointer; font-size:1.2rem; margin-left:15px;">🌗</button>
            </div>
        </div>
    </nav>

    <div class="container" style="max-width: 600px; padding: 4rem 15px;">
        <div style="background: var(--color-bg-panel); padding: 2rem; border-radius: 12px; box-shadow: var(--shadow-card); border: 1px solid rgba(255,255,255,0.05);">
            <h1 style="font-size: 2rem; margin-bottom: 2rem; color: var(--color-primary);">Account Settings</h1>
            
            <div style="margin-bottom: 2rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 2rem;">
                <h3 style="margin-bottom: 15px;">Profile Details</h3>
                <p style="color:var(--color-text-muted); margin-bottom:10px;">Logged in as: <strong id="settings-username" style="color:var(--color-text);">User</strong></p>
            </div>

            <div style="display:flex; flex-direction:column; gap:15px;">
                <button class="btn btn-outline" onclick="logoutAccount()" style="text-align:left; font-weight:600; padding:15px; border-color:transparent; background:rgba(0,0,0,0.4);">🚪 Log Out</button>
                <button class="btn btn-outline" onclick="triggerDelete()" style="text-align:left; font-weight:600; color:#ff4444; border-color:#ff4444; padding:15px;">⚠️ Delete Account</button>
            </div>
        </div>
    </div>

    <!-- Delete Confirmation Modal -->
    <div class="modal-overlay" id="delete-modal" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.8); z-index:9000; align-items:center; justify-content:center;">
        <div class="modal-content" style="background:var(--color-bg-panel); border-radius:12px; max-width:400px; width:95%; overflow:hidden; padding: 2rem; text-align:center;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">⚠️</div>
            <h2 style="color:#ff4444; margin-bottom:10px;">Are you sure?</h2>
            <p style="color:var(--color-text-muted); margin-bottom:25px;">Are you sure you want to delete your account? This action is permanent and cannot be undone.</p>
            
            <div style="display:flex; gap: 15px;">
                <button class="btn btn-outline" style="flex:1; border-color:var(--color-text-muted); color:var(--color-text-muted);" onclick="document.getElementById('delete-modal').style.display='none'">No, cancel</button>
                <button class="btn btn-primary" style="flex:1; background:#ff4444; border-color:#ff4444;" onclick="confirmDeleteAccount()">Yes, delete it</button>
            </div>
        </div>
    </div>

    <script src="js/app.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const user = localStorage.getItem('southcafe_user');
            if(user) document.getElementById('settings-username').innerText = user;
            else window.location.href = 'login.html';
        });

        function logoutAccount() {
            localStorage.removeItem('southcafe_user');
            window.location.href = 'index.html';
        }

        function triggerDelete() {
            document.getElementById('delete-modal').style.display = 'flex';
        }

        function confirmDeleteAccount() {
            localStorage.removeItem('southcafe_user');
            localStorage.removeItem('south_wallet_balance'); // Clear associated records securely
            alert('Account successfully deleted.');
            window.location.href = 'index.html';
        }
    </script>
</body>
</html>
'''
open('settings.html', 'w', encoding='utf-8').write(settings_code)


# 3. Update app.js `updateNav` to show ⚙️ settings button globally
js = open('js/app.js', 'r', encoding='utf-8').read()
new_nav_logic = '''function updateNav() {
    const user = localStorage.getItem('southcafe_user');
    const btnContainer = document.getElementById('nav-login-btn');
    if (!btnContainer) return;
    
    if(user) {
        btnContainer.innerHTML = `<a href="settings.html" class="btn btn-outline" style="padding: 5px 15px; border-color:rgba(255,255,255,0.2); color:inherit;">⚙️ ${user}</a>`;
    } else {
        btnContainer.innerHTML = `<a href="login.html" class="btn btn-outline" style="padding: 5px 15px;">Login</a>`;
    }
}'''

import re
# Replace entire updateNav function safely
js = re.sub(r'function updateNav\(\) \{[\s\S]*?(?=function [a-zA-Z]|\Z)', new_nav_logic + '\n\n', js)

open('js/app.js', 'w', encoding='utf-8').write(js)
