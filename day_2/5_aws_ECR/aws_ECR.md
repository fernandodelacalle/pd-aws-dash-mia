https://docs.aws.amazon.com/AmazonECS/latest/userguide/docker-basics.html


Amazon Elastic Container Registry (Amazon ECR) es unAWSUn servicio de registro de imágenes de contenedor administrado de seguro, escalable y fiable.



Amazon ECR es un servicio administrado de registro de Docker de AWS. Puede utilizar la CLI de Docker para insertar, extraer y administrar imágenes en suAmazon ECRrepositorios. Para obtener información detallada sobre el producto Amazon ECR, casos prácticos destacados de clientes y preguntas frecuentes, consulte las páginas de detalles del producto Amazon Elastic Container Registry.

Para esta sección, se necesita lo siguiente:

    Tener instalada y configurada la AWS CLI. Si no ha instalado la AWS CLI en el sistema, consulte Instalación de la AWS Command Line Interface en la AWS Command Line Interface Guía del usuario.

    El usuario debe tener los permisos necesarios de IAM para tener acceso al servicio Amazon ECR. Para obtener más información, consulteAmazon ECRPolíticas administradas de.

Etiquetado de la imagen y envío a Amazon ECR

    Cree un repositorio de Amazon ECR para almacenar su imagen hello-world. En los resultados, anote el repositoryUri. 
    aws ecr create-repository --repository-name hello-repository --region region

Se puede crear tambien el repositorio en la consola de Amazon ECR. 




Etiquete la imagen de hello-world con el valor de repositoryUri del paso anterior.

docker tag hello-world aws_account_id.dkr.ecr.region.amazonaws.com/hello-repository

Ejecute el comando aws ecr get-login-password. Especifique el URI del registro en el que desea autenticar. Para obtener más información, consulte Autenticación del registro en la Guía del usuario de Amazon Elastic Container Registry.

aws ecr get-login-password | docker login --username AWS --password-stdin aws_account_id.dkr.ecr.region.amazonaws.com

Salida:

Login Succeeded

Envíe la imagen a Amazon ECR con el valor repositoryUri del paso anterior.

    docker push aws_account_id.dkr.ecr.region.amazonaws.com/hello-repository



