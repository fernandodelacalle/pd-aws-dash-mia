---
marp: true
theme: default
paginate: true
---

<style>
img[alt~="center"] {
  display: block;
  margin: 0 auto;
}
</style>


# Introducción a redes y protocolos.

---


- Todo el cloud se basa en internet y sus protocolos.
- Es necesario conocerlos minimamente para poder entender que estamos haciendo.
- IP, TCP, HTTP, SSH, etc.

---
# Modelo OSI -- TCP/IP
- OSI: Open Systems Interconnection.
- Estándar que tiene por objetivo conseguir interconectar sistemas de procedencia distinta para que estos pudieran intercambiar información sin ningún tipo de impedimentos debido a los protocolos con los que estos operaban de forma propia según su fabricante. 

---

![center](imgs/osi.png)
---

# Capa Fisica
    - Transformaciones que se le hacen a la secuencia de bits para transmitirlos de un lugar a otro.
    - Protocolos Fisicos: Ethernet, Wifi, Bluetooth

---

# Capa de enlace de datos:
    - Transferencia fiable de información a través de un circuito de transmisión de datos.
    - Conseguir que la información fluya, libre de errores, entre dos máquinas que estén conectadas directamente

---

# Capa de Red
    - Proporciona conectividad y selección de ruta entre dos sistemas de hosts que pueden estar ubicados en redes geográficamente distintas.
    - Protocolo IP (Internet Protocol).
---

- Entrega de los paquetes de datos no confiable. 
- "mejor esfuerzo": lo hará lo mejor posible, pero garantizando poco.
- Al no garantizar nada sobre la recepción del paquete, este podría llegar dañado, en otro orden con respecto a otros paquetes, duplicado o simplemente no llegar.
- Las cabeceras IP contienen las direcciones de las máquinas de origen y destino (direcciones IP), direcciones que serán usadas por los enrutadores (routers) para decidir el tramo de red por el que reenviarán los paquetes. 
- Buscar la mejor ruta para llegar de una máquina a otra. 

---
- IP es el elemento común en el Internet de hoy. 
- El actual y más popular protocolo de red es IPv4.

---
- Una dirección IP es un número que identifica de manera lógica y jerárquicamente a una interfaz de un dispositivo (habitualmente una computadora) dentro de una red que utilice el protocolo de Internet (Internet Protocol),
- Si un Equipo dispone de una tarjeta de red Ethernet y otra WiFi, tendrá una dirección IP asignada a cada una si las está usando. 
- Dicho número no se ha de confundir con la dirección MAC que es un número físico que es asignado a la tarjeta o dispositivo de red (viene impuesta por el fabricante y no varía en toda su vida útil), mientras que la dirección IP puede cambiarse, por ejemplo, cambiando la red a la cual está conectado el equipo. 

---
- IPv6 es el sucesor propuesto de IPv4.
- Poco a poco Internet está agotando las direcciones disponibles por lo que IPv6 utiliza direcciones de fuente y destino de 128 bits, muchas más direcciones que las que provee IPv4 con 32 bits.
ipv4.bmp


---
- Si la dirección puede cambiar al reconectar. A la posibilidad de cambio de dirección de la IP se denomina dirección IP dinámica.
- Los sitios de Internet que por su naturaleza necesitan estar permanentemente conectados, generalmente tienen una dirección IP fija (IP fija o IP estática); es decir, no cambia con el tiempo

---
IP Pública y Privada

---

# Capa de transporte:
    - Encargado de la transferencia libre de errores de los datos entre el emisor y el receptor, aunque no estén directamente conectados, así como de mantener el flujo de la red
    - Protocolos de transporte:
        - UDP (User Datagram Protocol): no orientado a la conexión, util para audio, video etc.
        - TCP (Transmission Control Protocol): se diseñó específicamente para proporcionar un flujo de bytes confiable de extremo a extremo a través de una interred no confiable.

---

