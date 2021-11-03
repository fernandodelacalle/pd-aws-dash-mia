---
marp: true
theme: default
paginate: true

---

# Visualizaciones Interactivas

---


- El módulo dash_core_components incluye el componente Graph.
- Graph renderiza visualizaciones interactivas usando plotly.js.
- El argumento figure de dash_core_components.Graph es el mismo que se utiliza en plotly.py
- Por lo que podemos usar todos los ejemplos de esta librería: https://plotly.com/python/


---
- Los componentes de dash se describen con un conjunto de atributos.
- Todos estos atributos se pueden actualizar usando funciones callback.
- Solo un conjunto de estos atributos son actualizados con las interacciones del usuario (como cuando elegimos una opción en un menú).

---

- dcc.Graph tiene 4 atributos que son actualizados con la interacción del usuario: 
    - hoverData: ratón encima del dato.
    - clickData: dato pulsado.
    - selectedData: región selecionada.
    - relayoutData: zoom movimento de la region mostrada.

- En `example_1.py` puedes ver un ejemplo de cada uno.
- En `example_2.py` puedes ver una app completa que hace uso de esta funcionalidad.
---

