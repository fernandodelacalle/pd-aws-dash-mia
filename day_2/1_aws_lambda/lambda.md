



---


Lambda es un servicio informático que permite ejecutar código sin aprovisionar ni administrar servidores. Lambda ejecuta el código en una infraestructura informática de alta disponibilidad y realiza todas las tareas de administración de los recursos informáticos, incluido el mantenimiento del servidor y del sistema operativo, el aprovisionamiento de capacidad y el escalado automático, así como la monitorización del código y las funciones de registro. Con Lambda, puede ejecutar código para prácticamente cualquier tipo de aplicación o servicio de backend. 


---

Lenguajes Admitidos:

https://docs.aws.amazon.com/es_es/lambda/latest/dg/lambda-runtimes.html

---


 ideal para muchos escenarios de aplicaciones, siempre que pueda ejecutar el código de la aplicación utilizando el entorno de tiempo de ejecución estándar de Lambda y dentro de los recursos que Lambda proporciona


  solo es necesario preocuparse por el código. Lambda administra la flota de computación, que ofrece una combinación equilibrada de memoria, CPU, red y otros recursos para ejecutar su código. 

---


Puede crear funciones en la consola de Lambda o con un conjunto de herramientas IDE, herramientas de línea de comandos o los SDK de AWS. La consola de Lambda proporciona un editor de código para lenguajes no compilados que permiten modificar y probar el código con rapidez. La AWS Command Line Interface (AWS CLI) ofrece acceso directo a la API de Lambda para la configuración avanzada y casos de uso de automatización. 


---

casos de uso comunes

- Datos y análisis: Podemos cargar datos, por ejemplo en un csv, en un bucket de s3 y que cuando esto ocurra la función lamnda lo pocese y lo envie a otro bucket.

- Sitios web: supongamos que está creando un sitio web y que desea alojar la lógica del backend en Lambda. Puede invocar la función de Lambda a través de HTTP utilizando Amazon API Gateway como punto de enlace HTTP. A continuación, el cliente web puede invocar la API y, por último, API Gateway puede dirigir la solicitud a Lambda. 

- Procesos Periodicos: Podemos ejecutar un código frecuentemente, definiendo cuando con una expresión cron usando EventBridge.


---


Implemente su código de función para Lambda mediante un paquete de implementación. Lambda admite dos tipos de implementaciones:

    Un archivo de archivo .zip que contiene su código de función y sus dependencias.

    Imagen de contenedor compatible con la especificación Open Container Initiative (OCI). Lo veremos más adelante.


---

Crear una función de Lambda con la consola.

La función usa el código predeterminado que Lambda crea. 
La consola de Lambda proporciona un editor de código para lenguajes no compilados 


---
Creación de una función de Lambda con la consola

    Abra la Functions page (Página de funciones)

en la consola de Lambda.

Elija Create function (Crear función).

Bajo Basic information (Información básica), haga lo siguiente:

    En Function name (Nombre de función), introduzca my-function.

    En Tiempo de ejecución, Elejir Python3.9

Elija Create function (Crear función).

---


Cómo invocar la función de Lambda

Invoque la función de Lambda utilizando los datos del evento de muestra que se proporcionan en la consola.

Para invocar una función

    Después de seleccionar la función, elija la pestaña Prueba.

    En la sección Evento de prueba, elija Nuevo evento. En Plantilla, deje la opción predeterminada hello-world. Introduzca un nombre para esta prueba y tenga en cuenta la siguiente plantilla de evento de ejemplo: 

    Elija Save changes (Guardar cambios) y después Test (Probar). Cada usuario puede crear hasta 10 eventos de prueba por función. Dichos eventos de prueba no están disponibles para otros usuarios.

    Lambda ejecuta la función en su nombre. El controlador de funciones recibe y procesa el evento de muestra. 



Si se realiza correctamente, puede ver los resultados en la consola.

    El resultado de ejecución muestra el estado de ejecución correctamente. Para ver los resultados de ejecución de la función, expanda Detalles. Tenga en cuenta que el enlace de los logs (registros) abre la página de Log groups (Grupos de registro) en la consola de CloudWatch.

    La sección Summary (Resumen) muestra la información principal proporcionada en la sección Log output (Resultado del registro) (la línea REPORT del registro de ejecución).

    La sección de Log output (Salida de registro) muestra el registro que Lambda genera para cada invocación. La función escribe estos registros en CloudWatch. La consola de Lambda muestra estos registros para su comodidad. Elija Click here (Haga clic aquí) para agregar registros al grupo de registros de CloudWatch y abra la página Log groups (Grupos de registro) en la consola CloudWatch.



