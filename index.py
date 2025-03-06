import re
import streamlit as st

# password strength meter checker
# Add title
st.set_page_config(page_title="🔐 Password Strength Meter", layout="wide")
st.header("🔐 Password Strength Meter")
st.write("Password is the key to your account. Make it strong, unique, and difficuilt to guess to keep your information protected!🔒🔑")
def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
       feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # Strength Rating
    if score == 4:
      st.success("✅ Strong Password!")
    elif score == 3:
      st.info("⚠️ Moderate Password - Consider adding more security features.")
    else:
      st.error("❌ Weak Password - Improve it using the suggestions above.")

    if feedback:
      with st.expander("Imporve your password🛡️🔐"):
         for item in feedback:
            st.write(item)

# Get user input
password = st.text_input("Enter your password : ",type="password", key="Passcode")
if st.button("Check your passcode strength🛡️"):
    if password:
       check_password_strength(password)
    else:
     st.warning("Enter the password first🔴")

confirm_password = st.text_input("Confirm your password:", type="password",key="confirm_password")
if st.button("confirm🔏✔️"):
     if password == confirm_password:
      st.success("✅ Passwords match!")
     else:
            st.warning("❌ Passwords do not match. Please try again.")
