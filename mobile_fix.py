import os

os.chdir(r'c:\Users\USER\Desktop\anti-gravity')

css = open('css/styles.css', 'r', encoding='utf-8').read()

new_mobile_layer = '''
/* Aggressive Mobile Responsiveness Core Layer */
@media (max-width: 768px) {
    /* Prevent any horizontal scrolling globally */
    html, body { 
        max-width: 100vw; 
        overflow-x: hidden !important; 
        width: 100%; 
        padding: 0; 
        margin: 0; 
    }
    
    /* Ensure containers never break bounds */
    .container { 
        width: 100% !important; 
        padding: 0 15px !important; 
        box-sizing: border-box !important; 
        margin: 0 auto !important; 
    }
    
    /* Scale all text and massive headers down */
    #home h1 { font-size: 2rem !important; line-height: 1.2 !important; word-wrap: break-word; }
    h2 { font-size: 1.8rem !important; word-wrap: break-word; }
    p { font-size: 0.95rem !important; }
    
    /* Ensure grids and flex rows aggressively wrap */
    section > .container > div, .menu-categories { 
        flex-direction: column !important; 
        align-items: center !important; 
        width: 100% !important; 
    }
    
    /* Resize Navigation to fit exactly */
    .navbar .container { gap: 15px !important; }
    .nav-actions { 
        width: 100% !important; 
        display: flex !important;
        flex-direction: row !important;
        justify-content: space-between !important; 
        flex-wrap: wrap !important;
        gap: 10px !important;
    }
    
    /* Soften the search bar constraints */
    #global-search { 
        width: 100% !important; 
        max-width: 200px !important; 
    }
    
    /* Stack components cleanly */
    .product-card, .glass { 
        width: 100% !important; 
        box-sizing: border-box !important; 
        margin-bottom: 20px !important; 
    }
    
    .menu-categories .btn { width: 100% !important; margin-bottom: 5px !important; }

    /* Fix image and form breaking bounds */
    img, video, iframe, input, textarea { 
        max-width: 100% !important; 
        box-sizing: border-box !important; 
    }
    
    /* Fix Hero spacing */
    #home .container div[style*="display:flex"] { 
        flex-direction: column !important; 
        gap: 10px !important; 
    }
}
'''

# If the old simple layer was added in wave9 execution, remove it to prevent collision
if '/* Mobile Responsiveness Layer */' in css:
    css = css.split('/* Mobile Responsiveness Layer */')[0]
    
css += new_mobile_layer

open('css/styles.css', 'w', encoding='utf-8').write(css)