Ejecute la función (elija Test) unas cuantas veces más para recopilar algunas métricas que puede ver en el siguiente paso.

Elija la pestaña Monitor (Monitorear). Esta página muestra gráficos de las métricas que Lambda envía a CloudWatch. 


---


Function

Una función es un recurso que puede invocar para ejecutar el código en Lambda. Una función tiene código para procesar los eventos que pasa a la función o que otros AWS servicios envían a la función. 


Trigger

Un desencadenador es un recurso o configuración que invoca una función de Lambda. Los desencadenadores incluyen los servicios de AWS que puede configurar para invocar una función 

Event

Un evento es un documento con formato JSON que contiene datos para que una función de Lambda los procese. El tiempo de ejecución convierte el evento en un objeto y lo pasa al código de la función. Cuando se invoca una función, se determina la estructura y el contenido del evento. 

Para ver la estructura de los Eventos de los distintos servicios de aws que pueden desencadenar la función lamnda: https://docs.aws.amazon.com/es_es/lambda/latest/dg/lambda-services.html


Paquete de implementación: Un archivo de archivo .zip que contiene su código de función y sus dependencias. 



---

Lambda administra la infraestructura que ejecuta el código, escalándola automáticamente en respuesta a las solicitudes entrantes. Cuando la función se invoca a mayor velocidad de la que una sola instancia de su función puede procesar eventos, Lambda amplía la capacidad ejecutando instancias adicionales. Cuando el tráfico disminuye, las instancias inactivas se bloquean o detienen. Solo paga por el tiempo que la función inicia o procesa eventos. 



---

- El código se ejecuta en un entorno que incluye el SDK for Python (Boto3), con credenciales de un rol de AWS Identity and Access Management (IAM) que usted administre. 

El controlador de la función de Lambda es el método del código de la función que procesa eventos. Cuando se invoca una función, Lambda ejecuta el método del controlador. Si el controlador existe o devuelve una respuesta, pasará a estar disponible para gestionar otro evento. 

Puede usar la siguiente sintaxis general al crear un controlador de funciones en Python:


def handler_name(event, context): 
    ...
    return some_value


El nombre del controlador de funciones de Lambda especificado en el momento de la creación de una función de Lambda se deriva de:

    El nombre del archivo en el que se encuentra la función del controlador de Lambda

    El nombre de la función del controlador de Python


Cuando Lambda invoca su controlador de función, el tiempo de ejecución de Lambda pasa dos argumentos al controlador de funciones:

    El primer argumento es el objeto de evento. Un evento es un documento con formato JSON que contiene datos para que una función de Lambda los procese. El tiempo de ejecución de Lambda convierte el evento en un objeto y lo pasa al código de la función. Por lo general, es del tipo Python dict. También puede ser list, str, intfloat, o el tipo NoneType.

    El objeto de evento contiene información del servicio de invocación. Cuando se invoca una función, se determina la estructura y el contenido del evento. Cuando un servicio AWS invoca su función, el servicio define la estructura del evento. Para obtener más información acerca de los eventos de los servicios de AWS, consulte Utilización de AWS Lambda con otros servicios.

    El segundo argumento es el objeto de contexto. Un objeto de contexto se pasa a su función de Lambda en tiempo de ejecución. Este objeto proporciona métodos y propiedades que facilitan información acerca de la invocación, la función y el entorno de tiempo de ejecución.


---

Cuando Lambda ejecuta su función, pasa un objeto context al controlador. Este objeto proporciona métodos y propiedades que facilitan información acerca de la invocación, la función y el entorno de ejecución. Para obtener más información sobre cómo se pasa el objeto de contexto al controlador de funciones, consulte Controlador de funciones de Lambda en Python.

Métodos de context

    get_remaining_time_in_millis: devuelve el número de milisegundos que quedan antes del tiempo de espera de la ejecución.

Propiedades de context

    function_name: el nombre de la función de Lambda.

    function_version: la versión de la función.

    invoked_function_arn: el nombre de recurso de Amazon (ARN) que se utiliza para invocar esta función. Indica si el invocador especificó un número de versión o alias.

    memory_limit_in_mb: cantidad de memoria asignada a la función.

    aws_request_id: el identificador de la solicitud de invocación.

    log_group_name: grupo de registros de para la función.

    log_stream_name: el flujo de registro de la instancia de la función.

    identity: (aplicaciones móviles) Información acerca de la identidad de Amazon Cognito que autorizó la solicitud.

        cognito_identity_id: la identidad autenticada de Amazon Cognito.

        cognito_identity_pool_id: el grupo de identidad de Amazon Cognito que ha autorizado la invocación.

    client_context: (aplicaciones móviles) Contexto de cliente proporcionado a Lambda por la aplicación cliente.

        client.installation_id

        client.app_title

        client.app_version_name

        client.app_version_code

        client.app_package_name

        custom: un elemento dict de valores personalizados establecidos por la aplicación cliente para móviles.

        env: un elemento dict de información de entorno proporcionado por el AWS SDK.

