import pickle
import streamlit as st

# membaca model
Breast_model =  pickle.load(open('Breast_model.sav', 'rb'))

#Judul Web
st.title('Data Mining Prediksi Penyakit Kanker Payudara')

Radius = st.text_input('Radius Lobus')

Texture= st.text_input('Masukan  ukuran tekstur permukaan benjolan kanker')

Parimeter =st.text_input('Masukan ukuran keliling jaringan lobus')

Area = st.text_input('Masukan ukuran area yang terkena jaringan kanker')

Smoothness = st.text_input('masukan ukuran dalam level smoothless')


# code untuk kelompok jenis bunga
Breast_cancer_diagnosis = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi'):
    Breast_cancer_prediction = Breast_model.predict([[Radius, Texture, Parimeter, Area, Smoothness]])
    
    if(Breast_cancer_prediction[0] == 1):
        Breast_cancer_diagnosis = 'Pasien mengidap kanker payudara '
    else :
        Breast_cancer_diagnosis = 'Pasien tidak mengidap kanker payudara'

    st.success(Breast_cancer_diagnosis)
