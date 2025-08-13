import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Configuración de la página
st.set_page_config(page_title="Segmentación de Clientes", layout="wide")

st.title("📊 Segmentación de Clientes")
st.write("Ejemplo de clustering K-Means para segmentar clientes según frecuencia de compra, tipo de juego y ubicación.")

# Subida de archivo
uploaded_file = st.file_uploader("Sube tu archivo CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Vista previa de datos")
    st.dataframe(df.head())

    # Procesamiento de datos
    df['FrecuenciaCompra'] = df.groupby('Cliente')['Orden'].transform('count')

    # Codificación simple de variables categóricas
    df_encoded = df.copy()
    df_encoded['TipoInflable'] = df_encoded['TipoInflable'].astype('category').cat.codes
    df_encoded['DireccionMapa'] = df_encoded['DireccionMapa'].astype('category').cat.codes

    # Selección de características
    features = ['FrecuenciaCompra', 'TipoInflable', 'DireccionMapa']
    X = df_encoded[features]

    # Escalado
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Clustering
    kmeans = KMeans(n_clusters=3, random_state=42)
    df['Cluster'] = kmeans.fit_predict(X_scaled)

    st.subheader("Clientes Segmentados")
    st.dataframe(df[['Cliente', 'FrecuenciaCompra', 'TipoInflable', 'DireccionMapa', 'Cluster']])

    # Visualización
    fig, ax = plt.subplots()
    scatter = ax.scatter(X_scaled[:, 0], X_scaled[:, 1], c=df['Cluster'], cmap='viridis')
    ax.set_xlabel('Frecuencia de Compra (Escalada)')
    ax.set_ylabel('Tipo de Inflable (Escalado)')
    ax.set_title('Segmentación de Clientes')
    plt.colorbar(scatter, ax=ax)
    st.pyplot(fig)

else:
    st.info("Por favor sube un archivo CSV para comenzar.")