- Se ocupa de la administración de los puertos y los establece en el encabezado de los segmentos
- Un puerto suele estar numerado para de esta forma poder identificar la aplicación que lo usa. Decidir a qué programa entregará los datos recibidos.
- Esta asignación de puertos permite a una máquina establecer simultáneamente diversas conexiones con máquinas distintas, ya que todos los segmentos que se reciben tienen la misma dirección, pero van dirigidos a puertos diferentes. 
- https://es.wikipedia.org/wiki/Anexo:Puertos_de_red
---



- TCP nos proporciona:
    - Una trasmisión sin errores.
    - Los datos son entregados en orden.
- Una vez establecida la conexión TCP, los mensajes intercabiados entre el cliente y el sercidos nunca se pederan, modificaran o recirviran en otro orden.

---



# Capa de Aplicación
    - Define los protocolos que utilizan las aplicaciones para intercambiar datos.
    - HTTP, SSH, FTP, POP, SMTP, etc.

---
# HTTP

- Los servidres web hablan entre ellos mediante el protocolo HTTP: Hypertext Transfer Protocol.
- HTTP es el leguaje común de internet.
- El contenido web reside en servidres web.
- Estos servidores usan el protocolo HTTP: HTTP Servers.

---
- Los componentes básicos de la World Wide Web son HTTP clients y HTTP servers.
- Los clientes piden contenido a estos HTTP Servers, para ello mandan HTTP requests.
- Los servidores envian los datos pedidos en HTTP responses.

---

- HTTP usa el protocolo TCP para transportar sus mensajes.
- TCP usa IP para las conexiones, direciones IP y Puertos.

---

- Los servidores web almacenan recursos web de cualquier tipo. Contenido HTML, ficheros de text, imagenes, etc.
- Los recursos pueden ser generados de forma dinámica.

---

URIs

- Cada servidor tiene un nombre, de manera que los clientes puedan llamarlo.
- El nombre del servidor se denomina uniform resource identifie o URI.
- Son como direcciones postales de cada servidor.

URLs

-  Uniform Resource Locator (URL) es el URI más común.
- Especifica la localización espcica de un recurso en un servidor en concreto.
- Tiene 3 partes:
    - Esquema: Describe el protocolo usado para comunicarse con el recurso, normalmente el protocolo HTTP (http:// ).
    - Dirección
    - Localización: Donde esta el recurso localizado en el servidor.

---


- Una trasación HTTP consiste en un comando de request (del cliente al servidor) y una respuesta (del servidor al cliente). 
- Esta comunicación ocurren en bloques formateados llamandos mensajes HTTP.
- HTTP soporta distintos comandos, llamados  HTTP methods.
- Cualquier comunicación HTTP tiene asociada un método.
- El método dice al servidor que acción tiene que realizar.

---

- Todas las respuestas HTTTP tienen un codigo de status.
- El código en un numero de 3 dígitos que dice al cliente si la petición ha sido procesada correctamente o si se requieren otras acciones.

|Code| Descripción|
|---|---|
|200| OK|
|404| Not Found|
|500| Server Internal Error|	

---

- Una página web consiste de multiples HTTP transactions para mostrarse.
- Podemos verlo en la utilidad del navegador.

---

Pasos:

1. El cliente extre el hostname de la URL.
2. Usando el DNS el cliente convierte el hostname en una IP.
3. El cliente extrae el puerto de la URL, si no lo tiene usa el 80 por defecto.
4. El cliente extablece una comunicación TCP con el servior.
5. El cliente envia una peticción HTTP al servidor.
6. El servidor envia una respuesta al cliente.
7. La conexión se cierra y el cliente muesta la información.

---

# Otras aplicaciones:

- Proxies: Itermediarios entre el cliente y el servidor

- Caches: guardan copias de contenido popular más cerca de los clientes.

- Gateways: Servidores especiales que actuan de intermediarios de otros servidores ( por ejemplo para convertir trafico a otros protocolos)
    Special web servers that connect to other applications