En el siguiente ejemplo se muestra una función de controlador que registra información de context. 


import time

def lambda_handler(event, context):   
    print("Lambda function ARN:", context.invoked_function_arn)
    print("CloudWatch log stream name:", context.log_stream_name)
    print("CloudWatch log group name:",  context.log_group_name)
    print("Lambda Request ID:", context.aws_request_id)
    print("Lambda function memory limits in MB:", context.memory_limit_in_mb)
    # We have added a 1 second delay so you can see the time remaining in get_remaining_time_in_millis.
    time.sleep(1) 
    print("Lambda time remaining in MS:", context.get_remaining_time_in_millis())

---
Devolver un valor

Si lo desea, el controlador puede devolver un valor. Lo que sucede con el valor devuelto depende del tipo de invocación y el servicio que invocó la función. Por ejemplo:

    Si utiliza el tipo de invocación RequestResponse, como Invocación síncrona, AWS Lambda devuelve el resultado de la llamada a la función Python al cliente que invoca la función de Lambda (en la respuesta HTTP a la solicitud de invocación, serializado en JSON). Por ejemplo, la consola de AWS Lambda utiliza el tipo de invocación RequestResponse, por lo que al invocar la función utilizando la consola, esta mostrará el valor devuelto.

    Si el controlador devuelve objetos que no se pueden serializar con json.dumps, el tiempo de ejecución devuelve un error.

    Si el controlador devuelve None, al igual que hacen las funciones de Python sin una instrucción return, el runtime devuelve null.



---

Implementar funciones Python Lambda con archivos .zip


El código de la función AWS Lambda se compone de scripts o programas compilados y sus dependencias. Utiliza un paquete de implementación para implementar su código de función en Lambda. Lambda admite dos tipos de paquetes de implementación: imágenes de contenedor y archivos .zip. 


El archivo.zip contiene el código de su función y cualquier dependencia utilizada para ejecutar el código de su función (si corresponde) en Lambda. Si su función depende solo de bibliotecas estándar o bibliotecas SDK AWS, no necesita incluir estas bibliotecas en su archivo.zip. 

Si el archivo .zip tiene más de 50 MB, es necesario cargarlo desde un bucket Amazon Simple Storage Service (AmazonS3). 


---


Paquete de implementación sin dependencias

Cree el archivo .zip para su paquete de implementación.

Creación del paquete de implementación

    Abra un símbolo del sistema y cree un directorio del proyecto my-math-function. Por ejemplo, en macOS:

mkdir my-math-function

Desplácese hasta el directorio del proyecto my-math-function.

cd my-math-function

Copie el contenido del código Python de ejemplo de GitHub

y guárdelo en un nuevo archivo llamado lambda_function.py. La estructura de directorios debería ser similar a la siguiente:

my-math-function$
| lambda_function.py

Agregue el archivo lambda_function.py a la raíz del archivo.zip.

zip my-deployment-package.zip lambda_function.py

Esto genera un archivo my-deployment-package.zip en el directorio del proyecto. El comando produce el resultado siguiente.

adding: lambda_function.py (deflated 50%)

Mediante un entorno virtual

Para actualizar una función Python con un entorno virtual

    Active el entorno virtual. Por ejemplo:

~/my-function$ source myvenv/bin/activate

Instale las bibliotecas con pip.

(myvenv) ~/my-function$ pip install requests

Desactive el entorno virtual.

(myvenv) ~/my-function$ deactivate

Cree un paquete de implementación con las bibliotecas instaladas en la raíz.

~/my-function$cd myvenv/lib/python3.8/site-packages
zip -r ../../../../my-deployment-package.zip .

El último comando guarda el paquete de implementación en la raíz del directorio my-function.
sugerencia

Una biblioteca puede aparecer en site-packages o dist-packages y la primera carpeta lib o lib64. Puede utilizar el comando pip show para localizar un paquete específico.

Agregue archivos de código de función a la raíz del paquete de implementación.

~/my-function/myvenv/lib/python3.8/site-packages$ cd ../../../../
~/my-function$ zip -g my-deployment-package.zip lambda_function.py

