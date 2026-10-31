import streamlit as st

from src import convert_weight

st.set_page_config(page_title="Weight Convertor(Kilograms and Pounds)", page_icon="⚖️")
st.title("⚖️ENGINEERING FOUNDATION WEIGHT CONVERTER")


st.markdown(
    """
    <style>

    /* =================================
       1. GLOBAL BACKGROUND
    ================================= */

    html, body, #root,
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"],
    .stApp {
        background-color: #0F172A !important;
        color: #F8FAFC !important;
    }

    /* Remove the white header strip */
    [data-testid="stHeader"] {
        background-color: #0F172A !important;
    }

    [data-testid="stToolbar"] {
        background-color: transparent !important;
    }

    /* Main content spacing */
    [data-testid="stMainBlockContainer"] {
        padding-top: 2rem;
    }


    /* =================================
       2. HEADINGS
    ================================= */

    .stApp h1 {
        color: #38BDF8 !important;
        text-align: center !important;
        font-weight: 800 !important;
    }

    .stApp h2,
    .stApp h3 {
        color: #F8FAFC !important;
    }


    /* =================================
       3. LABELS AND NORMAL TEXT
    ================================= */

    .stApp label,
    .stApp p,
    .stApp [data-testid="stWidgetLabel"] {
        color: #CBD5E1 !important;
    }


    /* =================================
       4. NUMBER INPUT
    ================================= */

    div[data-testid="stNumberInput"] input {
        background-color: #1E293B !important;
        color: #F8FAFC !important;
        border: 1px solid #475569 !important;
        border-radius: 8px !important;
    }

    div[data-testid="stNumberInput"] button {
        background-color: #1E293B !important;
        color: #38BDF8 !important;
        border: none !important;
    }

    div[data-testid="stNumberInput"] button:hover {
        background-color: #334155 !important;
    }


    /* =================================
       5. SELECTBOX / DROPDOWNS
    ================================= */

    div[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
        background-color: #1E293B !important;
        color: #F8FAFC !important;
        border: 1px solid #475569 !important;
        border-radius: 8px !important;
    }

    div[data-testid="stSelectbox"] div[role="combobox"] {
        color: #F8FAFC !important;
    }

    div[data-testid="stSelectbox"] svg {
        fill: #38BDF8 !important;
    }

    /* Dropdown options */
    div[data-baseweb="popover"],
    div[data-baseweb="menu"],
    ul[role="listbox"] {
        background-color: #1E293B !important;
    }

    li[role="option"] {
        background-color: #1E293B !important;
        color: #F8FAFC !important;
    }

    li[role="option"]:hover {
        background-color: #334155 !important;
    }


    /* =================================
       6. CONVERT BUTTON
    ================================= */

    .stButton > button {
        background-color: #2563EB !important;
        color: #FFFFFF !important;
        border: 1px solid #2563EB !important;
        border-radius: 8px !important;
        padding: 10px 25px !important;
        font-weight: 600 !important;
        transition: 0.2s ease-in-out;
    }

    .stButton > button:hover {
        background-color: #38BDF8 !important;
        color: #0F172A !important;
        border-color: #38BDF8 !important;
    }


    /* =================================
       7. RESULT CARD
    ================================= */

    .result-card {
        background-color: #1E293B;
        border-left: 5px solid #38BDF8;
        border-radius: 8px;
        padding: 18px;
        margin-top: 15px;
    }

    .result-label {
        color: #94A3B8;
        font-size: 12px;
        font-weight: 600;
        letter-spacing: 1.5px;
    }

    .result-value {
        color: #38BDF8;
        font-size: 25px;
        font-weight: 700;
        margin-top: 8px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


weight = st.number_input("Enter Your Weight =>", value=0.0, format="%.2f")

units = {
    "Kilograms": "kg",
    "Pounds": "lbs",
    "Milligrams": "mg",
    "Grams": "g",
    "Tonne": "t",
}

choice1 = st.selectbox("Choose the current unit", list(units.keys()))

choice2 = st.selectbox("Choose the conversion unit", list(units.keys()))

unit2 = units[choice2]

if st.button == "convert":
    if weight < 0:
        st.error("Weight cannot be negative!")

else:
    result = convert_weight(weight, choice1, choice2)


# =================================
# 7. CONVERSION BUTTON
# =================================

if st.button("Convert", type="primary", use_container_width=True):
    if weight < 0:
        st.error("Weight cannot be negative!")

    else:
        result = convert_weight(weight, choice1, choice2)

        st.success(f"Result: {result:.4f} {unit2}")
