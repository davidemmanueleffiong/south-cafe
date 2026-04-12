import glob
import os
import re

os.chdir(r'c:\Users\USER\Desktop\anti-gravity')

# 1. Update CSS
css_content = open('css/styles.css', 'r', encoding='utf-8').read()
new_css = '''
/* Search Suggestions */
#search-suggestions { position: absolute; top: calc(100% + 5px); left: 0; width: 100%; min-width:250px; background: var(--color-bg-panel); border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; z-index: 6000; box-shadow: var(--shadow-card); max-height: 300px; overflow-y: auto; display: none; }
.suggestion-item { padding: 10px 15px; display: flex; align-items: center; gap: 10px; cursor: pointer; border-bottom: 1px solid rgba(255,255,255,0.05); transition: var(--transition-fast); }
.suggestion-item:hover { background: rgba(0, 148, 68, 0.1); }
.suggestion-img { width: 40px; height: 40px; border-radius: 4px; object-fit: cover; }
.suggestion-info { flex: 1; }
.suggestion-title { font-size: 0.9rem; font-weight: bold; color: var(--color-text); margin-bottom: 2px; }
.suggestion-price { font-size: 0.8rem; color: var(--color-text-muted); }
'''
if 'suggestion-item' not in css_content:
    open('css/styles.css', 'a', encoding='utf-8').write(new_css)

# 2. Update JS Logic
js = open('js/app.js', 'r', encoding='utf-8').read()
new_js = '''
const southCatalog = {
    '2 Liters Exotic Parfait': { price: 33000, img: 'assets/images/parfait.png', desc: 'The ultimate luxury parfait. A monumental 2-liter bucket layered with premium Greek yoghurt, imported exotic berries, golden honey, and artisan granola. Perfect for parties!' },
    '2 Liter Classic Parfait': { price: 26500, img: 'assets/images/parfait.png', desc: 'A massive 2-liter bowl of our classic blend. Rich yoghurt, fresh seasonal fruits, and crunchy toppings designed for serious cravings.' },
    '1 Liter Exotic Parfait': { price: 16500, img: 'assets/images/parfait.png', desc: 'An indulgent 1-liter treat saturated with exotic imported fruits and creamy luxury yogurt.' },
    '1 Liter Classic Parfait': { price: 13500, img: 'assets/images/parfait.png', desc: 'Our signature staple in a heavy 1-liter cup. Packed with natural sweetness and perfectly balanced granola.' },
    '500ml Exotic Parfait': { price: 8500, img: 'assets/images/parfait.png', desc: 'A dense, premium 500ml cup overflowing with strawberries, blueberries, and kiwi over Greek yoghurt.' },
    '500ml classic Bowl': { price: 7000, img: 'assets/images/parfait.png', desc: 'A perfectly sized 500ml cup offering the traditional South Cafe fruit and yogurt experience.' },
    '330ml Exotic Parfait': { price: 6500, img: 'assets/images/parfait.png', desc: 'Our premium exotic toppings packed into a convenient personal 330ml size.' },
    '330ml Classic Parfait': { price: 5500, img: 'assets/images/parfait.png', desc: 'The perfect on-the-go classic yogurt blend in an easy 330ml grab-and-go cup.' },
    'Extra-special Shawarma': { price: 6000, img: 'assets/images/shawarma.png', desc: 'The ultimate luxury wrap. Filled to the brim with premium smoked meats, double sausage, cheese, and our secret creamy sauce.' },
    'Special Shawarma': { price: 5500, img: 'assets/images/shawarma.png', desc: 'A massive wrap packing mixed chicken and beef cuts, double sausage, and extra creamy mayo.' },
    'Regular Shawarma': { price: 4900, img: 'assets/images/shawarma.png', desc: 'Classic chicken or beef shawarma rolled with fresh vegetables, spices, and our signature South Cafe sauce.' },
    'Mini Parfait': { price: 2500, img: 'assets/images/parfait.png', desc: 'A quick taste of everything nice. Fresh yoghurt layered with seasonal fruits.' },
    'Regular Parfait': { price: 3500, img: 'assets/images/parfait.png', desc: 'The standard delight. Fresh yogurt, exotic fruits, nuts and organic honey.' },
    'Large Parfait': { price: 5000, img: 'assets/images/parfait.png', desc: 'A hearty serving of our signature yogurt paired with sweet fruits and crunchy granola.' }
};

window.showProductDetails = function(name) {
    const detail = southCatalog[name];
    if(!detail) return;
    
    document.getElementById('detail-img').src = detail.img;
    document.getElementById('detail-title').innerText = name;
    document.getElementById('detail-desc').innerText = detail.desc;
    document.getElementById('detail-price').innerText = new Intl.NumberFormat('en-NG', { style: 'currency', currency: 'NGN' }).format(detail.price);
    
    document.getElementById('detail-add-btn').onclick = function() {
        addToCart(name, detail.price, detail.img);
        closeProductDetails();
    };
    
    document.getElementById('product-detail-modal').style.display = 'flex';
}

window.closeProductDetails = function() {
    document.getElementById('product-detail-modal').style.display = 'none';
}

window.searchProducts = function() {
    const val = document.getElementById('global-search').value.toLowerCase();
    const sugBox = document.getElementById('search-suggestions');
    if(!sugBox) return; 
    
    if(!val) { sugBox.style.display = 'none'; return; }
    
    sugBox.innerHTML = '';
    let matches = 0;
    
    for (const [name, data] of Object.entries(southCatalog)) {
        if(name.toLowerCase().includes(val)) {
            matches++;
            const priceFmt = new Intl.NumberFormat('en-NG', { style: 'currency', currency: 'NGN' }).format(data.price);
            sugBox.innerHTML += `
                <div class="suggestion-item" onclick="document.getElementById('global-search').value=''; document.getElementById('search-suggestions').style.display='none'; showProductDetails('${name}')">
                    <img src="${data.img}" class="suggestion-img">
                    <div class="suggestion-info">
                        <div class="suggestion-title">${name}</div>
                        <div class="suggestion-price">${priceFmt}</div>
                    </div>
                </div>
            `;
        }
    }
    
    if(matches > 0) { sugBox.style.display = 'block'; } 
    else { sugBox.style.display = 'none'; }
}
'''

