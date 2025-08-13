import streamlit as st
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.layouts import column, row
import numpy as np
import pandas as pd

st.title("Streamlit + Bokeh Avanzado")
st.write("Ejemplo con gráficos coordinados e interacción entre ellos.")

# --- Generar dataset de ejemplo ---
np.random.seed(42)
df = pd.DataFrame({
    "x": np.arange(1, 51),
    "y1": np.random.randint(10, 100, 50),
    "y2": np.random.randint(20, 120, 50),
    "category": np.random.choice(["A", "B", "C"], 50)
})

# --- Filtros interactivos ---
selected_category = st.selectbox("Selecciona la categoría:", df["category"].unique())
filtered_df = df[df["category"] == selected_category]

source = ColumnDataSource(filtered_df)

# --- Gráfico 1: Linea + Puntos ---
p1 = figure(title="Gráfico 1: Línea y puntos", 
            x_axis_label="X", y_axis_label="Y1", 
            plot_height=350, plot_width=500)
p1.line('x', 'y1', source=source, line_width=2, color="blue", legend_label="Y1 Line")
p1.circle('x', 'y1', source=source, size=8, color="red", legend_label="Y1 Points")

# --- Gráfico 2: Barra ---
p2 = figure(title="Gráfico 2: Barras", 
            x_axis_label="X", y_axis_label="Y2", 
            plot_height=350, plot_width=500)
p2.vbar(x='x', top='y2', source=source, width=0.5, color="green", legend_label="Y2 Bars")

# --- Layout ---
st.write(f"Mostrando datos de la categoría: {selected_category}")
st.bokeh_chart(row(p1, p2), use_container_width=True)
