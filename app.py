import streamlit as st
import csv
st.title("Coffee Store App")

st.header("Customer Order Form")

#
name = st.text_input("Enter Customer Table Name:")
phone = st.text_input("Enter Customer Cofee Number: ")
coffee = st.selectbox("Select Cofee" , ["Espresso Rs:120" , "Cappuccino Rs:150","Caffe` Latte Rs:180","Americano Rs: 190", "Coconut Coffee Rs:350", "Salt Coffe / Egg Coffee Rs: 380","Phin Black Coffee Rs:240"])

submit =st.button("submit")

if submit:
    if name=="" and phone == "":
        st.warning(" Please fill all fieds")
    else:
        with open ("data.csv" ,"a" , newline ="") as file:
            writer = csv.writer(file)
            writer.writerow([name , phone , coffee])


    st.success("Data received!")

import pandas as pd

st.header(" Customer Recordes")

try:
    data =pd.read_csv("data.csv")
    st.dataframe(data)
except:
    st.warnig("No data available yet")

if st.button("Clear All Data "):
    with open("data.csv" ,"w") as file:
        file.write("name , phone , coffee\n")
        st.success("All data cleared!")

with open("data.csv" ,"rb" ) as file:
    st.download_button(
        label ="Download Customer Data",
        data = file,
        file_name="customer_data.csv",
        mime="text/csv"
    )