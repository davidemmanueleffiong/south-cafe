import re
import os

os.chdir(r'c:\Users\USER\Desktop\anti-gravity')

# 1. Update css/styles.css for Mobile Responsiveness
css = open('css/styles.css', 'r', encoding='utf-8').read()
mobile_css = '''
/* Mobile Responsiveness Layer */
@media (max-width: 768px) {
    .navbar .container { flex-direction: column; gap: 10px; }
    .nav-links { display: none !important; }
    .nav-actions { width: 100%; justify-content: center; flex-wrap: wrap; }
    #home h1 { font-size: 2.2rem !important; margin-top: 50px; }
    .section { padding: 60px 0 !important; }
    .menu-categories { flex-wrap: wrap; }
    #global-search { width: 150px; }
    .container { width: 95%; }
}
'''
if '@media (max-width: 768px)' not in css:
    open('css/styles.css', 'a', encoding='utf-8').write('\n' + mobile_css)

# 2. Update index.html menu categories
html = open('index.html', 'r', encoding='utf-8').read()

old_categories = '''<div class="menu-categories" style="display:flex; justify-content:center; gap:20px; margin-bottom:40px;">
                <button class="btn btn-primary" style="background:var(--color-primary); border-radius:30px;">Coffee</button>
                <button class="btn btn-outline" style="border-radius:30px;">Breakfast</button>
                <button class="btn btn-outline" style="border-radius:30px;">Snacks</button>
                <button class="btn btn-outline" style="border-radius:30px;">Desserts</button>
            </div>'''
            
new_categories = '''<div class="menu-categories" style="display:flex; justify-content:center; gap:20px; margin-bottom:40px;">
                <button class="btn cat-btn" style="background:var(--color-primary); color:#111; border-radius:30px;" onclick="filterCategory('All', this)">All</button>
                <button class="btn btn-outline cat-btn" style="border-radius:30px;" onclick="filterCategory('Parfait', this)">Parfait</button>
                <button class="btn btn-outline cat-btn" style="border-radius:30px;" onclick="filterCategory('Shawarma', this)">Shawarma</button>
            </div>'''
            
html = html.replace(old_categories, new_categories)

# 3. Update Contact section internal UI to include the Location toggle
old_contact_block = '''<h2 style="font-size:2.5rem; color:var(--color-primary); margin-bottom:20px; font-family:'Playfair Display', serif;">Visit Us</h2>
                <p style="color:var(--color-text-muted); margin-bottom:10px;">📍 14 Luxury Avenue, Calabar</p>
                <p style="color:var(--color-text-muted); margin-bottom:10px;">📞 +234 802 850 5626</p>'''

new_contact_block = '''<h2 style="font-size:2.5rem; color:var(--color-primary); margin-bottom:20px; font-family:'Playfair Display', serif;">Visit Us</h2>
                <div style="margin-bottom:20px; display:inline-flex; border: 1px solid var(--color-primary); border-radius:30px; overflow:hidden;">
                    <button id="loc-btn-calabar" onclick="setLocation('Calabar')" class="btn" style="background:var(--color-primary); color:#111; border-radius:0; padding:10px 20px; border:none;">Calabar</button>
                    <button id="loc-btn-uyo" onclick="setLocation('Uyo')" class="btn" style="background:transparent; color:var(--color-text); border-radius:0; padding:10px 20px; border:none;">Uyo</button>
                </div>
                <p id="contact-address" style="color:var(--color-text-muted); margin-bottom:10px;">📍 14 Luxury Avenue, Calabar</p>
                <p style="color:var(--color-text-muted); margin-bottom:10px;">📞 +234 802 850 5626</p>'''

html = html.replace(old_contact_block, new_contact_block)

# 4. Inject Logic Script right before </body>
script_injection = '''
    <script>
        function filterCategory(cat, btnElement) {
            // Update Active button state
            document.querySelectorAll('.cat-btn').forEach(btn => {
                btn.style.background = 'transparent';
                btn.style.color = 'var(--color-text)';
            });
            btnElement.style.background = 'var(--color-primary)';
            btnElement.style.color = '#111';
            
            // Filter
            const cards = document.querySelectorAll('.product-card');
            cards.forEach(card => {
                const title = card.querySelector('h3').innerText.toLowerCase();
                if(cat === 'All') {
                    card.style.display = 'block';
                } else if (title.includes(cat.toLowerCase())) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        }
        
        function setLocation(loc) {
            document.getElementById('loc-btn-calabar').style.background = loc === 'Calabar' ? 'var(--color-primary)' : 'transparent';
            document.getElementById('loc-btn-calabar').style.color = loc === 'Calabar' ? '#111' : 'var(--color-text)';
            document.getElementById('loc-btn-uyo').style.background = loc === 'Uyo' ? 'var(--color-primary)' : 'transparent';
            document.getElementById('loc-btn-uyo').style.color = loc === 'Uyo' ? '#111' : 'var(--color-text)';
            
            document.getElementById('contact-address').innerText = loc === 'Calabar' ? '📍 14 Luxury Avenue, Calabar' : '📍 22 Premium Lane, Uyo';
        }
    </script>
</body>
'''
html = html.replace('</body>', script_injection)

open('index.html', 'w', encoding='utf-8').write(html)
