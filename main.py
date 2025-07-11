import streamlit as st
st.set_page_config(page_title="Portfolio",
                   layout="wide", page_icon=":rocket:")
st.title("Portfolio Saya")
st.header("Data Scientist")
st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman",
                        ["Tentang Saya", "Project_1", "Project_2", "Machine Learning", "Kontak"])


if page == 'Kontak' :
    import kontak
    kontak.tampilkan_kontak()
elif page == 'Tentang Saya' : 
    import tentang
    tentang.tampilkan_tentang()
elif page == 'Project_1' : 
    import proyek
    proyek.projectsatu()
elif page == 'Project_2' : 
    import projectdua
    projectdua.project2()
elif page == 'Machine Learning' : 
    import prediksi
    prediksi.prediksi()

