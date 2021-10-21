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

# Amazon DynamoDB

---

- Amazon DynamoDB es un servicio de base de datos NoSQL totalmente administrado que ofrece un rendimiento rápido y predecible, así como una perfecta escalabilidad.
- Muy sencillo de utilizar usando python.

---




---
# Ejercico
- Crea una tabla que tenga el siguiente esquema:
```python
    KeySchema=[
        {
            'AttributeName': 'VALOR',
            'KeyType': 'HASH'  # Partition key
        },
        {
            'AttributeName': 'TIME',
            'KeyType': 'RANGE'  # Sort key
        }
```


