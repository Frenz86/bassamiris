import streamlit as st
import joblib

st.title("this my first app of ML" )

model = joblib.load("model1.pkl")

input1 = st.number_input('inserire petal lenght cm', min_value=0.0, max_value=8.0, value=4.0, step=0.1)
input2 = st.number_input('inserire petal width cm', min_value=0.0, max_value=8.0, value=4.0, step=0.1)
input3 = st.number_input('inserire sepal lenght cm', min_value=0.0, max_value=8.0, value=4.0, step=0.1)
input4 = st.number_input('inserire sepal width cm', min_value=0.0, max_value=8.0, value=4.0, step=0.1)




if st.button('RESULT'):
    result = model.predict([[2,3,4.6,4]])
    st.write('the final result of the classification: %s' % result[0])


#st.write("the final result of the classification:", result[0])

