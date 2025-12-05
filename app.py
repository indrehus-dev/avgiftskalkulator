import streamlit as st
import math

def calc_from_gross(gross):
    if gross is None:
        return None, None
    # Fee = 10% of gross, min 25, max 55
    fee = min(max(0.10 * gross, 25), 55)
    net = gross - fee
    return fee, net

def calc_from_net(net):
    if net is None:
        return None, None
    
    if net < 225:
        gross = net + 25
    elif net <= 495:
        gross = net / 0.9
    else:
        gross = net + 55
        
    fee = gross - net
    return fee, gross

def format_currency(value):
    if value is None:
        return "–"
    return f"{round(value):,} kr".replace(",", " ")

st.set_page_config(page_title="Billettavgiftskalkulator – Ælvespeilet", layout="centered")

st.title("Billettavgiftskalkulator – Ælvespeilet")
st.markdown("""
Avgift = **10 %** av utsalgspris (inkl. avgift), **min. 25 kr**, **maks. 55 kr**. 
Beregningene avrundes til nærmeste krone.
""")

col1, col2 = st.columns(2)

with col1:
    st.header("1) Utsalgspris")
    st.caption("(inkl. avgift)")
    
    gross_input = st.number_input("Utsalgspris", min_value=0.0, step=1.0, format="%.2f", key="gross_input")
    
    if gross_input:
        fee, net = calc_from_gross(gross_input)
        
        st.metric("Billettavgift", format_currency(fee))
        st.metric("Pris eks. avgift", format_currency(net))
        
    st.caption("Eksempler: 200 → 25 kr · 500 → 50 kr · 600 → 55 kr")

with col2:
    st.header("2) Pris eks. avgift")
    st.caption("(netto)")
    
    net_input = st.number_input("Pris eks. avgift", min_value=0.0, step=1.0, format="%.2f", key="net_input")
    
    if net_input:
        fee, gross = calc_from_net(net_input)
        
        st.metric("Pris inkl. avgift", format_currency(gross))
        st.metric("Billettavgift", format_currency(fee))

    st.caption("Logikk: <225 → +25 kr · 225–495 → /0,9 · >495 → +55 kr")


import os

# ... rest of imports ...

# At the bottom of the file
st.markdown("---")
st.caption("© Kulturhuset Ælvespeilet")

image_filename = "QR_avgiftskalkulator.jpg"
current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, image_filename)

if os.path.exists(image_path):
    st.image(image_path, width=150)
else:
    st.error(f"Finner ikke bildefilen: {image_filename}. Sjekk at filen ligger i samme mappe som app.py.")
