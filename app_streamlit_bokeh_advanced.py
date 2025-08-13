import streamlit as st
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
import numpy as np
import pandas as pd

st.title("Streamlit + Bokeh Ejemplo Compatible")

# Datos de ejemplo
np.random.seed(42)
df = pd.DataFrame({
    "x": np.arange(1, 21),
    "y1": np.random.randint(10, 100, 20),
    "y2": np.random.randint(20, 120, 20)
})

source = ColumnDataSource(df)

# Gráfico 1
p1 = figure(
    title="Línea y puntos",
    x_axis_label="X", y_axis_label="Y1",
    plot_height=350, plot_width=500
)
p1.line('x', 'y1', source=source, line_width=2, color="blue")
p1.circle('x', 'y1', source=source, size=8, color="red")

# Gráfico 2
p2 = figure(
    title="Barras",
    x_axis_label="X", y_axis_label="Y2",
    plot_height=350, plot_width=500
)
p2.vbar(x='x', top='y2', source=source, width=0.5, color="green")

# Mostrar
st.bokeh_chart(p1, use_container_width=True)
st.bokeh_chart(p2, use_container_width=True)
