import os
import glob
import re

os.chdir(r'c:\Users\USER\Desktop\anti-gravity')

# 1. Update CSS File
css = open('css/styles.css', 'r', encoding='utf-8').read()

# Replace fonts
css = re.sub(r'(--font-heading:).*?;', r"\1 'Playfair Display', serif;", css)
css = re.sub(r'(--font-body:).*?;', r"\1 'Poppins', sans-serif;", css)

# Replace variables aggressively
css_overrides = '''
:root {
  --color-primary: #3e2723; 
  --color-primary-dark: #2a1a17;
  --color-accent: #d4af37; 
  --color-bg-dark: #fcf8f2;
  --color-bg-panel: #ffffff;
  --color-bg-card: #fdfdfd;
  --color-text: #2c2c2c;
  --color-text-muted: #757575;
  --shadow-card: 0 8px 30px rgba(0, 0, 0, 0.05);
}

html {
    scroll-behavior: smooth;
}

[data-theme="dark"] {
  --color-bg-dark: #121212;
  --color-bg-panel: #1e1e1e;
  --color-bg-card: #252525;
  --color-text: #f5f5f5;
  --color-text-muted: #a1a1aa;
}

/* Glassmorphism Classes */
.glass {
    background: rgba(255, 255, 255, 0.7);
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    border: 1px solid rgba(255,255,255,0.2);
}
[data-theme="dark"] .glass {
    background: rgba(30, 30, 30, 0.7);
    border-color: rgba(255,255,255,0.05);
}

/* Smooth Image Hover */
.hover-scale { overflow: hidden; }
.hover-scale img { transition: var(--transition-smooth); }
.hover-scale:hover img { transform: scale(1.05); }

'''

# Inject these at the very top of file after the imports
css = "/* New Coffee Palette Override */\n" + css_overrides + css

open('css/styles.css', 'w', encoding='utf-8').write(css)

# 2. Update JS Catalog
js = open('js/app.js', 'r', encoding='utf-8').read()

coffee_catalog = '''const southCatalog = {
    'Artisan Espresso': { price: 2500, img: 'https://images.unsplash.com/photo-1510591509098-f4fdc6d0ff04?q=80&w=600', desc: 'A double shot of our finest house blend. Rich, dark, and intensely aromatic.' },
    'Vanilla Caramel Latte': { price: 3500, img: 'https://images.unsplash.com/photo-1557006021-b85faa2bc5e2?q=80&w=600', desc: 'Smooth espresso cut with perfectly steamed milk, organic vanilla bean, and a drizzle of salted caramel.' },
    'Classic Avocado Toast': { price: 4500, img: 'https://images.unsplash.com/photo-1588137378633-bea104cb1a21?q=80&w=600', desc: 'Smashed organic avocado on toasted sourdough, topped with microgreens and chili flakes.' },
    'Buttermilk Pancakes': { price: 5000, img: 'https://images.unsplash.com/photo-1554520735-0a6b8b0ce8b0?q=80&w=600', desc: 'A stack of three fluffy buttermilk pancakes served with maple syrup and fresh berries.' },
    'Gourmet Butter Croissant': { price: 2000, img: 'https://images.unsplash.com/photo-1555507036-ab1f4038808a?q=80&w=600', desc: 'Flaky, buttery, and baked fresh every morning by our artisan pastry chefs.' },
    'Truffle Fries': { price: 3000, img: 'https://images.unsplash.com/photo-1630431341973-02e1b662ce3b?q=80&w=600', desc: 'Crispy shoestring fries tossed in parmesan cheese and premium white truffle oil.' },
    'New York Cheesecake': { price: 4000, img: 'https://images.unsplash.com/photo-1533134242443-d4fd215305ad?q=80&w=600', desc: 'A dense, rich slice of classic vanilla cheesecake with a graham cracker crust.' },
    'Dark Chocolate Tart': { price: 3500, img: 'https://images.unsplash.com/photo-1559598466-f5ff17b9d7a2?q=80&w=600', desc: 'Decadent 70% dark chocolate ganache inside a crisp, buttery tart shell.' }
};'''

