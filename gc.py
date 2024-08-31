
import streamlit as st
import random
import time

pt = st.markdown('<h2 style="font-size: 36px; font-weight: bold;">रुको ज़रा, सब्र करो</h2>', unsafe_allow_html=True)
with st.spinner(''):
    time.sleep(2)
pt.empty()
    
# Initialize attempt counter
a = st.session_state.get('av', 0)
c = st.session_state.get('cv', random.randint(1, 100))  # Random number to guess

# Streamlit UI elements
st.title(f"Your Welcome!  आपका स्वागत है।")
st.title(f"     Can You Guess?          ")
st.subheader(f"Mai Ansh hu Apka Player Maine 1 se 100 ke bich ek number liya hai. Kya Aap us number ko guess kar sakte HaI?")
st.success(f"Your {a + 1}/10 attempts are completed. आपके {a + 1}/10 प्रयास समाप्त हो चुके हैं।"  )

# Number input
n = st.number_input("Enter your guess. अपना गेस दर्ज करें:",min_value=1,max_value=100,step=1)

# Guess button
if st.button("Guess गेस करें"):
    a += 1  # Increment the attempt counter

    if n > c:
        st.warning("Oh! You entered a big number.Please enter a small number. अरे! आपने एक बड़ा नंबर एंटर किया है। कृपया एक छोटा नंबर एंटर करें।")
    elif n < c:
        st.warning("Oh! You entered a small number.Please enter a big number.अरे! आपने एक छोटा नंबर एंटर किया है। कृपया एक बड़ा नंबर एंटर करें।")
    else:
        st.success(f"WOW! You guessed the number correctly in {a} guesses. I was taken {c}. वाह! आपने सही नंबर {a} प्रयासों में गेस किया। मैंने {c} लिया था।")
        st.balloons()  # Show balloons if the user guesses correctly
        st.session_state.clear()  # Clear session state to reset the game

    # Update session state
    st.session_state['av'] = a
    st.session_state['cv'] = c

if a == 10:  # Check if the number of attempts is 10
    st.error(f"Sorry! Aapke 10 attempts khatam ho gaye. Sahi number {c} tha.")
    st.snow()
    st.session_state.clear() 

st.progress(100)
st.header(f" What is Can you Guess?     ")
st.subheader(f"It is an amazing game in which computer take a random number beetween 1 to 100 and user have to guess it.")
st.header(f'Can you Guess? क्या है?')
st.subheader(f"यह एक अद्भुत खेल है जिसमें कंप्यूटर 1 से 100 के बीच एक रैंडम नंबर चुनता है और यूज़र को उसे अनुमान लगाना होता है।")



