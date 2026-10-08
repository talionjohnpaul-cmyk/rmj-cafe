import streamlit as st

# ==========================================
# 1. PAGE CONFIGURATION & CUSTOM STYLING (CSS)
# ==========================================
st.set_page_config(
    page_title="RMJ Cafe | Freshly Brewed Happiness",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #1a1615;
        color: #f4eae1;
    }
    h1, h2, h3 {
        color: #d4a373 !important;
        font-family: 'Trebuchet MS', sans-serif;
    }
    div[data-testid="stMetricValue"] {
        color: #e76f51 !important;
    }
    .stButton>button {
        background-color: #d4a373;
        color: #1a1615;
        font-weight: bold;
        border-radius: 8px;
        border: none;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #e76f51;
        color: #ffffff;
    }
    section[data-testid="stSidebar"] {
        background-color: #2b2320;
    }
    .badge {
        background-color: #e76f51;
        color: white;
        padding: 4px 8px;
        border-radius: 12px;
        font-size: 12px;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize Session State
if 'cart' not in st.session_state:
    st.session_state.cart = []

# ==========================================
# 2. MENU DATA
# ==========================================
menu_items = [
    {"name": "RMJ Signature Espresso", "category": "Coffee", "price": 140, "desc": "Rich double-shot espresso with secret velvet cream.", "img": "https://images.unsplash.com/photo-1510591509098-f4fdc6d0ff04?w=500"},
    {"name": "Spanish Latte", "category": "Coffee", "price": 165, "desc": "Espresso mixed with sweet textured milk.", "img": "https://images.unsplash.com/photo-1541167760496-1628856ab772?w=500"},
    {"name": "Caramel Macchiato", "category": "Coffee", "price": 175, "desc": "Fresh steamed milk with vanilla-flavored syrup and caramel drizzle.", "img": "https://images.unsplash.com/photo-1485808191679-5f86510681a2?w=500"},
    {"name": "Brown Sugar Milk Tea", "category": "Milk Tea", "price": 130, "desc": "Classic black tea with creamy milk and caramelized brown sugar pearls.", "img": "https://images.unsplash.com/photo-1558857563-b371033873b8?w=500"},
    {"name": "Taro Pearl Milk Tea", "category": "Milk Tea", "price": 135, "desc": "Rich taro root flavor paired with chewy tapioca pearls.", "img": "https://images.unsplash.com/photo-1525385133512-2f3bdd039054?w=500"},
    {"name": "Flaky Butter Croissant", "category": "Pastries", "price": 95, "desc": "French-style golden pastry baked fresh every morning.", "img": "https://images.unsplash.com/photo-1555507036-ab1f4038808a?w=500"},
    {"name": "Dark Chocolate Muffin", "category": "Pastries", "price": 110, "desc": "Decadent cocoa muffin packed with chocolate chunks.", "img": "https://images.unsplash.com/photo-1607958996333-41aef7caefaa?w=500"},
    {"name": "Creamy Carbonara", "category": "Pasta", "price": 220, "desc": "Rich parmesan sauce, crispy bacon, and freshly grated pepper.", "img": "https://images.unsplash.com/photo-1612874742237-6526221588e3?w=500"}
]

# ==========================================
# 3. SIDEBAR NAVIGATION & CART
# ==========================================
with st.sidebar:
    st.title("☕ RMJ Cafe")
    st.write("*Freshly Brewed Happiness*")
    st.write("---")
    
    page = st.radio("Pumili ng Pahina:", ["🏠 Home & Menu", "🧮 Event Estimator", "📬 Contact Us"])
    
    st.write("---")
    st.header("🛒 Shopping Cart")
    
    if len(st.session_state.cart) == 0:
        st.info("Wala pang laman ang cart mo.")
    else:
        total_price = 0
        for idx, item in enumerate(st.session_state.cart):
            col1, col2 = st.columns([3, 1])
            col1.write(f"• **{item['name']}** - ₱{item['price']}")
            total_price += item['price']
            if col2.button("❌", key=f"del_{idx}"):
                st.session_state.cart.pop(idx)
                st.rerun()
                
        st.write("---")
        st.markdown(f"### **Total: ₱{total_price}**")
        
        if st.button("🚀 Checkout Orders", use_container_width=True):
            st.balloons()
            st.success("Salamat sa order! Inihahanda na ng RMJ Cafe ang inyong order.")
            st.session_state.cart = []

# ==========================================
# 4. MAIN PAGE CONTENT
# ==========================================

# ----------------- PAGE 1: HOME & MENU -----------------
if page == "🏠 Home & Menu":
    st.title("Welcome to RMJ Cafe ☕")
    st.caption("Tikman ang pinakamasarap na kape at pastry sa lungsod!")
    
    st.image("https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?w=1200", use_container_width=True)
    
    st.write("---")
    
    st.subheader("📜 Our Menu")
    categories = ["All", "Coffee", "Milk Tea", "Pastries", "Pasta"]
    selected_cat = st.selectbox("I-filter ayon sa kategorya:", categories)
    
    filtered_items = [item for item in menu_items if selected_cat == "All" or item['category'] == selected_cat]
    
    cols = st.columns(2)
    for idx, item in enumerate(filtered_items):
        with cols[idx % 2]:
            st.image(item['img'], use_container_width=True)
            st.markdown(f"### {item['name']}")
            st.markdown(f"<span class='badge'>{item['category']}</span> **₱{item['price']}**", unsafe_allow_html=True)
            st.write(item['desc'])
            
            if st.button(f"➕ Add to Cart - ₱{item['price']}", key=f"btn_{item['name']}"):
                st.session_state.cart.append(item)
                st.toast(f"Naidagdag ang {item['name']} sa cart!", icon="🛒")
                st.rerun()
            st.write("---")

# ----------------- PAGE 2: EVENT ESTIMATOR -----------------
elif page == "🧮 Event Estimator":
    st.title("🎉 Party & Catering Estimator")
    st.write("Plano mo bang magpa-book o mag-party sa RMJ Cafe? Gamitin ang calculator sa ibaba para malaman ang tantyang gastos!")
    
    pax = st.slider("Ilang tao ang dadalo? (Number of Guests)", min_value=5, max_value=100, value=20, step=5)
    
    package = st.radio("Pumili ng Package:", [
        "Basic (1 Beverage + 1 Pastry per head)",
        "Premium (1 Beverage + 1 Pasta + 1 Pastry per head)",
        "VIP Exclusive Cafe Rental (Unli-Coffee + Full Meals + Whole Venue Access)"
    ])
    
    rate_per_head = 220
    if "Premium" in package:
        rate_per_head = 380
    elif "VIP" in package:
        rate_per_head = 650
        
    estimated_total = pax * rate_per_head
    
    st.write("---")
    st.subheader("📊 Estimated Cost Summary")
    st.metric(label="Total Guests", value=f"{pax} pax")
    st.metric(label="Estimated Total Cost", value=f"₱{estimated_total:,.2f}")
    
    st.info("💡 Ang presyong ito ay tantya pa lamang. Makipag-ugnayan sa amin sa Contact Page para sa opisyal na reservation.")

# ----------------- PAGE 3: CONTACT US -----------------
elif page == "📬 Contact Us":
    st.title("📬 Contact RMJ Cafe")
    st.write("May mga katanungan ka ba o gustong mag-reserve? Mag-iwan ng mensahe!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.form("contact_form"):
            name = st.text_input("Pangalan:")
            email = st.text_input("Email:")
            msg = st.text_area("Mensahe:")
            submitted = st.form_submit_button("Ipadala ang Mensahe")
            
            if submitted:
                if name and email and msg:
                    st.success(f"Salamat {name}! Natanggap na ng RMJ Cafe ang iyong mensahe.")
                else:
                    st.error("Paki-punan ang lahat ng field sa form.")
                    
    with col2:
        st.subheader("📍 Saan kami matatagpuan?")
        st.write("🏢 **RMJ Cafe Building**, Main Street, City Center")
        st.write("⏰ **Operating Hours:** 8:00 AM - 10:00 PM (Lunes hanggang Linggo)")
        st.write("📞 **Phone:** (02) 8123-4567 / 0917-123-4567")
        st.write("✉️ **Email:** hello@rmjcafe.com")