import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Catálogo de Lavados", layout="wide")

st.title("Panel de Producción - Catálogo de Lavados")

# Menú de selección
lavado = st.selectbox(
    "Selecciona un Estilo de Lavado:",
    ["-- Elige uno --", "DELT", "MOBU", "OVRW"]
)

# Definimos las rutas exactas según tus carpetas y nombres de archivo
if lavado == "DELT":
    ruta = "img/DELT/DELT"
    ext = ".jpg"
elif lavado == "MOBU":
    ruta = "img/MOBU/MOBU"
    ext = ".JPG.jpg"  # Extensión exacta según tu captura
elif lavado == "OVRW":
    ruta = "img/OVRW/OVRW"
    ext = ".JPG.jpg"  # Extensión exacta según tu captura
else:
    ruta = None

if lavado != "-- Elige uno --" and ruta:
    st.header(f"Lavado: {lavado}")
    
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Parte Frontal")
        # Diseño BMP
        st.image(f"{ruta}_frente_bmp{ext}", caption="Diseño BMP")
        # Resultado Lavado
        st.image(f"{ruta}_frente_lavado{ext}", caption="Resultado Lavado")

    with col2:
        st.subheader("Parte Trasera")
        # Diseño BMP Trasero
        st.image(f"{ruta}_trasera_bmp{ext}", caption="Diseño BMP Trasero")
        # Resultado Lavado Trasero
        st.image(f"{ruta}_trasera_lavado{ext}", caption="Resultado Lavado Trasero")

else:
    st.info("Selecciona un lavado para visualizar las comparativas.")
