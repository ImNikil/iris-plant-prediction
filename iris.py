import streamlit as st
import pickle

st.title("Iris plant prediction")
sl=st.number_input("enter sepal length")
sw=st.number_input("enter sepal width")
pl=st.number_input("enter petal length")
pw=st.number_input("enter petal width")
button=st.button("predict")

if button:
    model=pickle.load(open("iris.pkl","rb"))
    res=model.predict([[sl,sw,pl,pw]])[0]
    st.markdown(f"predicted iris class:{res}")
