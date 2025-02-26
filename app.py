import streamlit as st
from pint import UnitRegistry

# Initialize UnitRegistry
ureg = UnitRegistry()

# Custom CSS for Styling
st.markdown(
    """
    <style>
        body {
            background-color: #f5f5f5;
            font-family: Arial, sans-serif;
        }
        .stApp {
            background-color: #ffffff;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);
        }
        label {
            font-size: 14px !important;
            font-weight: bold;
            color: #333333 !important;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 14px;
            padding: 8px;
            border-radius: 5px;
            border: none;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .result-box {
            background-color: #e3f2fd;
            color: #333;
            padding: 8px;
            border-radius: 5px;
            border: 1px solid #90caf9;
            font-size: 16px;
            text-align: center;
        }
        .error-message {
            background-color: #ffcccc;
            color: #b30000;
            padding: 8px;
            border-radius: 5px;
            border: 1px solid #ff0000;
            font-size: 16px;
            text-align: center;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Welcome Message
st.markdown("""<h2 style='text-align: center; color:rgb(126, 126, 126);'>Umaima welcomes you to her Unit Converter!</h2>""", unsafe_allow_html=True)

# Streamlit App Layout
st.markdown("<h1 style='text-align: center; color: #333;'>Universal Unit Converter</h1>", unsafe_allow_html=True)

# Layout for Input and Conversion Fields
col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    user_input = st.text_input("**Enter Value to Convert:**", placeholder="Type a number...", max_chars=10)

# Validate Input and Convert to Number
def parse_input(value):
    try:
        if "." in value:
            return float(value)
        return int(value)
    except ValueError:
        return None

amount = parse_input(user_input)

# Conversion Fields Side by Side
col4, col5 = st.columns([1, 1])

with col4:
    from_unit = st.selectbox("**From Unit:**", sorted(ureg))

with col5:
    to_unit = st.selectbox("**To Unit:**", sorted(ureg))

# Convert Button
if st.button("Convert"):
    if amount is None:
        st.markdown("""
            <div class='error-message'>
                ❌ Please enter a valid number.
            </div>
        """, unsafe_allow_html=True)
    else:
        try:
            result = (amount * ureg(from_unit)).to(to_unit)
            formatted_result = int(result.magnitude) if result.magnitude.is_integer() else round(result.magnitude, 2)
            formatted_amount = int(amount) if isinstance(amount, int) else amount
            st.markdown(
                f"""
                <div class='result-box'>
                    {formatted_amount} {from_unit} = <b>{formatted_result} {to_unit}</b>
                </div>
                """, unsafe_allow_html=True
            )
        except Exception as e:
            st.markdown(f"""
                <div class='error-message'>
                    ❌ Conversion Error: {e}
                </div>
            """, unsafe_allow_html=True)

# Run this app using: streamlit run app.py
