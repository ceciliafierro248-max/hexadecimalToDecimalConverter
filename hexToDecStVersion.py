import streamlit as st

hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

def hexToDecimal(userInput):
    list = []
    multipyMagic = 1
    result = 0

    for char in userInput:
        if char not in hexNumbers:
            return 'theyDidSomethingWrong'
        else:
            for char in userInput:
                newNumber = hexNumbers[char]
                list.insert(0, newNumber)
                print(list)

            for i in list:
                result = (multipyMagic * i) + result
                multipyMagic = multipyMagic * 16
            return result

with st.sidebar:
    st.subheader("About app:")
    st.markdown("This app provides some basic information about hexadecimals and a hexadecimal to decimal converter. This tool was created by Cecilia F. as an extension of the Python Essentials Training LinkedIn Learning course.")
    st.markdown("")
    st.markdown("*I hope you enjoy!*")


st.header("Welcome to Hexadecimal to Decimal Converter!", divider = 'orange')
st.text("")
st.markdown("Hex, or hexadecimal, is a base-16 number system. This means the number place changes by the power of 16, not the usual power of 10.")
st.text("")
st.markdown("")
st.markdown("*Lets look at an example...*")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("**Base-10 Example**")
st.text("")
st.markdown("")
st.latex(r"4150 = ((4 * (10 * 10 * 10)) + (1 * (10 * 10)) + (5 * (10)) + (0 * (1)))")
st.markdown("")
st.latex(r"4150 = (4 * 10^3) + (1 * 10^2) + (5 * 10^1) + (0 * 10^0)")
st.markdown("")
st.latex(r"4150 = (4 * 1000) + (1 * 100) + (5 * 10) + (0 * 1) = 4150")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("**Base-16 Example**")
st.markdown("")
st.markdown("")
st.latex(r"4150 = ((4 * (16 * 16 * 16)) + (1 * (16 * 16)) + (5 * (16)) + (0 * (1)))")
st.markdown("")
st.latex(r"4150 = (4 * 16^3) + (1 * 16^2) + (5 * 16^1) + (0 * 16^0)")
st.markdown("")
st.latex(r"4150 = (4 * 4096) + (1 * 256) + (5 * 16) + (0 * 1) = 16720 \text{ in base-10}")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("Why is it important? Base-16 allows us to store bigger numbers in smaller spaces than base-10. Think about it, since we are multiplying by a 16th power in base-16, we can store the larger results from base-16 in the same space as smaller numbers multiplied by the 10th power in base-10. Base-16 is incredibly important to computer science, since some programs have such large numbers that without base-16 they would not be able to store them.")
st.markdown("")
st.markdown("")
st.markdown("")
st.subheader("Hexadecimal Charts", divider = 'orange')
st.markdown("")
col1, col2 = st.columns(2)

with col1:
    st.table(data=hexNumbers, width=int(125), height="stretch")
with col2:
    st.image("/Users/ceciliafierro/Desktop/hexademicalToDecimalToBinary.jpg")
    st.markdown("")
    st.markdown("")
    st.link_button("Interested in more information? Click me!", "https://www.khanacademy.org/math/algebra-home/alg-intro-to-algebra/algebra-alternate-number-bases/v/hexadecimal-number-system")

st.markdown("")
st.markdown("")
st.subheader("")

st.subheader("Converter", divider='orange')
st.markdown("")
userInput = st.text_input("Type your hexadecimal code here!")

if userInput == "":
    st.text("")
else:
    try:
        answer = str(hexToDecimal(userInput))
        if answer == 'theyDidSomethingWrong':
            st.text("Ah oh! Something went wrong, likely you typed in characters that are not part of the hexadecimal alphabet. Please try again.")
        else:
            st.text("The final result is " + answer + "!")
    except KeyError:
        st.text("Ah oh! Something went wrong, likely you typed in characters that are not part of the hexadecimal alphabet. Please try again.")
