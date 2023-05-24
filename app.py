import streamlit as st
import pandas as pd
import numpy as np
import pickle

model = pickle.load(open("model.pkl", "rb"))

def find_credit_mix(text):
	if text == "Bad":
		return 0
	elif text == "Standard":
		return 1
	else:
		return 2

st.title("Credit Score Prediction:")
i1 = st.number_input("Annual Income")
i2 = st.number_input("Monthly Inhand Salary")
i3 = st.number_input("Number of Bank Accounts")
i4 = st.number_input("Number of Credit Cards")
i5 = st.number_input("Interest Rate")
i6 = st.number_input("Number of Loans")
i7 = st.number_input("Average number of days delayed by the person")
i8 = st.number_input("Number of delayed payments")
i9 = st.selectbox("Credit Mix", ("Bad", "Standard", "Good"))
i10 = st.number_input("Outstanding Debt")
i11 = st.number_input("Credit History Age")
i12 = st.number_input("Monthly Balance")

if st.button("Predict"):
	i9 = find_credit_mix(i9)
	test = np.array([[i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12]])
	res = model.predict(test)
	print(res[0])
	st.success("Prediction: " + str(res[0]))
