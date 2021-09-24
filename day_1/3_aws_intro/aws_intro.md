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

# Introducción a AWS

---
# Overview 

- Lanzada Internamente en 2002.
- Lanzada Publicamente en 2004.
- Relaunch with S3 y EC2 en 2006.
- Todo amazon.com migrado a AWS en 2010.
- Revenue 45$ Billion in 2020.
- Mas de 200 servicios.
---

![center](imgs/aws_periodic.jpg)

---


![center](imgs/cuadrant.png)

- 48% del segmento del mercado en IaaS.
- Lider durante más de 10 años.

---

IA Developer services:

![center](imgs/cudrant_ia.png)


---

# AWS Global Infrastructure

- Amazon EC2 está hospedado en varias ubicaciones de todo el mundo.

- 24 Regiones:

![center](imgs/regiones.png)


---

 Estas ubicaciones se componen de regiones, zonas de disponibilidad, Local Zones, AWS Outposts y zonas de Wavelength. Cada región es un área geográfica independiente.
 
 - Cada región de Amazon EC2 se ha diseñado para que esté totalmente aislada de las demás regiones de Amazon EC2. Con ello se consigue la mejor tolerancia a errores y estabilidad posibles. 

 - Las zonas de disponibilidad son varias ubicaciones aisladas dentro de cada región.

- Cuando lanza una instancia o servicio, puede seleccionar una zona de disponibilidad o dejar que se eliga automaticamete.

- Las regiones entre si estan conectadas con una red de muy alto anche de banda y rebundante.

- https://aws.amazon.com/es/about-aws/global-infrastructure/

---

- Cuando se consultan los recursos, solo se ven los recursos vinculados a la región especificada. 
- Esto se debe a que las regiones están aisladas entre sí y no replicamos automáticamente los recursos en distintas regiones. 

---
# Costes

- Los costes fundamentales son:
  - Compute: CPU y RAM
  - Storage: gastado o alocado.
  - Outbound Data Transfer: Trasnferencia hacia afuera.

- https://aws.amazon.com/es/pricing/
- https://calculator.aws
---

# Creación de la Cuenta

- https://aws.amazon.com/es/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all


---

# Billing Alarm 

- Usaremos mayoritariamente recursos de la capa free tier.
- Billing -> Billing Preferences --> FreeTier
- Cloudwatch: Permite crear alarmas sobre métricas por ejemplo facturación.
---


# AWS Identity and Access Management (IAM)

- Con AWS Identity and Access Management (IAM) jestionamos los usuarios y las politicas de acceso en AWS.
- La cuenta que acabas de crear es la Root Account: AWS recomienda no usarla.
- Debes crear cuenta para ti y otro usuarios.

---


![center](imgs/policies.png)

---

- IAM User: Representa una persona o service
- IAM Group: Collecion de usuarios
- IAM Role: Delegación (usado en servicios, lo vermos más adelante.)
- Podemos aplicar Policies a Usuarios, grupos o roles donde se especifican los permisos. 


---

# Metodos de Autentificación


- Access Key: Compuesta de: access key ID y secret access key. Usadas por ejemplo para AWS CLI o para hacer a AWS en tus programas.
- Password: para acceder para la AWS Management Console.


![center](imgs/key.png)


---

- Creamos un grupo y un usuario con policy: AdministratorAccess.

---

# Amazon Virtual Private Cloud (VPC)

- Espacio virtual donde puedes lanzar recursos.
- Porción aislada en una región de aws.

---

![center](imgs/vpc.png)

---

- Podemos tener subnets en diferentes aailability zones.
- Public subnets: tienen dirección IP publica. 
- Vemos la VPC por defecto.


---

# Servicios publicos y privados

![center](imgs/public.png)

---
# IaaS, PaaS, SaaS

![center](imgs/serverless.jpg)

https://aws.amazon.com/es/types-of-cloud-computing/

---


# Instalación de AWS y vscode extension

- https://aws.amazon.com/es/cli/
- Extension:
![center](imgs/extension.png)


---
# Documentación

https://docs.aws.amazon.com/index.html
