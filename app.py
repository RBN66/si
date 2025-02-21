import streamlit as st
from datetime import datetime, timedelta

#from librerias.hojaCalc import insertarFila
#from librerias.enviarMail import enviarMail
#from librerias.agendarCita import agendarCita

st.set_page_config(page_title='Google API conexiones', page_icon='📅')
# Formulario en Streamlit
st.title('Formulario de Cita')

with st.form('Formulario de citas',clear_on_submit=True):
    nombre = st.text_input('Nombre')
    email = st.text_input('eMail')
    tfno = st.text_input('Teléfono')
    fecha= st.date_input('Fecha')
    hora = st.time_input('Hora')

    hora_formato = datetime.combine(datetime.today(),hora)
    hora_fin = (hora_formato + timedelta(hours=1))
    hora_fin = hora_fin.time()


    if st.form_submit_button('Enviar'):
        # Añado a Sheets
        insertarFila(nombre, email, tfno, fecha, hora)
        # Envío de correo
        enviarMail(nombre, email, str(fecha), str(hora))
        # Agendo cita
        agendarCita(nombre, email, tfno, fecha, hora, hora_fin)

        st.success('Datos enviados con éxito!')