from flask import Flask, request
import requests

app = Flask(__name__)

# Ye tera auto-reply ka dimagh hai - Hafiz ke kaam ke hisab se
def get_reply(msg):
    msg = msg.lower()
    if "salam" in msg or "hello" in msg or "hi" in msg:
        return "Wa Alaikum Salam Hero! 🤖 Me Hafiz Naveed ka AI Agent hun.\n\n1. Website banwani hai?\n2. Fridge/Dispenser Repair?\n3. Fees puchni hai?\n\nKya likho?"
    elif "website" in msg:
        return "G haan! Hafiz Website banata hai ✅\nJacobabad ke Clinics, Shops, Restaurants ke liye.\n\n- Portfolio Website: 5000 Rs\n- Booking/Order wali: 10000 Rs\n- Free Sample available\n\nApni shop ka naam bhejo, demo bana dun?"
    elif "fridge" in msg or "refrigerator" in msg or "dispenser" in msg or "ac" in msg:
        return "Fridge / AC / Dispenser Repair ❄️\nHafiz Ustaad - Home Service Jacobabad.\n\nMasla kya hai? Thanda nahi kar raha ya pani nahi de raha? Location bhejo."
    elif "fees" in msg or "price" in msg or "kitne" in msg or "paisa" in msg:
        return "Fees List:\nPortfolio = 5000\nBooking Website = 10000\nFull Business Website = 15000\n\nSab mobile friendly aur WhatsApp connected hogi."
    elif "hafiz" in msg:
        return "Me Hafiz Naveed ka AI Agent hun 👨‍💻\nHafiz-e-Quran | DIT | Website Developer | Fridge Technician\nIT Track, Jacobabad. Aap ko kya kaam hai?"
    else:
        return "Samajh nahi aaya Hero. 🤔\nLikho:\n'Website' - website ke liye\n'Fridge' - repair ke liye\n'Fees' - price ke liye"

@app.route("/", methods=["GET"])
def home():
    return "Hafiz AI Agent is Running! WhatsApp ke liye /webhook use karo"

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        # Meta verification ke liye
        return request.args.get("hub.challenge")
    
    data = request.json
    try:
        # Message nikalna
        msg = data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
        from_number = data['entry'][0]['changes'][0]['value']['messages'][0]['from']
        
        reply = get_reply(msg)
        
        # Yahan WhatsApp API se wapis bhejna hai (Token lagana hoga)
        print(f"User: {msg} -> Reply: {reply}")
        # TODO: yahan apna WHATSAPP_TOKEN lagana
        
        return "ok", 200
    except:
        return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