Cuando realice este paso, tendrá la siguiente estructura de directorio:

my-deployment-package.zip$
  │ lambda_function.py
  │ __pycache__
  │ certifi/
  │ certifi-2020.6.20.dist-info/
  │ chardet/
  │ chardet-3.0.4.dist-info/
  ...

---


mplementar el archivo .zip en la función

Para implementar el nuevo código en la función, cargue el nuevo paquete de implementación del archivo .zip. Puede utilizar la consola de Lambda para cargar un archivo .zip a la función o puede usar el comando de la CLI UpdateFunctionCode. 


El siguiente ejemplo carga un archivo denominado my-deployment-package.zip. Utilice el prefijo de archivo fileb:// para cargar el archivo .zip binario a Lambda. 


aws lambda update-function-code --function-name MyLambdaFunction --zip-file fileb://my-deployment-package.zip

---

AWS Lambda monitorea automáticamente funciones Lambda en su nombre e informa sobre las métricas a Amazon CloudWatch. Su función de Lambda viene con un grupo de registros de CloudWatch Logs y con un flujo de registro para cada instancia de su función. El entorno de tiempo de ejecución de Lambda envía detalles sobre cada invocación al flujo de registro y retransmite los registros y otras salidas desde el código de la función. 

Para generar registros desde el código de su función, puede utilizar el método print o cualquier biblioteca de registro que escriba en stdout o en stderr. En el siguiente ejemplo, se registran los valores de las variables de entorno y el objeto de evento. 


Cuando el código da lugar a un error, Lambda genera una representación JSON de este. Este documento de error aparece en el registro de invocación y, en el caso de invocaciones síncronas, en la salida.

Esta página describe cómo ver los errores de invocación de funciones de Lambda para el tiempo de ejecución de Python utilizando la consola de Lambda y la AWS CLI. 


---

# Practicas Recomendadas


- Separe el controlador de Lambda de la lógica del núcleo. 
- Utilice variables de entorno para pasar parámetros operativos a su función: Por ejemplo, si está escribiendo en un bucket de Amazon S3, en lugar de codificar de forma rígida el nombre del bucket, configúrelo como una variable de entorno. 
- Minimice el tamaño del paquete de implementación de acuerdo con las necesidades de su tiempo de ejecución. 
- Reutilice el entorno de ejecución para mejorar el rendimiento de la función. Inicialice los clientes de SDK y las conexiones de base de datos fuera del controlador de funciones 

---


na función de Lambda también tiene una política, que se denomina rol de ejecución, que la concede permiso para tener acceso a los servicios y recursos de AWS.




---

- From web
- From aws cli
- From aws extension vscode


- Triger Event
- S3 Event
- HTTP With Gateway


- Hasta 15 minutos de ejecución
- Muy barato.


----

Ejercicio

- Cree una funcion lamnda por defecto.
- Modifique el código en la consola de aws para que mueste la fecha en la que se ejecuto, y realice un print de event y context
- Prueba la función con el test por defecto.
- Observe el resultado

---

Ejercicio

Realice todos estos pasos desde su instancia EC2 conectada a Visual Studio Code.
- Cree una nueva carpeta
- Cree una nueva función que use la libreria pandas.
- Cree el paquete .zip
- Suba el fichero a un bucket de s3. Para ello cree un nuevo bucket.
- Ejecute el sieguiente comando para crear la función.

- Prueba la función desde la consola de aws.


---

Ejercicio

- Cree una función que se conecte a la API de los algoritmos de BME y descarge los datos del Santander.
- Empaquete todas las librerías que necesite usar usando un virtual enviroment.
- El api key tendra que estar en una variable de entorno.
- Una vez probada la función modifiquela para que guarde el csv en un bucket de s3. El nombre del fichero tendra el siguiente formato:


---

Ejercicio
- Cree una función lamnda que se ejecute una vez cada minuto y tenga un print que muestre la hora de ejecución.


---

Ejercicio

- Cree una función lamnda que se ejecute cuando un nuevo fichero se suba a un bucket s3. Para ello es necesario que cree un nuevo bucket
- La función tendrá que leer el fichero y procesarlo. Los ficheros que subiremos seran los ficheros de prueba de market data.
- La función tendrá que procesar el fichero para que la salida sea otro fichero csv, que guardaremos en otro bucket con el siguiente formato:


----

Ejercicio
- En este ejercicio vamos a crear un método get de un API usando lamnda y API Gateway.ç
- El método recivira dos parametros a y b y realizara su suma.
- Para ello el triger de la función sera un http y usaremos API Gateway para exponer el API a internet.


---


