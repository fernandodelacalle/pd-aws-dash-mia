

# CRONJOBS


- Para ejecutar algo en un horario determinado existen múltiples opciones.
- Lo ideal es ponerlo en cloud (siguiente módulo de Master).
- Si tenéis un Linux o Mac podéis usar crontab.



### Crontab


- Usamos el comando:
  ```bash  
    crontab -e
```
- Tenemos que editar para poner:
    ```bash 
    * * * * * python /path/mi_algo.py
    ```
    Donde * * * * *:
    ```bash
    * * * * * command* - minute (0-59)
    * - hour (0-23)
    * - day of the month (1-31)
    * - month (1-12)
    * - day of the week (0-6, 0 is Sunday)
    command - command to execute
    ```
  Se puede entender mejor en: https://crontab.guru/
- Por ejemplo:
```bash
01 9 * * 1-5 python /path/mi_algo.py
```
Ejecutaria de lunes a viernes a las 9:01 el comando /path/mi_algo.py.


- Para editar con vim: i para entrar, editamos, salimos con esc y guardamos cons :wq
- Si queremos tener guardados los logs podemos poner:
```bash
01 9 * * 1-5 python /path/mi_algo.py > /path/mi_algo/logs/cron_`date +\%Y-\%m-\%d_\%H:\%M:\%S`.log 2>&1
```

- Si queremos ver nuestros crons utilizamos el comando:
  ```bash  
    crontab -l
```

- Ejemplo:
  ```bash  
    */1 * * * * python3 /home/fernando_decalle/test.py > /home/fernando_decalle/cron_`date +\%Y-\%m-\%d_\%H:\%M:\%S`.log 2>&1 
  ```
  Ejecuta el programa python /home/fernando_decalle/test.py cada minuto y guarda un log cada vez que se ejecuta.


