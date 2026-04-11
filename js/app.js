// Application Logic - Wave 2 (Wallet, Toasts, Advanced AI)

// --- STATE MANAGEMENT ---
const currentUser = localStorage.getItem('southcafe_user');
let walletBalance = parseFloat(localStorage.getItem('southcafe_wallet') || '0');
let cart = JSON.parse(localStorage.getItem('southcafe_cart')) || [];
let cartTotalNumeric = 0;

// --- TOAST NOTIFICATIONS ---
function showToast(message, type = 'success') {
    const container = document.getElementById('toast-container') || createToastContainer();
    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.innerHTML = `<span>${type === 'success' ? '✓' : '⚠️'}</span> ${message}`;
    container.appendChild(toast);
    
    setTimeout(() => {
        toast.style.animation = 'fadeOut 0.3s forwards';
        setTimeout(() => toast.remove(), 300);
    }, 4000);
}

function createToastContainer() {
    const container = document.createElement('div');
    container.id = 'toast-container';
    container.className = 'toast-container';
    document.body.appendChild(container);
    return container;
}

// Check for Welcome Message
if (window.location.search.includes('newuser=true')) {
    setTimeout(() => {
        showToast("Welcome to South Cafe! We've sent a special offer to your email.", "success");
        history.replaceState(null, '', window.location.pathname);
    }, 500);
}

// --- AUTH & WALLET UI ---
const loginBtn = document.getElementById('nav-login-btn');

function updateAuthUI() {
    if(loginBtn) {
        if (currentUser) {
            const formattedBalance = new Intl.NumberFormat('en-NG', { style: 'currency', currency: 'NGN' }).format(walletBalance);
            loginBtn.innerHTML = `
                <a href="wallet.html" class="wallet-badge">👛 ${formattedBalance}</a>
                <span style="font-size:0.85rem; margin-left:15px; color:var(--color-primary);">Hi, ${currentUser}</span>
                <span style="cursor:pointer; margin-left:10px; color:#a1a1aa; font-size:0.8rem;" id="logout-btn">(Logout)</span>
            `;
            document.getElementById('logout-btn')?.addEventListener('click', () => {
                localStorage.removeItem('southcafe_user');
                showToast("Logged out successfully.");
                setTimeout(() => window.location.reload(), 1000);
            });
        } else {
            loginBtn.innerHTML = `<a href="login.html" class="btn btn-outline" style="padding: 0.5rem 1.5rem">Login</a>`;
        }
    }
}
updateAuthUI();

// --- CHECKOUT & PAYMENTS ---
let activePaymentMethod = 'wallet';

window.openCheckout = function() {
    if(cart.length === 0) {
        showToast("Your cart is empty!", "error");
        return;
    }
    if(!currentUser) {
        showToast("Please login to checkout.", "error");
        setTimeout(() => window.location.href = 'login.html', 1500);
        return;
    }
    toggleCart(false);
    document.getElementById('checkout-modal').classList.add('active');
    document.getElementById('checkout-amount').innerText = new Intl.NumberFormat('en-NG', { style: 'currency', currency: 'NGN' }).format(cartTotalNumeric);
}

window.closeCheckout = function() {
    document.getElementById('checkout-modal').classList.remove('active');
}

window.selectPaymentMethod = function(method) {
    activePaymentMethod = method;
    document.querySelectorAll('.pay-method').forEach(el => el.classList.remove('active'));
    document.getElementById('pay-' + method).classList.add('active');
    
    // UI changes based on method
    const btn = document.getElementById('confirm-payment-btn');
    if(method === 'wallet') btn.innerText = "Pay via Wallet";
    if(method === 'paystack') btn.innerText = "Proceed to Paystack";
    if(method === 'transfer') btn.innerText = "I have made the Transfer";
}

window.confirmPayment = function(e) {
    e.preventDefault();
    const btn = document.getElementById('confirm-payment-btn');
    btn.innerText = "Processing Transaction...";
    btn.style.opacity = "0.7";
    
    setTimeout(() => {
        if(activePaymentMethod === 'wallet') {
            if(walletBalance >= cartTotalNumeric) {
                // Deduct balance
                walletBalance -= cartTotalNumeric;
                localStorage.setItem('southcafe_wallet', walletBalance);
                
                // Empty the cart
                cart = [];
                updateCartUI();
                updateAuthUI();
                closeCheckout();
                
                // Show huge success
                const amountFormatted = new Intl.NumberFormat('en-NG', { style: 'currency', currency: 'NGN' }).format(cartTotalNumeric);
                alert(`SUCCESS: Payment of ${amountFormatted} was deducted from your South Wallet! Your order is on its way.`);
                showToast("Payment successful! Your order is being prepared.", "success");
            } else {
                alert("ERROR: Insufficient wallet balance. Please top up your wallet first.");
                showToast("Insufficient wallet balance. Please top up.", "error");
            }
        } else if(activePaymentMethod === 'paystack' || activePaymentMethod === 'transfer') {
            cart = [];
            updateCartUI();
            closeCheckout();
            alert("SUCCESS: Payment confirmed! Order placed.");
            showToast("Payment confirmed. Order placed.", "success");
        }
        
        btn.innerText = "Confirm Payment";
        btn.style.opacity = "1";
    }, 1500);
}