start = js.find('const southCatalog = {')
end = js.find('window.showProductDetails = function(name)')
if start != -1 and end != -1:
    js = js[:start] + coffee_catalog + '\n\n' + js[end:]
    open('js/app.js', 'w', encoding='utf-8').write(js)

# 3. Rewrite index.html completely
new_index = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Experience Premium Coffee Like Never Before.">
    <title>South Cafe | High-End Coffee Boutique</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>

    <!-- 2. Navigation Bar (Glassmorphic) -->
    <nav class="navbar glass" style="position:fixed; top:0; width:100%; z-index:1000; padding:15px 0;">
        <div class="container" style="display:flex; justify-content:space-between; align-items:center;">
            <a href="index.html" class="logo-container" style="display:flex; align-items:center; gap:10px;">
                <span class="logo-text" style="font-family:'Playfair Display', serif; font-size:1.8rem; font-weight:700; color:var(--color-primary);">SOUTH CAFE</span>
            </a>
            
            <div class="nav-links" style="display:flex; gap:2rem;">
                <a href="#home" class="nav-link" style="font-weight:500;">Home</a>
                <a href="#about" class="nav-link" style="font-weight:500;">About</a>
                <a href="#menu" class="nav-link" style="font-weight:500;">Menu</a>
                <a href="#contact" class="nav-link" style="font-weight:500;">Contact</a>
            </div>

            <div class="nav-actions" style="display:flex; gap:1rem; align-items:center;">
                <!-- Search wrapper -->
                <div style="position:relative;">
                    <input type="text" id="global-search" onkeyup="searchProducts()" placeholder="Search..." style="padding:8px 15px; border-radius:20px; border:1px solid #ddd; outline:none; background:rgba(255,255,255,0.5);">
                    <div id="search-suggestions" style="position:absolute; top:100%; left:0; width:100%; background:var(--color-bg-panel); display:none; max-height:200px; overflow-y:auto; border-radius:8px; box-shadow:var(--shadow-card); z-index:2000;"></div>
                </div>
                
                <div id="nav-login-btn"></div>
                <div class="cart-icon" onclick="toggleCart()" style="cursor:pointer;">
                    🛒 <span class="cart-badge" id="cart-badge" style="background:var(--color-accent); color:white; border-radius:50%; padding:2px 6px; font-size:0.7rem; position:absolute; top:-10px; right:-10px;">0</span>
                </div>
            </div>
        </div>
    </nav>

    <!-- 1. Hero Section -->
    <section id="home" style="height:100vh; background:linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('https://images.unsplash.com/photo-1497935586351-b67a49e012bf?q=80&w=2000') center/cover; display:flex; align-items:center; justify-content:center; text-align:center; color:#fff; position:relative;">
        <div class="container" style="max-width:800px; padding-top:60px;">
            <h1 style="font-size:3.5rem; margin-bottom:20px; text-shadow:2px 2px 5px rgba(0,0,0,0.5); font-family:'Playfair Display', serif;">Experience Premium Coffee Like Never Before</h1>
            <p style="font-size:1.2rem; font-weight:300; margin-bottom:40px; color:#e0e0e0;">Freshly brewed coffee, delicious meals, and a cozy atmosphere</p>
            <div style="display:flex; gap:20px; justify-content:center;">
                <a href="#menu" class="btn btn-primary" style="background:var(--color-accent); color:#111; padding:15px 30px; font-size:1.1rem; border-radius:30px;">View Menu</a>
                <a href="#contact" class="btn btn-outline" style="border:2px solid #fff; color:#fff; padding:15px 30px; font-size:1.1rem; border-radius:30px;">Visit Us</a>
            </div>
        </div>
    </section>

    <!-- 3. About Section -->
    <section id="about" class="section" style="padding:100px 0;">
        <div class="container" style="display:flex; flex-wrap:wrap; align-items:center; gap:50px;">
            <div style="flex:1; min-width:300px; padding:20px;">
                <img src="https://images.unsplash.com/photo-1554118811-1e0d58224f24?q=80&w=1000" style="width:100%; border-radius:15px; box-shadow:var(--shadow-card);" alt="Coffee brewing">
            </div>
            <div style="flex:1; min-width:300px;">
                <h2 style="font-size:2.5rem; color:var(--color-primary); margin-bottom:20px; font-family:'Playfair Display', serif;">Our Story</h2>
                <p style="color:var(--color-text-muted); font-size:1.1rem; margin-bottom:20px;">Founded in the heart of the city, South Cafe represents the absolute pinnacle of luxury cafe culture. We source only the top 1% of ethically farmed beans globally, air-roasting them perfectly to preserve their distinct flavor profiles.</p>
                <p style="color:var(--color-text-muted); font-size:1.1rem;">It's not just a cup of coffee. It is an uncompromising dedication to comfort, quality, and your daily experience.</p>
            </div>
        </div>
    </section>

    <!-- 4. Menu Section -->
    <section id="menu" class="section" style="background:var(--color-bg-card); padding:100px 0;">
        <div class="container text-center">
            <h2 style="font-size:3rem; color:var(--color-primary); margin-bottom:10px; font-family:'Playfair Display', serif;">Curated Menu</h2>
            <p style="color:var(--color-text-muted); margin-bottom:50px;">Select from our premium offerings</p>
            
            <div class="menu-categories" style="display:flex; justify-content:center; gap:20px; margin-bottom:40px;">
                <button class="btn btn-primary" style="background:var(--color-primary); border-radius:30px;">Coffee</button>
                <button class="btn btn-outline" style="border-radius:30px;">Breakfast</button>
                <button class="btn btn-outline" style="border-radius:30px;">Snacks</button>
                <button class="btn btn-outline" style="border-radius:30px;">Desserts</button>
            </div>

            <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:30px; text-align:left;">
                
                <!-- Coffee/Item Cards -->
                <div class="product-card glass hover-scale" style="padding:20px; border-radius:15px; cursor:pointer;" onclick="showProductDetails('Artisan Espresso')">
                    <div style="width:100%; height:200px; border-radius:10px; overflow:hidden; margin-bottom:15px;"><img src="https://images.unsplash.com/photo-1510591509098-f4fdc6d0ff04?q=80&w=600" style="width:100%; height:100%; object-fit:cover;"></div>
                    <h3 style="font-size:1.3rem; margin-bottom:5px; font-family:'Playfair Display', serif;">Artisan Espresso</h3>
                    <p style="color:var(--color-text-muted); font-size:0.9rem; margin-bottom:15px; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden;">A double shot of our finest house blend.</p>
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <span style="font-weight:700; color:var(--color-accent); font-size:1.2rem;">₦2,500</span>
                        <span style="background:var(--color-primary); color:#fff; padding:5px 15px; border-radius:5px; font-size:0.9rem;">View</span>
                    </div>
                </div>

                <div class="product-card glass hover-scale" style="padding:20px; border-radius:15px; cursor:pointer;" onclick="showProductDetails('Vanilla Caramel Latte')">
                    <div style="width:100%; height:200px; border-radius:10px; overflow:hidden; margin-bottom:15px;"><img src="https://images.unsplash.com/photo-1557006021-b85faa2bc5e2?q=80&w=600" style="width:100%; height:100%; object-fit:cover;"></div>
                    <h3 style="font-size:1.3rem; margin-bottom:5px; font-family:'Playfair Display', serif;">Vanilla Caramel Latte</h3>
                    <p style="color:var(--color-text-muted); font-size:0.9rem; margin-bottom:15px; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden;">Smooth espresso cut perfectly steamed milk.</p>
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <span style="font-weight:700; color:var(--color-accent); font-size:1.2rem;">₦3,500</span>
                        <span style="background:var(--color-primary); color:#fff; padding:5px 15px; border-radius:5px; font-size:0.9rem;">View</span>
                    </div>
                </div>

                <div class="product-card glass hover-scale" style="padding:20px; border-radius:15px; cursor:pointer;" onclick="showProductDetails('Classic Avocado Toast')">
                    <div style="width:100%; height:200px; border-radius:10px; overflow:hidden; margin-bottom:15px;"><img src="https://images.unsplash.com/photo-1588137378633-bea104cb1a21?q=80&w=600" style="width:100%; height:100%; object-fit:cover;"></div>
                    <h3 style="font-size:1.3rem; margin-bottom:5px; font-family:'Playfair Display', serif;">Classic Avocado Toast</h3>
                    <p style="color:var(--color-text-muted); font-size:0.9rem; margin-bottom:15px; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden;">Smashed organic avocado on sourdough.</p>
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <span style="font-weight:700; color:var(--color-accent); font-size:1.2rem;">₦4,500</span>
                        <span style="background:var(--color-primary); color:#fff; padding:5px 15px; border-radius:5px; font-size:0.9rem;">View</span>
                    </div>
                </div>
                
                <div class="product-card glass hover-scale" style="padding:20px; border-radius:15px; cursor:pointer;" onclick="showProductDetails('New York Cheesecake')">
                    <div style="width:100%; height:200px; border-radius:10px; overflow:hidden; margin-bottom:15px;"><img src="https://images.unsplash.com/photo-1533134242443-d4fd215305ad?q=80&w=600" style="width:100%; height:100%; object-fit:cover;"></div>
                    <h3 style="font-size:1.3rem; margin-bottom:5px; font-family:'Playfair Display', serif;">New York Cheesecake</h3>
                    <p style="color:var(--color-text-muted); font-size:0.9rem; margin-bottom:15px; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden;">Dense, rich slice of classic vanilla cheesecake.</p>
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <span style="font-weight:700; color:var(--color-accent); font-size:1.2rem;">₦4,000</span>
                        <span style="background:var(--color-primary); color:#fff; padding:5px 15px; border-radius:5px; font-size:0.9rem;">View</span>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- 5. Featured Section -->
    <section id="featured" class="section" style="padding:100px 0;">
        <div class="container text-center">
            <h2 style="font-size:2.5rem; color:var(--color-primary); margin-bottom:40px; font-family:'Playfair Display', serif;">Signature Selection</h2>
            <div style="display:flex; flex-wrap:wrap; gap:30px; justify-content:center;">
                <div class="glass" style="flex:1; min-width:300px; padding:30px; border-radius:15px; text-align:left; background:url('https://images.unsplash.com/photo-1497935586351-b67a49e012bf?q=80&w=600') center/cover; position:relative; overflow:hidden;">
                    <div style="position:absolute; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.6);"></div>
                    <div style="position:relative; color:#fff;">
                        <h3 style="font-size:1.8rem; margin-bottom:10px; font-family:'Playfair Display', serif;">The Golden Bean Roast</h3>
                        <p style="font-size:1rem; margin-bottom:20px; color:#ddd;">Exclusive imported espresso infused with rich chocolate notes.</p>
                        <button class="btn" style="background:#fff; color:#111;">Order Now</button>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 6. Testimonials Section -->
    <section id="testimonials" class="section" style="background:var(--color-bg-card); padding:100px 0;">
        <div class="container text-center">
            <h2 style="font-size:2.5rem; color:var(--color-primary); margin-bottom:40px; font-family:'Playfair Display', serif;">What Our Clients Say</h2>
            <div style="display:flex; flex-wrap:wrap; gap:30px;">
                <div class="glass" style="flex:1; min-width:250px; padding:30px; border-radius:10px; text-align:center;">
                    <p style="font-style:italic; color:var(--color-text-muted); margin-bottom:20px;">"The Vanilla Caramel Latte is an absolute masterpiece. Best cafe in town!"</p>
                    <h4 style="color:var(--color-primary);">- Sarah Jenkins</h4>
                </div>
                <div class="glass" style="flex:1; min-width:250px; padding:30px; border-radius:10px; text-align:center;">
                    <p style="font-style:italic; color:var(--color-text-muted); margin-bottom:20px;">"Their avocado toast and espresso combination totally saves my mornings."</p>
                    <h4 style="color:var(--color-primary);">- Michael Adebayo</h4>
                </div>
                <div class="glass" style="flex:1; min-width:250px; padding:30px; border-radius:10px; text-align:center;">
                    <p style="font-style:italic; color:var(--color-text-muted); margin-bottom:20px;">"Incredible elegant interior and the cheesecake is strictly world-class."</p>
                    <h4 style="color:var(--color-primary);">- Elena Roberts</h4>
                </div>
            </div>
        </div>
    </section>

    <!-- 7. Contact Section -->
    <section id="contact" class="section" style="padding:100px 0;">
        <div class="container" style="display:flex; flex-wrap:wrap; gap:50px;">
            <div style="flex:1; min-width:300px;">
                <h2 style="font-size:2.5rem; color:var(--color-primary); margin-bottom:20px; font-family:'Playfair Display', serif;">Visit Us</h2>
                <p style="color:var(--color-text-muted); margin-bottom:10px;">📍 14 Luxury Avenue, Calabar</p>
                <p style="color:var(--color-text-muted); margin-bottom:10px;">📞 +234 802 850 5626</p>
                <p style="color:var(--color-text-muted); margin-bottom:30px;">📧 hello@southcafe.ng</p>
                <div style="width:100%; height:250px; background:#e0e0e0; border-radius:10px; display:flex; align-items:center; justify-content:center; color:#666;">[Embedded Google Map UI]</div>
            </div>
            <div style="flex:1; min-width:300px; background:var(--color-bg-card); padding:30px; border-radius:15px; box-shadow:var(--shadow-card);">
                <form>
                    <div style="margin-bottom:15px;"><input type="text" placeholder="Your Name" style="width:100%; padding:12px; border:1px solid #ddd; border-radius:5px;"></div>
                    <div style="margin-bottom:15px;"><input type="email" placeholder="Your Email" style="width:100%; padding:12px; border:1px solid #ddd; border-radius:5px;"></div>
                    <div style="margin-bottom:15px;"><textarea placeholder="Your Message" rows="5" style="width:100%; padding:12px; border:1px solid #ddd; border-radius:5px;"></textarea></div>
                    <button class="btn btn-primary btn-block" style="background:var(--color-primary); color:#fff;">Send Message</button>
                </form>
            </div>
        </div>
    </section>

    <!-- 8. Footer Section -->
    <footer style="background:var(--color-primary-dark); color:#fff; padding:50px 0; text-align:center;">
        <div class="container">
            <h2 style="font-family:'Playfair Display', serif; margin-bottom:20px; font-size:2rem; color:var(--color-accent);">South Cafe</h2>
            <div style="display:flex; justify-content:center; gap:20px; margin-bottom:30px;">
                <span>Opening Hours: Mon-Sun 7AM - 10PM</span>
            </div>
            <p style="color:#aaa; font-size:0.9rem;">&copy; 2026 South Cafe. All rights reserved.</p>
        </div>
    </footer>


    <!-- Global UI Integrations (Modals/AI/Cart) -->
    
    <div class="cart-drawer-overlay" id="cart-overlay" onclick="toggleCart(false)"></div>
    <div class="cart-drawer" id="cart-drawer">
        <div class="cart-header"><h3>Your Order</h3><div style="cursor:pointer;" onclick="toggleCart(false)">✕</div></div>
        <div class="cart-items" id="cart-items"></div>
        <div class="cart-footer">
            <div class="cart-total"><span>Total:</span><span id="cart-total-price">₦0.00</span></div>
            <button class="btn btn-primary btn-block" onclick="openCheckout()">Checkout</button>
        </div>
    </div>

    <div class="modal-overlay" id="checkout-modal">
        <div class="modal-content">
            <div class="modal-header"><h2>Secure Checkout</h2><span class="modal-close" onclick="closeCheckout()">✕</span></div>
            <p style="color:var(--color-text-muted); margin-bottom:1.5rem;">Amount Due: <strong style="color:var(--color-primary); font-size:1.5rem;" id="checkout-amount"></strong></p>
            <div class="payment-methods">
                <div class="pay-method active" id="pay-wallet" onclick="selectPaymentMethod('wallet')"><div class="pay-icon">👛</div><div>South Wallet</div></div>
            </div>
            <form onsubmit="confirmPayment(event)"><button type="submit" id="confirm-payment-btn" class="btn btn-primary btn-block">Pay via Wallet</button></form>
        </div>
    </div>

    <!-- AI Widget Component -->
    <div class="ai-widget">
        <div class="ai-chat-window" id="ai-chat-window">
            <div class="ai-chat-header">
                <div class="ai-title"><span style="font-size:1.2rem;">✨</span> South AI Assistant</div>
                <div class="close-ai" onclick="toggleAI()">✕</div>
            </div>
            <div class="ai-messages" id="ai-messages">
                <div class="message msg-ai">Hi! I am South AI. Type "Order Espresso" to add coffee to your cart securely!</div>
            </div>
            <div class="ai-input-area">
                <input type="text" id="ai-message-input" class="ai-input" placeholder="Type here...">
                <button class="ai-mic" onclick="toggleVoiceAI()" style="background:transparent; border:none; font-size:1.5rem; cursor:pointer;" title="Click to Record">🎤</button>
                <button class="ai-send" onclick="sendAIMessage()">➤</button>
            </div>
        </div>
        <div class="ai-btn" onclick="toggleAI()">✨</div>
    </div>
    
    <!-- Product Detail Modal -->
    <div class="modal-overlay" id="product-detail-modal" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.8); z-index:9000; align-items:center; justify-content:center;">
        <div class="modal-content" style="background:var(--color-bg-panel); border-radius:12px; max-width:400px; width:95%; overflow:hidden;">
            <div style="position:relative;">
                <img id="detail-img" src="" style="width:100%; height:250px; object-fit:cover;">
                <span onclick="closeProductDetails()" style="position:absolute; top:10px; right:10px; background:rgba(0,0,0,0.5); color:#fff; width:30px; height:30px; display:flex; align-items:center; justify-content:center; border-radius:50%; cursor:pointer;">✕</span>
            </div>
            <div style="padding: 2rem;">
                <h2 id="detail-title" style="color:var(--color-primary); margin-bottom:10px; font-family:'Playfair Display', serif;"></h2>
                <div id="detail-price" style="font-size:1.2rem; font-weight:bold; margin-bottom:15px; color:var(--color-accent);"></div>
                <p id="detail-desc" style="color:var(--color-text-muted); line-height:1.6; margin-bottom:20px; font-family:'Poppins', sans-serif;"></p>
                <button id="detail-add-btn" class="btn btn-primary btn-block">Add to Cart</button>
            </div>
        </div>
    </div>

    <!-- Floating WhatsApp -->
    <a href="https://wa.me/2348028505626" target="_blank" class="floating-whatsapp" style="position:fixed; bottom:30px; left:30px; background-color:#25D366; color:white; width:60px; height:60px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:2rem; box-shadow:0 4px 10px rgba(0,0,0,0.3); z-index:4000; transition:0.3s;">
        <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" viewBox="0 0 16 16"><path d="M13.601 2.326A7.85 7.85 0 0 0 7.994 0C3.627 0 .068 3.558.064 7.926c0 1.399.366 2.76 1.057 3.965L0 16l4.204-1.102a7.9 7.9 0 0 0 3.79.965h.004c4.368 0 7.926-3.558 7.93-7.93A7.9 7.9 0 0 0 13.6 2.326z"/></svg>
    </a>

    <script src="js/app.js"></script>
</body>
</html>
'''

open('index.html', 'w', encoding='utf-8').write(new_index)
