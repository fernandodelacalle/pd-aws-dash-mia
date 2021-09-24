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


# Desarrollo en remoto con vscode y SSH

--- 

- Como habeis visto desarrollar en desde la terminal puede ser tedioso.
- vscode tiene una extensión llamada Remote - SSH que nos permite trabajar con nuestro vscode dentro de la máquina EC2.


---

![center](imgs/architecture-ssh.png)


- https://code.visualstudio.com/docs/remote/ssh

---
Los pasos para conectar nuestro Code a la máquina EC2 son los siguientes:




- Creamos una nueva instancia de EC2.

- Es importante que tegamos habilitado el pueto 22 (SSH) desde nuesta ip.

- En el último paso de la creación es necesario guardar el fichero con la clave privada.


- Descargamos la extensión Remote - SSH.


- Pulsamos el boton verde de la la esquina inferior izquierda.

- Pulsamos: Remote - SSH: Connect to Host

- Pulsamos Configure SSH

- Pulsa el primero de los ficheros perteneciente a tu usuario.


Introduce lo sigueinte:


```
Host aws-ec2
    HostName ec2-15-188-185-255.eu-west-3.compute.amazonaws.com
    User ec2-user
    IdentityFile /Users/fernando/Desktop/miax-key_pait.pem
```


---



    Host (aws-ec2) is just a name that will appear in VS Code. It can be any name.
    HostName is the server’s host or IP.
    User is the Ubuntu username.
    IdentityFile is the path to the private key.

To obtain the HostName and User for your instance, navigate to your EC2 console. Right Click on an instance > Connect. This will open up a dialog like

Here, ubuntu is the User and ec2–44–229–243–8.us-west-2.compute.amazonaws.com is the HostName.

Save the configuration file. Now you’re ready to connect to your Host. Click the status item on the bottom left and select Connect to Host. You should now be able to see your host.




