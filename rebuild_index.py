import os

html = open('index.html', 'r', encoding='utf-8').read()

new_main = '''
    <main class="container" style="background:#fff; min-height:100vh; padding: 2rem 0;">
        
        <!-- Search area mimicking the image -->
        <div style="display:flex; justify-content:center; align-items:center; margin-bottom: 2rem; border-bottom: 1px solid #eee; padding-bottom: 1rem;">
            <div style="position:relative; width: 50%; max-width: 600px; display:flex; align-items:center;">
                <input type="text" placeholder="Search" style="width:100%; padding: 12px 40px 12px 20px; border-radius:30px; border:1px solid #ddd; background:#f9f9f9; font-family:'Inter'; font-size:1rem; outline:none; color:#111;">
                <span style="position:absolute; right:15px; color:#666;">🔍</span>
            </div>
        </div>

        <div class="landing-product-grid" style="display:grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap:2rem; padding: 1rem;">
            
            <div class="product-card" style="background:#fff; border:none;">
                <img src="assets/images/parfait.png" style="width:100%; height:250px; object-fit:cover; border-radius:8px; margin-bottom:10px; border: 1px solid #f0f0f0;">
                <h3 style="font-size:1rem; color:#333; margin-bottom:5px; font-weight:400;">2 Liters Exotic Parfait</h3>
                <p style="font-weight:700; color:#111; margin-bottom:15px;">₦33,000</p>
                <button class="btn btn-primary btn-block" style="background:#00a651; border-color:#00a651; border-radius:6px;" onclick="addToCart('2 Liters Exotic Parfait', 33000, 'assets/images/parfait.png')">Add to Cart</button>
            </div>

            <div class="product-card" style="background:#fff; border:none;">
                <img src="assets/images/parfait.png" style="width:100%; height:250px; object-fit:cover; border-radius:8px; margin-bottom:10px; border: 1px solid #f0f0f0;">
                <h3 style="font-size:1rem; color:#333; margin-bottom:5px; font-weight:400;">2 Liter Classic Parfait</h3>
                <p style="font-weight:700; color:#111; margin-bottom:15px;">₦26,500</p>
                <button class="btn btn-primary btn-block" style="background:#00a651; border-color:#00a651; border-radius:6px;" onclick="addToCart('2 Liter Classic Parfait', 26500, 'assets/images/parfait.png')">Add to Cart</button>
            </div>

            <div class="product-card" style="background:#fff; border:none;">
                <img src="assets/images/parfait.png" style="width:100%; height:250px; object-fit:cover; border-radius:8px; margin-bottom:10px; border: 1px solid #f0f0f0;">
                <h3 style="font-size:1rem; color:#333; margin-bottom:5px; font-weight:400;">1 Liter Exotic Parfait</h3>
                <p style="font-weight:700; color:#111; margin-bottom:15px;">₦16,500</p>
                <button class="btn btn-primary btn-block" style="background:#00a651; border-color:#00a651; border-radius:6px;" onclick="addToCart('1 Liter Exotic Parfait', 16500, 'assets/images/parfait.png')">Add to Cart</button>
            </div>

            <div class="product-card" style="background:#fff; border:none;">
                <img src="assets/images/parfait.png" style="width:100%; height:250px; object-fit:cover; border-radius:8px; margin-bottom:10px; border: 1px solid #f0f0f0;">
                <h3 style="font-size:1rem; color:#333; margin-bottom:5px; font-weight:400;">1 Liter Classic Parfait</h3>
                <p style="font-weight:700; color:#111; margin-bottom:15px;">₦13,500</p>
                <button class="btn btn-primary btn-block" style="background:#00a651; border-color:#00a651; border-radius:6px;" onclick="addToCart('1 Liter Classic Parfait', 13500, 'assets/images/parfait.png')">Add to Cart</button>
            </div>

            <div class="product-card" style="background:#fff; border:none;">
                <img src="assets/images/parfait.png" style="width:100%; height:250px; object-fit:cover; border-radius:8px; margin-bottom:10px; border: 1px solid #f0f0f0;">
                <h3 style="font-size:1rem; color:#333; margin-bottom:5px; font-weight:400;">500ml Exotic Parfait</h3>
                <p style="font-weight:700; color:#111; margin-bottom:15px;">₦8,500</p>
                <button class="btn btn-primary btn-block" style="background:#00a651; border-color:#00a651; border-radius:6px;" onclick="addToCart('500ml Exotic Parfait', 8500, 'assets/images/parfait.png')">Add to Cart</button>
            </div>

            <div class="product-card" style="background:#fff; border:none;">
                <img src="assets/images/parfait.png" style="width:100%; height:250px; object-fit:cover; border-radius:8px; margin-bottom:10px; border: 1px solid #f0f0f0;">
                <h3 style="font-size:1rem; color:#333; margin-bottom:5px; font-weight:400;">500ml classic Bowl</h3>
                <p style="font-weight:700; color:#111; margin-bottom:15px;">₦7,000</p>
                <button class="btn btn-primary btn-block" style="background:#00a651; border-color:#00a651; border-radius:6px;" onclick="addToCart('500ml classic Bowl', 7000, 'assets/images/parfait.png')">Add to Cart</button>
            </div>

            <div class="product-card" style="background:#fff; border:none;">
                <img src="assets/images/parfait.png" style="width:100%; height:250px; object-fit:cover; border-radius:8px; margin-bottom:10px; border: 1px solid #f0f0f0;">
                <h3 style="font-size:1rem; color:#333; margin-bottom:5px; font-weight:400;">330ml Exotic Parfait</h3>
                <p style="font-weight:700; color:#111; margin-bottom:15px;">₦6,500</p>
                <button class="btn btn-primary btn-block" style="background:#00a651; border-color:#00a651; border-radius:6px;" onclick="addToCart('330ml Exotic Parfait', 6500, 'assets/images/parfait.png')">Add to Cart</button>
            </div>

            <div class="product-card" style="background:#fff; border:none;">
                <img src="assets/images/parfait.png" style="width:100%; height:250px; object-fit:cover; border-radius:8px; margin-bottom:10px; border: 1px solid #f0f0f0;">
                <h3 style="font-size:1rem; color:#333; margin-bottom:5px; font-weight:400;">330ml Classic Parfait</h3>
                <p style="font-weight:700; color:#111; margin-bottom:15px;">₦5,500</p>
                <button class="btn btn-primary btn-block" style="background:#00a651; border-color:#00a651; border-radius:6px;" onclick="addToCart('330ml Classic Parfait', 5500, 'assets/images/parfait.png')">Add to Cart</button>
            </div>
            
        </div>
    </main>
'''

start = html.find('<main class="container">')
end = html.find('</main>') + 7
if start != -1 and end != -1:
    html = html[:start] + new_main + html[end:]

html = html.replace('data-theme="dark"', 'data-theme="light"')

# Fix light mode toggle if the user toggles
html = html.replace('<body', '<body data-theme="light"')

# Change mic icon logic to WhatsApp timer logic
btn_old = '<button class="ai-mic" onclick="startVoiceAI()" style="background:transparent; border:none; font-size:1.5rem; cursor:pointer;" title="Hold to Speak">🎤</button>'
btn_new = '<button class="ai-mic" onclick="toggleVoiceAI()" style="background:transparent; border:none; font-size:1.5rem; cursor:pointer;" title="Click to Record">🎤</button>'
html = html.replace(btn_old, btn_new)

open('index.html', 'w', encoding='utf-8').write(html)
