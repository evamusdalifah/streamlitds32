import streamlit as st
import pandas as pd
import numpy as np

def project2():
    pilihan = st.radio("Pilih opsi:", ("Opsi 1", "Opsi 2", "Opsi 3"))

    if pilihan == "Opsi 1":
        st.write("Anda memilih opsi 1")
    elif pilihan == "Opsi 2":
        st.write("Anda memilih opsi 2")
    else:
        st.write("Anda memilih opsi 3")