// --- CART LOGIC ---
function updateCartUI() {
    const badge = document.getElementById('cart-badge');
    const cartItemsContainer = document.getElementById('cart-items');
    const cartTotalEl = document.getElementById('cart-total-price');
    
    if(badge) badge.innerText = cart.length;
    
    if(cartItemsContainer) {
        cartItemsContainer.innerHTML = '';
        cartTotalNumeric = 0;
        
        if (cart.length === 0) {
            cartItemsContainer.innerHTML = '<p style="color:var(--color-text-muted); text-align:center; margin-top:2rem;">Your cart is empty.</p>';
        } else {
            cart.forEach((item, index) => {
                cartTotalNumeric += item.price;
                const priceFormatted = new Intl.NumberFormat('en-NG', { style: 'currency', currency: 'NGN' }).format(item.price);
                cartItemsContainer.innerHTML += `
                    <div class="cart-item">
                        <img src="${item.image}" alt="${item.name}">
                        <div class="cart-item-details">
                            <div class="cart-item-title">${item.name}</div>
                            <div class="cart-item-price">${priceFormatted}</div>
                        </div>
                        <div class="cart-remove" onclick="removeFromCart(${index})">✕</div>
                    </div>
                `;
            });
        }
        
        if(cartTotalEl) {
            cartTotalEl.innerText = new Intl.NumberFormat('en-NG', { style: 'currency', currency: 'NGN' }).format(cartTotalNumeric);
        }
    }
    
    localStorage.setItem('southcafe_cart', JSON.stringify(cart));
}

window.addToCart = function(name, price, image) {
    cart.push({ name, price: parseInt(price), image });
    updateCartUI();
    showToast(`Added ${name} to cart.`);
    toggleCart(true);
}

window.removeFromCart = function(index) {
    cart.splice(index, 1);
    updateCartUI();
}

window.toggleCart = function(forceOpen = 'toggle') {
    const overlay = document.getElementById('cart-overlay');
    const drawer = document.getElementById('cart-drawer');
    if(!overlay || !drawer) return;
    
    if (forceOpen === true) {
        overlay.classList.add('open');
        drawer.classList.add('open');
    } else if (forceOpen === false) {
        overlay.classList.remove('open');
        drawer.classList.remove('open');
    } else {
        overlay.classList.toggle('open');
        drawer.classList.toggle('open');
    }
}

// --- AI LOGIC ---
window.toggleAI = function() {
    document.getElementById('ai-chat-window').classList.toggle('open');
}

window.sendAIMessage = function() {
    const input = document.getElementById('ai-message-input');
    const msg = input.value.trim();
    if(!msg) return;
    
    const messagesContainer = document.getElementById('ai-messages');
    messagesContainer.innerHTML += `<div class="message msg-user">${msg}</div>`;
    input.value = '';
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
    
    setTimeout(() => {
        let response = "I am South AI! How can I help you customize your parfait today?";
        const lowMsg = msg.toLowerCase();
        
        if(lowMsg.includes('shawarma')) response = "Our Extra-special Shawarma goes for ₦6,000 and is packed with double meat and sausage! Would you like me to add it to your cart?";
        else if(lowMsg.includes('parfait')) response = "We offer Mini, Regular, and Large parfaits starting from ₦2,500. They contain fresh yogurt, fruits, and organic granola.";
        else if(lowMsg.includes('price')) response = "Our prices range from ₦2,500 for a Mini Parfait up to ₦6,000 for the Extra-Special Shawarma.";
        else if(lowMsg.includes('hello') || lowMsg.includes('hi')) response = "Hello! Welcome to South Cafe. What are you craving today?";

        messagesContainer.innerHTML += `<div class="message msg-ai">${response}</div>`;
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }, 1000);
}

// UI AI Profiler
window.startVoiceAI = function() {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if(!SpeechRecognition) {
        showToast("Voice AI not supported in your current browser.", "error");
        return;
    }
    const recognition = new SpeechRecognition();
    recognition.lang = 'en-US';
    recognition.interimResults = false;
    
    const input = document.getElementById('ai-message-input');
    
    recognition.onstart = function() {
        input.placeholder = "Listening... Speak now 🎤";
    };
    
    recognition.onsuccess = function(event) {
        const transcript = event.results[0][0].transcript;
        input.value = transcript;
        input.placeholder = "Type here...";
        sendAIMessage(); // automatically send
    };
    
    recognition.onerror = function(event) {
        input.placeholder = "Type here...";
        showToast("Voice recognition error: " + event.error, "error");
    };
    
    recognition.start();
}