start = js.find('window.searchProducts = function()')
end = js.find('// Intercept search queries')
if start != -1 and end != -1:
    js = js[:start] + new_js + '\n' + js[end:]
    open('js/app.js', 'w', encoding='utf-8').write(js)


# 3. Update HTML files
modal_html = '''
    <div class="modal-overlay" id="product-detail-modal" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.8); z-index:9000; align-items:center; justify-content:center;">
        <div class="modal-content" style="background:var(--color-bg-panel); border-radius:12px; max-width:400px; width:95%; overflow:hidden;">
            <div style="position:relative;">
                <img id="detail-img" src="" style="width:100%; height:250px; object-fit:cover;">
                <span onclick="closeProductDetails()" style="position:absolute; top:10px; right:10px; background:rgba(0,0,0,0.5); color:#fff; width:30px; height:30px; display:flex; align-items:center; justify-content:center; border-radius:50%; cursor:pointer;">✕</span>
            </div>
            <div style="padding: 2rem;">
                <h2 id="detail-title" style="color:var(--color-primary); margin-bottom:10px;"></h2>
                <div id="detail-price" style="font-size:1.2rem; font-weight:bold; margin-bottom:15px; color:var(--color-text);"></div>
                <p id="detail-desc" style="color:var(--color-text-muted); line-height:1.6; margin-bottom:20px;"></p>
                <button id="detail-add-btn" class="btn btn-primary btn-block">Add to Cart</button>
            </div>
        </div>
    </div>
'''

for file in glob.glob('*.html'):
    html = open(file, 'r', encoding='utf-8').read()
    
    # Apply suggestion box underneath global search if it exists
    if 'id="global-search"' in html and 'id="search-suggestions"' not in html:
        # locate search bar parent relative div
        html = re.sub(r'(<input type="text" id="global-search"[^>]+>.*?</div>)', r'\1\n                <div id="search-suggestions"></div>', html, flags=re.DOTALL)
        
    if 'id="product-detail-modal"' not in html:
        html = html.replace('</body>', modal_html + '\n</body>')
        
    # Make product cards slightly interactive (make title click trigger modal)
    # Simple replace for specifically indexed items in menu.html and index.html
    items = [
        '2 Liters Exotic Parfait', '2 Liter Classic Parfait', '1 Liter Exotic Parfait', '1 Liter Classic Parfait',
        '500ml Exotic Parfait', '500ml classic Bowl', '330ml Exotic Parfait', '330ml Classic Parfait',
        'Extra-special Shawarma', 'Special Shawarma', 'Regular Shawarma',
        'Mini Parfait', 'Regular Parfait', 'Large Parfait', 'Mini Luxury Parfait', 'Regular Luxury Parfait'
    ]
    
    # Adding string replaces to h3 to attach modal trigger. (Need to match exactly or broadly)
    # e.g., <h3 class="product-title">Regular Shawarma</h3>
    for item in items:
        # Handles index.html manual h3
        html = html.replace(
            f'<h3 style="font-size:1rem; color:#333; margin-bottom:5px; font-weight:400;">{item}</h3>',
            f'<h3 onclick="showProductDetails(\'{item}\')" style="font-size:1rem; color:#333; margin-bottom:5px; font-weight:600; cursor:pointer;" onmouseover="this.style.textDecoration=\'underline\'" onmouseout="this.style.textDecoration=\'none\'">{item}</h3>'
        )
        # Handles menu.html classes
        html = html.replace(
            f'<h3 class="product-title">{item}</h3>',
            f'<h3 class="product-title" onclick="showProductDetails(\'{item.replace("Luxury ", "")}\')" style="cursor:pointer;" onmouseover="this.style.textDecoration=\'underline\'" onmouseout="this.style.textDecoration=\'none\'">{item}</h3>'
        )
        
    open(file, 'w', encoding='utf-8').write(html)
