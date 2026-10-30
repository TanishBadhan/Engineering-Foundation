import streamlit as st

from src import add, cube, div, mod, multi, sq, subt

st.set_page_config(page_title="Simple Calculator", page_icon="🔢")
st.title("🔢 Engineering Foundation Calculator")

number1 = st.number_input("Your first number ", value=0.0, format="%.3f")
number2 = st.number_input("Your second number ", value=0.0, format="%.3f")

choice = st.selectbox(
    "Choose The Operation You Want",
    (
        "select an operation...",
        "Addition",
        "Multiplication",
        "Division",
        "Subtraction",
        "Modulus",
        "Square",
        "Cube",
    ),
)

if choice == "Addition":
    result = add(number1, number2)
    st.success(f"--Answer:-- {result:.3f}")

if choice == "Multiplication":
    result = multi(number1, number2)
    st.success(f"--Answer:-- {result:.3f}")

if choice == "Division":
    result = div(number1, number2)
    st.success(f"--Answer:-- {result}")

if choice == "Subtraction":
    result = subt(number1, number2)
    st.success(f"--Answer:-- {result:.3f}")

if choice == "Modulus":
    result = mod(number1, number2)
    st.success(f"--Answer:-- {result}")

if choice == "Square":
    result = sq(number1)
    st.success(f"--Answer:--{result}")

if choice == "Cube":
    result = cube(number1)
    st.success(f"--Answer:--{result}")
