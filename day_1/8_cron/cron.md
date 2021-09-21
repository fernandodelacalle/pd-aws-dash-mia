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

# Cronjobs

---

- Para ejecutar algo en un horario determinado existen múltiples opciones.
- Una de las herramientas más utilizada es crontab.

---

### Crontab

- Con crontab definimos en un fichero cuando queremos que se ejecute nuestro programa y que comando queremos ejecutar.
- El horario se define con 5 expresiones separadas por un espacio: ```* * * * *``` donde:
    ```bash
    * - minute (0-59)
    * - hour (0-23)
    * - day of the month (1-31)
    * - month (1-12)
    * - day of the week (0-6, 0 is Sunday)
- Por ejemplo ```0 8 * * 1-5``` significa a las 8:00 de lunes a viernes.
- Puedes obtener ayuda en: https://crontab.guru/
- Muchas de las utilidades cloud como veremos usan este formato.

---

- Para añadir un nuevo cron usamos el comando:
```bash  
  crontab -e
```
- Tenemos que editar para poner por ejemplo:
```bash
* * * * * python /path/mi_algo.py
```
- Ejecutaria cada minuto el comando /path/mi_algo.py.

---
- Por defecto crontab nos hace editar con vim: i para entrar, editamos, salimos con esc y guardamos cons :wq
- Podemos editar con nano si usamos:
```bash
export VISUAL=nano; crontab -e
```


---

- Si queremos ver nuestros crons utilizamos el comando:
```bash  
crontab -l
```

----

- Si queremos tener guardados los logs podemos poner:
```bash
01 9 * * 1-5 python /path/mi_algo.py > /path/mi_algo/logs/cron_`date +\%Y-\%m-\%d_\%H:\%M:\%S`.log 2>&1
```

---


- Ejemplo:
  ```bash  
    */1 * * * * python3 /home/fernando_decalle/test.py > /home/fernando_decalle/cron_`date +\%Y-\%m-\%d_\%H:\%M:\%S`.log 2>&1 
  ```
  Ejecuta el programa python /home/fernando_decalle/test.py cada minuto y guarda un log cada vez que se ejecuta.


---
## Ejercicio

- Crea una carpeta nueva.
- Genera dentro de esta un nuevo virtual enviroment
- Instala la librería pandas
- Escribe un programa que use esta librería y que tenga un print que ponga la hora actual por pantalla.
- Genera un script sh que active el virtual enviroment y ejecute tu programa.
- Prueba a ejecutar el script en la terminal (```./my_script.sh```), puede que tengas que dar a este fichero permisos de ejecución con: ```chmod +x my_script.sh```
- Usa crontab para que se ejecute cada minuto y guarde el log.
