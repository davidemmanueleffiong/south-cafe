import os
import re

os.chdir(r'c:\Users\USER\Desktop\anti-gravity')

# 1. Update CSS for Dark/White Text Aesthetic
css = open('css/styles.css', 'r', encoding='utf-8').read()

# Make the root palette inherently dark luxury with white text
dark_root = '''
:root {
  --color-primary: #d4af37; /* Soft Gold is now primary for dark mode pop */
  --color-primary-dark: #b5952f;
  --color-accent: #fcf8f2; 
  --color-bg-dark: #16110f; /* Very dark rich brown/black */
  --color-bg-panel: #241c19;
  --color-bg-card: #2a221f;
  --color-text: #ffffff; /* White text as requested */
  --color-text-muted: #b0a8a6;
  --shadow-card: 0 8px 30px rgba(0, 0, 0, 0.4);
}
'''
# We completely strip the old overriding root injected in Wave 8 at the top
css = re.sub(r':root \{[\s\S]*?(?=\}\n)', dark_root.strip()[:-1], css, count=1)

open('css/styles.css', 'w', encoding='utf-8').write(css)

# 2. Update app.js to RESTORE Parfaits & Shawarmas but keep the function signature
js = open('js/app.js', 'r', encoding='utf-8').read()

luxury_parfait_catalog = '''const southCatalog = {
    '2 Liters Exotic Parfait': { price: 33000, img: 'assets/images/parfait.png', desc: 'The ultimate luxury parfait. A monumental 2-liter bucket layered with premium Greek yoghurt, imported exotic berries, golden honey, and artisan granola.' },
    'Extra-special Shawarma': { price: 6000, img: 'assets/images/shawarma.png', desc: 'The ultimate luxury wrap. Filled to the brim with premium smoked meats, double sausage, cheese, and our secret creamy sauce.' },
    'Special Shawarma': { price: 5500, img: 'assets/images/shawarma.png', desc: 'A massive wrap packing mixed chicken and beef cuts, double sausage, and extra creamy mayo.' },
    'Regular Shawarma': { price: 4900, img: 'assets/images/shawarma.png', desc: 'Classic chicken or beef shawarma rolled with fresh vegetables, spices, and our signature South Cafe sauce.' },
    '1 Liter Exotic Parfait': { price: 16500, img: 'assets/images/parfait.png', desc: 'An indulgent 1-liter treat saturated with exotic imported fruits and creamy luxury yogurt.' },
    'Mini Luxury Parfait': { price: 2500, img: 'assets/images/parfait.png', desc: 'A quick taste of everything nice. Fresh yoghurt layered with seasonal fruits.' },
    'Large Luxury Parfait': { price: 5000, img: 'assets/images/parfait.png', desc: 'A hearty serving of our signature yogurt paired with sweet fruits and crunchy granola.' },
    'Regular Luxury Parfait': { price: 3500, img: 'assets/images/parfait.png', desc: 'The standard delight. Fresh yogurt, exotic fruits, nuts and organic honey.' }
};'''

js = re.sub(r'const southCatalog = \{.*?\};', luxury_parfait_catalog, js, flags=re.DOTALL)
open('js/app.js', 'w', encoding='utf-8').write(js)

# 3. Update index.html to display Parfaits instead of Coffee
html = open('index.html', 'r', encoding='utf-8').read()

