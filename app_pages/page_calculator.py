# Create a function named calculator_body()
# Within it, create 3 columns using the st.columns() function
# Note, in the video, this column function was still in beta
    
import streamlit as st

def calculator_body():
    st.write("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        num1 = st.number_input(label='Enter the first number', step=1)
    with col2:
        num2 = st.number_input(label='Enter the second number', step=1)
    with col3:
        operator = st.selectbox(label='Select an operator',
                                options=['Add', 'Subtract', 'Multiply', 'Divide'])
    if st.button('CALCULATE'):
        if num2 == 0 and operator == 'Divide':
            st.error("You can't divide by 0 dumb-ass")
        else:
            calculator_function(num1, num2, operator)


def calculator_function(num1, num2, operator):
    if operator == 'Add':
        result = num1 + num2
    elif operator == 'Subtract':
        result = num1 - num2
    elif operator == 'Multiply':
        result = num1 * num2
    elif operator == 'Divide':
        result = num1 / num2

    st.success(f'The result is **{result}**')


