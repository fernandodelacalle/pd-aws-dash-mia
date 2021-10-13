---
marp: true
theme: default
paginate: true
class: invert
---

# Componentes Principales de Dash

---

# Dropdown

- Id  → String  →  Identificador único
- clearable →  Boolean  →  Opción de eliminar el valor actual
- disabled →  Boolean  →  Habilitado / Deshabilitado 
- Multi →  Boolean  →  Posibilidad seleccionar varios valores
- Options →  Dict  →  Valores posibles a seleccionar Dropdown - Parámetros 
- placeholder  → String  →  Cadena a mostrar al comienzo
- searchable →  Boolean  →  Opción de busqueda 
- style →  Dict  →  Estilo CSS 
- value →  String | number |list  →  Valor por defecto / inicial 

# Slider
- Id  → String  →  Identificador único- min →  number  →  Valor mínimo del slider 
- max →  number  →  Valor máximo del slider
- step →  number  →  Valor por el que incrementar/decrementar 
- marks →  Dict  →  Diccionario valor – etiqueta
- updatemode  → String omouseup →  Se actualiza cuando soltamos ratón odrag  →  Se actualiza continuamente
- value →  number  →  Valor inicial 
- vertical →  Boolean  →  Slider en vertical



# RangeSlider
- Id  → String  →  Identificador único
- min →  number  →  Valor mínimo del slider 
- max →  number  →  Valor máximo del slider
- step →  number  →  Valor por el que incrementar/decrementar 
- marks →  Dict  →  Diccionario valor – etiqueta 
- value →  number  →  Valor inicial 
- vertical →  Boolean  →  Slider en vertical 
- allowcross →  Permiter cruzar los punteros al arrastrar
- pushable →  Boolean | number  →  Distancia mínima entre los dos puntos 




# Input
- Id  → String  →  Identificador único- autoFocus →  Boolean  →  Coge el foco al recargar página 
- debounce →  Boolean  →  Si True, solo enviamos datos cuando perdemos el foco
- disabled →  Boolean  →  Habilitado / Deshabilitado 
placeholder  → String  →  Cadena a mostrar al comienzo
- type  → String  → “text”, “number”, “password”, “email”, ...
- value →  String | number →  Valor por defecto / inicial - style →  Dict  →  Estilo CSS 
- maxLength →  number →  Número máximo de carácteres 


# TextArea
- Id  → String  →  Identificador único
- autoFocus →  Boolean  →  Coge el foco al recargar página 
- lang →  String  →  Lenguaje 
- disabled →  Boolean  →  Habilitado / Deshabilitado 
- readonly →  Boolean  →  Solo lectura
- placeholder  → String  →  Cadena a mostrar al comienzo
- title  → String  →  Valor a mostrar cuando nos situamos encima
- value →  String | number →  Valor por defecto / inicial
- style →  Dict  →  Estilo CSS
- maxLength →  number →  Número máximo de carácteres 
- cols  → number  →  Número de columnas – Ancho del espacio
- rows  → number  →  Número filas – Alto del espacio
- draggable →  Boolean  →  Indica  si puede ser arrastrado 

# Checkboxes
- Id  → String  →  Identificador único
- options →  Dict  →  Valores posibles  
- value →  List  →  Valor por defecto 
- style →  Dict  →  Estilo CSS 

# Radio Items
- Id  → String  →  Identificador único
- options →  Dict  →  Valores posibles  
- value →  String  →  Valor por defecto 
- style →  Dict  →  Estilo CSS

# Button
- Id  → String  →  Identificador único
- contentEditable →  String  →  Se puede editar el contenido
- draggable →  String  →  Posibilidad  de arrastrarlo
- hidden →  Boolean  →  Mostramos o no el botón 
- n_clicks →  Number  →  Número de clicks
- N_clicks_timestamp  →  Number  →  Fecha del último click 



# date-picker
- Id  → String  →  Identificador único- min_date_allowed →  Date  →  Fecha mínima seleccionable 
- max_date_allowed →  Date  →  Fecha máxima seleccionable
- initial_visible_month →  Date  →  Fecha inicial a mostrar 
- clearable →  Boolean  →  Botón para eliminar fecha 
- with_portal  → Boolean  →  Abre el calendario en un pop up
- display_format  →  String  →  Formato de fecha a mostrar 
- stay_open_on_select  →  Boolean  →  El calendario continúa una vez seleccionada la fecha
- first_day_of_week  → number  →  Primer día de la semana: oDomingo: 0 oLunes: 1

# Markdown
- Id  → String  →  Identificador único
- Children  → String  →  Texto markdown
- style →  Dict  →  Estilo CSS 


# Upload
- Id  → String  →  Identificador único
- children →  List  → Elementos que aparecen en el upload 
- style →  Dict  →  Estilo CSS 
- disabled →  Boolean  →  Habilitamos / Deshabilitamos 
- max_size →  Number  →  Tamaño máximo
- min_size  →  Number  →  Tamaño mínimo
- multiple  →  Boolean  →  Posibilidad  subir varios ficheros

# Tabs
- Id  → String  →  Identificador único
- value →  String  →  Pestaña activa 
- children →  List  →  Elementos dentro de cada pestaña
- style →  Dict  →  Estilo CSS
- vertical →  Boolean  →  Vertical / Horizontal 


# Graph
- Id  → String  →  Identificador único
- figure  →  Dict 
    - data  →  Datos a mostrar
    - ayout  →  Diseño 
