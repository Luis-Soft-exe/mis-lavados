import streamlit as st
import os

st.set_page_config(page_title="Catálogo de Lavados", layout="wide")
st.title("Panel de Producción - Catálogo de Lavados")

# Menú de selección
lavado = st.selectbox("Selecciona un Estilo de Lavado:", ["-- Elige uno --", "DELT", "MOBU", "OVRW"])

def mostrar_imagen(ruta_base, nombre_pieza, descripcion):
    # Esta función busca la imagen con cualquier extensión para que no salga el error rojo
    extensiones = [".jpg", ".JPG", ".JPG.jpg", ".png"]
    encontrada = False
    
    for ext in extensiones:
        ruta_completa = f"{ruta_base}_{nombre_pieza}{ext}"
        if os.path.exists(ruta_completa):
            st.image(ruta_completa, caption=descripcion)
            encontrada = True
            break
    
    if not encontrada:
        st.warning(f"No se encontró la foto: {nombre_pieza}")

if lavado != "-- Elige uno --":
    st.header(f"Lavado: {lavado}")
    
    # Ruta hacia la carpeta (ejemplo: img/MOBU/MOBU)
    ruta_base = f"img/{lavado}/{lavado}"
    
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Parte Frontal")
        mostrar_imagen(ruta_base, "frente_bmp", "Diseño BMP")
        mostrar_imagen(ruta_base, "frente_lavado", "Resultado Lavado")

    with col2:
        st.subheader("Parte Trasera")
        mostrar_imagen(ruta_base, "trasera_bmp", "Diseño BMP Trasero")
        mostrar_imagen(ruta_base, "trasera_lavado", "Resultado Lavado Trasero")
else:
    st.info("Selecciona un lavado para visualizar las comparativas.")
