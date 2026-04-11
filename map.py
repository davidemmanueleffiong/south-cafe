import os

new_func = '''// Location Logic
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
'''

os.chdir(r'c:\Users\USER\Desktop\anti-gravity')
js = open('js/app.js', 'r', encoding='utf-8').read()

start = js.find('// Location Logic')
if start != -1:
    end = js.find('// Search Filter Logic', start)
    js = js[:start] + new_func + js[end:]
    open('js/app.js', 'w', encoding='utf-8').write(js)
