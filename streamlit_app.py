import streamlit as st

def main():
    st.title("Find the Highest Number")

    num1 = st.number_input("Enter the first number:", step=1.0)
    num2 = st.number_input("Enter the second number:", step=1.0)
    num3 = st.number_input("Enter the third number:", step=1.0)

    highest_number = max(num1, num2, num3)

    st.write("The highest number is:", highest_number)

if __name__ == "__main__":
    main()
