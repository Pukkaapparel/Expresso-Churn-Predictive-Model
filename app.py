from model import *
import streamlit as st
import _pickle

cat_col = pickle.load(open("married_fuga.pkl", "rb"))
def main():
    
    st.title("Expresso Telecommunication Churn Prediction")


    user_id = st.selectbox("Insert Your User ID", (cat_col["user_id"]))
    region = st.selectbox("Insert Your Region", (cat_col["REGION"]))
    tenure = st.selectbox("Insert Your Suscription", (cat_col["TENURE"]))
    montant = st.number_input("Insert The Number", value=13500)
    frequent_rech = st.number_input("Insert the frequency of your recharge", value=15.0)
    revenue = st.number_input("Insert the revenue", value=13502.0)
    arpu_segement = st.number_input("Insert the segement", value=4501.0)
    frequency = st.number_input("Insert the Frequency Number", value=18.0)
    data_vol = st.number_input("Insert the data volume of your recharge", value=43804.0)
    on_net = st.number_input("Insert the on_net value", value=41.0)
    orange = st. number_input("Insert the orange", value=102.0)
    tigo = st.number_input("Insert The Togo", value=2.0)
    zone1 = st.number_input("Insert Zone 1", value=1.0)
    zone2 = st.number_input("Insert Zone 2", value=1.0)
    mrg = st.text_input("Insert No", value="No")
    regularity = st.number_input("Insert the regularity", value=62.0)
    top_pack = st.selectbox("Insert your suscription pack", (cat_col["TOP_PACK"]))
    freq_top_pack = st.number_input("Insert frequency pack number", value=11.0)

    CHURN = ""

    if st.button("Predict"):

        CHURN = prediction([user_id, region, tenure, montant, frequent_rech, revenue, arpu_segement, 
                            frequency,data_vol, on_net, orange, tigo, zone1, zone2, mrg, regularity,
                              top_pack,freq_top_pack])


    st.success(CHURN)


if __name__ == "__main__":
    main()
