import os

js = open('js/app.js', 'r', encoding='utf-8').read()

new_logic = '''window.sendAIMessage = function() {
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
        
        let customAction = false;
        
        // Cart Auto-Add Intent Check
        if(lowMsg.includes('add') || lowMsg.includes('order') || lowMsg.includes('want')) {
            if(lowMsg.includes('extra') && lowMsg.includes('shawarma')) {
                addToCart('Extra-special Shawarma', 6000, 'assets/images/shawarma.png');
                response = "Success: I've added an Extra-Special Shawarma into your cart!";
                customAction = true;
            } else if(lowMsg.includes('special') && lowMsg.includes('shawarma')) {
                 addToCart('Special Shawarma', 5500, 'assets/images/shawarma.png');
                 response = "Success: I've placed a Special Shawarma in your cart.";
                 customAction = true;
            } else if(lowMsg.includes('shawarma')) {
                addToCart('Regular Shawarma', 4900, 'assets/images/shawarma.png');
                response = "Success: One Regular Shawarma added to your cart instantly!";
                customAction = true;
            } else if(lowMsg.includes('2 liter') && lowMsg.includes('parfait')) {
                addToCart('2 Liter Classic Parfait', 26500, 'assets/images/parfait.png');
                response = "Success: Added the massive 2 Liter Classic Parfait to your cart!";
                customAction = true;
            } else if(lowMsg.includes('parfait')) {
                addToCart('Regular Parfait', 3500, 'assets/images/parfait.png');
                response = "Success: I've added a Regular Parfait into your shopping cart for you.";
                customAction = true;
            }
        }
        
        if(!customAction) {
            if(lowMsg.includes('shawarma')) response = "Our Extra-special Shawarma goes for ₦6,000 and is packed with double meat! Say 'add extra shawarma' to place it in your cart.";
            else if(lowMsg.includes('parfait')) response = "We offer luxury parfaits starting from ₦2,500 up to 2 Liters at ₦33,000. Just tell me to 'add a parfait'!";
            else if(lowMsg.includes('price')) response = "Our prices range from ₦2,500 for a Mini Parfait up to ₦6,000 for the Extra-Special Shawarma.";
            else if(lowMsg.includes('hello') || lowMsg.includes('hi')) response = "Hello! Welcome to South Cafe. What are you craving today?";
        }

        messagesContainer.innerHTML += `<div class="message msg-ai">${response}</div>`;
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }, 1000);
}'''

start = js.find('window.sendAIMessage = function()')
end = js.find('window.startVoiceAI = function()')
if start != -1 and end != -1:
    js = js[:start] + new_logic + '\n\n' + js[end:]
    open('js/app.js', 'w', encoding='utf-8').write(js)