# Replace the Menu Section grid with Parfaits
new_menu_html = '''
            <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:30px; text-align:left;">
                
                <div class="product-card glass hover-scale" style="padding:20px; border-radius:15px; cursor:pointer;" onclick="showProductDetails('2 Liters Exotic Parfait')">
                    <div style="width:100%; height:200px; border-radius:10px; overflow:hidden; margin-bottom:15px; background:#1a1a1a;"><img src="assets/images/parfait.png" style="width:100%; height:100%; object-fit:contain;"></div>
                    <h3 style="font-size:1.3rem; margin-bottom:5px; font-family:'Playfair Display', serif; color:var(--color-primary);">2 Liters Exotic Parfait</h3>
                    <p style="color:var(--color-text-muted); font-size:0.9rem; margin-bottom:15px; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden;">The ultimate luxury parfait bucket.</p>
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <span style="font-weight:700; color:var(--color-text); font-size:1.2rem;">₦33,000</span>
                        <span style="background:var(--color-primary); color:#111; padding:5px 15px; border-radius:5px; font-size:0.9rem;">View</span>
                    </div>
                </div>

                <div class="product-card glass hover-scale" style="padding:20px; border-radius:15px; cursor:pointer;" onclick="showProductDetails('Extra-special Shawarma')">
                    <div style="width:100%; height:200px; border-radius:10px; overflow:hidden; margin-bottom:15px; background:#1a1a1a;"><img src="assets/images/shawarma.png" style="width:100%; height:100%; object-fit:contain;"></div>
                    <h3 style="font-size:1.3rem; margin-bottom:5px; font-family:'Playfair Display', serif; color:var(--color-primary);">Extra-special Shawarma</h3>
                    <p style="color:var(--color-text-muted); font-size:0.9rem; margin-bottom:15px; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden;">Luxury wrap filled with premium meats & cheese.</p>
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <span style="font-weight:700; color:var(--color-text); font-size:1.2rem;">₦6,000</span>
                        <span style="background:var(--color-primary); color:#111; padding:5px 15px; border-radius:5px; font-size:0.9rem;">View</span>
                    </div>
                </div>

                <div class="product-card glass hover-scale" style="padding:20px; border-radius:15px; cursor:pointer;" onclick="showProductDetails('1 Liter Exotic Parfait')">
                    <div style="width:100%; height:200px; border-radius:10px; overflow:hidden; margin-bottom:15px; background:#1a1a1a;"><img src="assets/images/parfait.png" style="width:100%; height:100%; object-fit:contain;"></div>
                    <h3 style="font-size:1.3rem; margin-bottom:5px; font-family:'Playfair Display', serif; color:var(--color-primary);">1 Liter Exotic Parfait</h3>
                    <p style="color:var(--color-text-muted); font-size:0.9rem; margin-bottom:15px; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden;">Exotic imported fruits and creamy luxury yogurt.</p>
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <span style="font-weight:700; color:var(--color-text); font-size:1.2rem;">₦16,500</span>
                        <span style="background:var(--color-primary); color:#111; padding:5px 15px; border-radius:5px; font-size:0.9rem;">View</span>
                    </div>
                </div>
                
                <div class="product-card glass hover-scale" style="padding:20px; border-radius:15px; cursor:pointer;" onclick="showProductDetails('Regular Shawarma')">
                    <div style="width:100%; height:200px; border-radius:10px; overflow:hidden; margin-bottom:15px; background:#1a1a1a;"><img src="assets/images/shawarma.png" style="width:100%; height:100%; object-fit:contain;"></div>
                    <h3 style="font-size:1.3rem; margin-bottom:5px; font-family:'Playfair Display', serif; color:var(--color-primary);">Regular Shawarma</h3>
                    <p style="color:var(--color-text-muted); font-size:0.9rem; margin-bottom:15px; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden;">Classic rolled with fresh vegetables and spices.</p>
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <span style="font-weight:700; color:var(--color-text); font-size:1.2rem;">₦4,900</span>
                        <span style="background:var(--color-primary); color:#111; padding:5px 15px; border-radius:5px; font-size:0.9rem;">View</span>
                    </div>
                </div>

            </div>
'''
html = re.sub(r'<div style="display:grid; grid-template-columns:repeat\(auto-fit, minmax\(280px, 1fr\)\).*?</div>\s*</div>\s*</section>', new_menu_html + '\n        </div>\n    </section>', html, flags=re.DOTALL)

# Need to fix the search bar to have a higher z index so its suggestions pop correctly in navbar
html = html.replace('z-index:2000;', 'z-index:9999; color:#111; border:1px solid rgba(0,0,0,0.1);')

# The modal logic text color should be safely visible
html = html.replace('id="detail-title" style="color:var(--color-primary);', 'id="detail-title" style="color:#fff;')
html = html.replace('id="detail-price" style="font-size:1.2rem; font-weight:bold; margin-bottom:15px; color:var(--color-accent);', 'id="detail-price" style="font-size:1.2rem; font-weight:bold; margin-bottom:15px; color:var(--color-primary);')
html = html.replace('id="detail-desc" style="color:var(--color-text-muted);', 'id="detail-desc" style="color:#e0e0e0;')

open('index.html', 'w', encoding='utf-8').write(html)