window.runAIProfiler = function() {
    const mood = document.getElementById('profiler-input').value;
    const resultEl = document.getElementById('profiler-result');
    if(!mood) { resultEl.innerText = "Please tell me how you feel first!"; return; }
    
    resultEl.innerHTML = `<span style="color:#fff;">Analyzing your mood...</span>`;
    setTimeout(() => {
        const text = mood.toLowerCase();
        let suggestion = "A **Regular Parfait** and **Extra-Special Shawarma** combo to balance your energy!";
        if(text.includes('sad') || text.includes('tired')) suggestion = "A **Large Luxury Parfait** loaded with chocolate and honey to instantly boost your mood!";
        if(text.includes('hungry')) suggestion = "Our **Extra-Special Shawarma** and a **Cold Zobo** to completely satisfy your cravings.";
        if(text.includes('happy') || text.includes('good')) suggestion = "Celebrate with a **Special Shawarma** and a **Tropical Smoothie**!";
        
        resultEl.innerHTML = `✨ South AI Suggests: <br> ${suggestion} <br> <a href="menu.html" style="color:#fff; text-decoration:underline;">Order Now</a>`;
    }, 1200);
}

// Menu Filter Logic
function initMenuFilters() {
    const filterBtns = document.querySelectorAll('.filter-btn');
    const products = document.querySelectorAll('.product-card');

    if (filterBtns.length > 0) {
        filterBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                // Remove active from all
                filterBtns.forEach(b => b.classList.remove('active'));
                // Add active to current
                btn.classList.add('active');
                
                const filterValue = btn.innerText.toLowerCase();

                products.forEach(product => {
                    const category = product.getAttribute('data-category');
                    if (filterValue === 'all') {
                        product.style.display = 'block';
                    } else if (category === filterValue) {
                        product.style.display = 'block';
                    } else {
                        product.style.display = 'none';
                    }
                });
            });
        });
    }
}

document.addEventListener('DOMContentLoaded', () => {
    updateCartUI();
    initMenuFilters();
});


// --- ADDED IN WAVE 3: LOGIC ---

// Theme Logic
function toggleTheme() {
    const root = document.documentElement;
    if (root.getAttribute('data-theme') === 'light') {
        root.removeAttribute('data-theme');
        localStorage.setItem('southcafe_theme', 'dark');
        showToast('Switched to Dark Mode', 'success');
    } else {
        root.setAttribute('data-theme', 'light');
        localStorage.setItem('southcafe_theme', 'light');
        showToast('Switched to Light Mode', 'success');
    }
}
if(localStorage.getItem('southcafe_theme') === 'light') document.documentElement.setAttribute('data-theme', 'light');

// Location Logic
function updateMapUI(val) {
    const cityEl = document.getElementById('display-city');
    const addressEl = document.getElementById('display-address');
    const iframe = document.getElementById('map-iframe');
    
    if(cityEl && addressEl && iframe) {
        if(val === 'Uyo') {
            cityEl.innerText = 'Uyo';
            addressEl.innerHTML = 'Oron Road, Uyo, Akwa Ibom State, Nigeria. <br>Mon - Sun: 10:00 AM - 11:00 PM <br><strong style="color:#fff;">+234 802 850 5626</strong>';
            iframe.src = 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d31742.666996614134!2d7.8967963!3d5.0315357!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x105d5b0000000000%3A0x0!2sUyo%2C%20Nigeria!5e0!3m2!1sen!2sus!4v1700000000001';
        } else {
            cityEl.innerText = 'Calabar';
            addressEl.innerHTML = 'Marian Road, Calabar, Cross River State, Nigeria. <br>Mon - Sun: 10:00 AM - 11:00 PM <br><strong style="color:#fff;">+234 802 850 5626</strong>';
            iframe.src = 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d15893.303350410656!2d8.3303862!3d4.9583155!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x1067863dd252c71f%3A0xeab5e83c65e84898!2sMarian%20Rd%2C%20Calabar%2C%20Nigeria!5e0!3m2!1sen!2sus!4v1700000000000';
        }
    }
}

function changeLocation(val) {
    localStorage.setItem('southcafe_location', val);
    showToast('Location seamlessly updated to ' + val + '.', 'success');
    updateMapUI(val);
}
document.addEventListener('DOMContentLoaded', () => {
    const loc = localStorage.getItem('southcafe_location');
    if(loc) {
        document.querySelectorAll('#location-select').forEach(el => el.value = loc);
        updateMapUI(loc);
    }
});
// Search Filter Logic
window.searchProducts = function() {
    const val = document.getElementById('global-search').value.toLowerCase();
    const products = document.querySelectorAll('.product-card');
    
    if(products.length === 0) {
        if(window.event && window.event.key === 'Enter') {
            window.location.href = 'menu.html?search=' + encodeURIComponent(val);
        }
        return;
    }
    
    // De-activate filter buttons if user searches
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    
    products.forEach(product => {
        const title = product.querySelector('.product-title').innerText.toLowerCase();
        if(title.includes(val)) {
            product.style.display = 'block';
        } else {
            product.style.display = 'none';
        }
    });
}

// Intercept search queries from redirects
document.addEventListener('DOMContentLoaded', () => {
    const urlParams = new URLSearchParams(window.location.search);
    if(urlParams.has('search')) {
        const query = urlParams.get('search');
        const searchInput = document.getElementById('global-search');
        if(searchInput) {
            searchInput.value = query;
            setTimeout(() => window.searchProducts(), 200);
        }
    }
});
