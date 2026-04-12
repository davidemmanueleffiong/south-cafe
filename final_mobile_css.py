import os

os.chdir(r'c:\Users\USER\Desktop\anti-gravity')

# We are going to entirely rewrite styles.css to clear out the cascading duplicates
# and correctly set up the Dark Theme coffee aesthetic without hiding the navbar.

clean_css = '''
:root {
  --color-primary: #d4af37; 
  --color-primary-dark: #b5952f;
  --color-accent: #fcf8f2; 
  --color-bg-dark: #16110f; 
  --color-bg-panel: #241c19;
  --color-bg-card: #2a221f;
  --color-text: #ffffff; 
  --color-text-muted: #b0a8a6;
  
  --font-heading: 'Playfair Display', serif;
  --font-body: 'Poppins', sans-serif;
  
  --shadow-glow: 0 0 20px rgba(212, 175, 55, 0.3);
  --shadow-card: 0 10px 30px rgba(0,0,0,0.5);
  
  --transition-fast: 0.2s ease;
  --transition-smooth: 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

* { margin: 0; padding: 0; box-sizing: border-box; }

html { scroll-behavior: smooth; }

body {
  font-family: var(--font-body);
  background-color: var(--color-bg-dark);
  color: var(--color-text);
  line-height: 1.6;
  overflow-x: hidden;
}

h1, h2, h3, h4, h5, h6 { font-family: var(--font-heading); font-weight: 600; }
a { text-decoration: none; color: inherit; transition: var(--transition-fast); }
ul { list-style: none; }
img { max-width: 100%; display: block; border-radius: 8px; }

/* Utilities */
.container { width: 90%; max-width: 1300px; margin: 0 auto; }
.section { padding: 6rem 0; }
.text-center { text-align: center; }

/* Buttons */
.btn {
  display: inline-flex; align-items: center; justify-content: center;
  padding: 0.8rem 2rem; font-family: var(--font-heading); font-weight: 500;
  border-radius: 5px; cursor: pointer; transition: var(--transition-smooth);
  border: 1px solid transparent; letter-spacing: 1px; font-size: 0.9rem;
}
.btn-primary { background-color: var(--color-primary); color: #111; box-shadow: var(--shadow-glow); border: none; }
.btn-primary:hover { filter: brightness(1.1); transform: translateY(-3px); }
.btn-outline { background-color: transparent; border-color: var(--color-text); color: var(--color-text); }
.btn-outline:hover { background-color: rgba(255,255,255,0.1); }
.btn-block { width: 100%; }

/* Glassmorphism */
.glass {
    background: rgba(36, 28, 25, 0.7);
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    border: 1px solid rgba(255,255,255,0.05);
}

/* Animations */
.hover-scale { overflow: hidden; }
.hover-scale img { transition: var(--transition-smooth); }
.hover-scale:hover img { transform: scale(1.05); }

/* Cart Drawer */
.cart-drawer-overlay { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); opacity: 0; pointer-events: none; transition: var(--transition-smooth); z-index: 2000; }
.cart-drawer-overlay.open { opacity: 1; pointer-events: all; }
.cart-drawer { position: fixed; top: 0; right: -400px; width: 400px; height: 100%; background: var(--color-bg-panel); box-shadow: -5px 0 30px rgba(0,0,0,0.5); z-index: 2001; transition: var(--transition-smooth); display: flex; flex-direction: column; border-left: 1px solid rgba(255,255,255,0.05); }
.cart-drawer.open { right: 0; }
.cart-header { padding: 1.5rem; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.05); }
.cart-items { flex: 1; overflow-y: auto; padding: 1.5rem; }
.cart-item { display: flex; gap: 15px; margin-bottom: 15px; background: rgba(255,255,255,0.02); padding: 10px; border-radius: 8px; align-items: center; }
.cart-item img { width: 60px; height: 60px; object-fit: cover; border-radius: 5px; }
.cart-item-details { flex: 1; }
.cart-item-title { font-weight: 500; font-size: 0.9rem; margin-bottom: 3px; color: var(--color-primary); }
.cart-item-price { color: var(--color-text-muted); font-size: 0.85rem; }
.cart-remove { color: #ff4d4f; cursor: pointer; padding: 5px; font-weight: bold; }
.cart-footer { padding: 1.5rem; border-top: 1px solid rgba(255,255,255,0.05); background: rgba(0,0,0,0.2); }
.cart-total { display: flex; justify-content: space-between; font-size: 1.2rem; font-weight: 600; margin-bottom: 1rem; color: var(--color-primary); }

/* Modals */
.modal-overlay { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.8); display: flex; align-items: center; justify-content: center; opacity: 0; pointer-events: none; transition: var(--transition-fast); z-index: 3000; }
.modal-overlay.active { opacity: 1; pointer-events: auto; }
.modal-content { background: var(--color-bg-panel); width: 90%; max-width: 500px; padding: 2.5rem; border-radius: 12px; box-shadow: var(--shadow-card); position: relative; border: 1px solid rgba(255,255,255,0.1); }
.modal-header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.05); padding-bottom: 1rem; margin-bottom: 1.5rem; }
.modal-close { cursor: pointer; font-size: 1.5rem; color: var(--color-text-muted); transition: 0.2s; }
.modal-close:hover { color: var(--color-primary); }

/* Payment Methods */
.payment-methods { display: flex; gap: 1rem; margin-bottom: 2rem; }
.pay-method { flex: 1; border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; padding: 1rem; text-align: center; cursor: pointer; transition: 0.2s; background: rgba(255,255,255,0.02); }
.pay-method:hover { border-color: var(--color-primary); }
.pay-method.active { border-color: var(--color-primary); background: rgba(212, 175, 55, 0.1); color: var(--color-primary); font-weight: bold; }
.pay-icon { font-size: 1.8rem; margin-bottom: 0.5rem; }

/* AI Widget */
.ai-widget { position: fixed; bottom: 30px; right: 30px; z-index: 1000; }
.ai-btn { width: 60px; height: 60px; border-radius: 50%; background: var(--color-primary); color: #111; display: flex; align-items: center; justify-content: center; font-size: 1.8rem; cursor: pointer; box-shadow: var(--shadow-glow); transition: var(--transition-smooth); animation: float 3s ease-in-out infinite; }
.ai-btn:hover { transform: scale(1.1); box-shadow: 0 0 30px rgba(212,175,55,0.6); }
.ai-chat-window { position: absolute; bottom: 80px; right: 0; width: 350px; background: var(--color-bg-panel); border-radius: 12px; box-shadow: var(--shadow-card); overflow: hidden; display: none; flex-direction: column; border: 1px solid rgba(255,255,255,0.1); }
.ai-chat-window.open { display: flex; animation: slideUp 0.3s ease; }
.ai-chat-header { background: rgba(255,255,255,0.05); padding: 15px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.05); }
.ai-title { font-weight: 600; font-family: var(--font-heading); color: var(--color-primary); }
.close-ai { cursor: pointer; color: var(--color-text-muted); }
.ai-messages { height: 300px; padding: 15px; overflow-y: auto; display: flex; flex-direction: column; gap: 10px; background: var(--color-bg-dark); }
.message { max-width: 80%; padding: 10px 15px; border-radius: 15px; font-size: 0.9rem; line-height: 1.4; }
.msg-ai { background: rgba(212,175,55,0.1); border-bottom-left-radius: 5px; color: var(--color-text); border: 1px solid rgba(212,175,55,0.2); }
.msg-user { background: var(--color-bg-card); align-self: flex-end; border-bottom-right-radius: 5px; color: var(--color-text); border: 1px solid rgba(255,255,255,0.05); }
.ai-input-area { padding: 15px; display: flex; gap: 10px; background: var(--color-bg-panel); border-top: 1px solid rgba(255,255,255,0.05); align-items:center; }
.ai-input { flex: 1; padding: 10px 15px; border: 1px solid rgba(255,255,255,0.1); border-radius: 20px; outline: none; background: var(--color-bg-dark); color: var(--color-text); justify-content:center; align-items:center;}
.ai-send { background: var(--color-primary); color: #111; border: none; width: 40px; height: 40px; border-radius: 50%; cursor: pointer; display: flex; align-items: center; justify-content: center; }
@keyframes float { 0% { transform: translateY(0); } 50% { transform: translateY(-10px); } 100% { transform: translateY(0); } }
@keyframes slideUp { from { transform: translateY(20px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }

/* Toast Notifications */
.toast-container { position: fixed; top: 80px; right: 20px; z-index: 5000; display: flex; flex-direction: column; gap: 10px; }
.toast { background: var(--color-bg-panel); color: var(--color-text); padding: 12px 20px; border-radius: 8px; box-shadow: var(--shadow-card); display: flex; align-items: center; gap: 10px; animation: slideInX 0.3s forwards; font-size: 0.9rem; border-left: 4px solid var(--color-primary); }
@keyframes slideInX { from { transform: translateX(100%); opacity:0; } to { transform: translateX(0); opacity:1; } }
@keyframes fadeOut { to { opacity: 0; } }

/* Inputs Base */
#forgot-email, .form-input, textarea, input[type="text"], input[type="email"], input[type="password"] {
    background: var(--color-bg-card);
    border: 1px solid rgba(255,255,255,0.1);
    color: var(--color-text);
    border-radius: 5px;
}
#forgot-email:focus, .form-input:focus, textarea:focus { border-color: var(--color-primary); outline: none; }

/* Search Suggestions */
#search-suggestions { position: absolute; top: calc(100% + 5px); left: 0; width: 100%; min-width:250px; background: var(--color-bg-panel); border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; z-index: 6000; box-shadow: var(--shadow-card); max-height: 300px; overflow-y: auto; display: none; }
.suggestion-item { padding: 10px 15px; display: flex; align-items: center; gap: 10px; cursor: pointer; border-bottom: 1px solid rgba(255,255,255,0.05); transition: var(--transition-fast); }
.suggestion-item:hover { background: rgba(255, 255, 255, 0.05); }
.suggestion-img { width: 40px; height: 40px; border-radius: 4px; object-fit: cover; }
.suggestion-info { flex: 1; }
.suggestion-title { font-size: 0.9rem; font-weight: bold; color: var(--color-primary); margin-bottom: 2px; }
.suggestion-price { font-size: 0.8rem; color: var(--color-text-muted); }


/* MOBILE RESPONSIVENESS FIX */
@media (max-width: 768px) {
    body, html { overflow-x: hidden; width: 100%; }
    .container { width: 95%; max-width: 100vw; padding: 0 10px; }
    
    /* Navbar Scaling & Visbility (DO NOT HIDE NAV LINKS) */
    .navbar .container { flex-direction: column; gap: 10px; text-align: center; }
    .nav-links { display: flex !important; flex-wrap: wrap; justify-content: center; gap: 10px; width: 100%; }
    .nav-actions { display: flex !important; flex-wrap: wrap; justify-content: center; gap: 10px; width: 100%; margin-top: 10px; }
    #global-search { width: 100%; max-width: none; }

    /* Fix Hero Headers so they fit */
    #home h1 { font-size: 2.2rem !important; margin-top: 40px; }
    
    /* Fix Sections and Grids padding */
    .section { padding: 50px 0 !important; }
    .menu-categories { flex-wrap: wrap; justify-content: center; }
    .menu-categories .btn { width: 100%; }
    
    /* Ensure About Section / Contact Section flex stacks correctly */
    #about .container, #contact .container { flex-direction: column !important; text-align: center; }
    #about img { width: 100%; height: auto; }
    #contact .btn { width: 100%; margin-top: 10px; }

    /* Modals Scaling */
    .modal-content { max-width: 95%; width: 100%; padding: 1.5rem; text-align: center; }

    #loc-btn-calabar, #loc-btn-uyo { width: 50%; font-size: 0.9rem; padding: 10px; }
}

@media (max-width: 480px) {
    #home h1 { font-size: 1.8rem !important; }
    .product-card { padding: 15px; }
    .ai-chat-window { width: 90vw; right: 5vw; }
}
'''

open('css/styles.css', 'w', encoding='utf-8').write(clean_css)
