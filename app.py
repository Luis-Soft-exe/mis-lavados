import streamlit as st
import os

# Configuración de la página
st.set_page_config(page_title="Catálogo de Lavados", layout="wide")

st.title("Panel de Producción - Catálogo de Lavados")

# Crear el menú desplegable en la barra lateral o al centro
lavado = st.selectbox(
    "Selecciona un Estilo de Lavado:",
    ["-- Elige uno --", "DELT", "MOBU", "OVRW"]
)

# Diccionario para manejar las extensiones raras (.JPG.jpg)
# DELT parece ser .jpg normal, MOBU y OVRW tienen la doble extensión
ext = {
    "DELT": ".jpg",
    "MOBU": ".JPG.jpg",
    "OVRW": ".JPG.jpg"
}

if lavado != "-- Elige uno --":
    st.header(f"Lavado: {lavado}")
    
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Parte Frontal")
        st.image(f"img/{lavado}/{lavado}_frente_bmp{ext[lavado]}", caption="Diseño BMP")
        st.image(f"img/{lavado}/{lavado}_frente_lavado{ext[lavado]}", caption="Resultado Lavado")

    with col2:
        st.subheader("Parte Trasera")
        # Nota: DELT a veces no tiene trasera en algunas fotos, 
        # esto intentará cargarlas si existen
        try:
            st.image(f"img/{lavado}/{lavado}_trasera_bmp{ext[lavado]}", caption="Diseño BMP")
            st.image(f"img/{lavado}/{lavado}_trasera_lavado{ext[lavado]}", caption="Resultado Lavado")
        except:
            st.write("Fotos traseras no disponibles para este modelo.")

else:
    st.info("Por favor, selecciona un lavado del menú superior para ver las fotos.")
