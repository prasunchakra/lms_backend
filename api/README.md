### Serializer (General)

A **serializer** is a tool used to convert complex data structures, such as objects, into a format that can be easily stored or transmitted (e.g., JSON, XML) and vice versa. It enables seamless data exchange between systems or layers, such as APIs and databases.

### Django Serializer

In **Django**, serializers (provided by the **Django REST framework**) handle the following tasks:

- Transforming Django model instances or other data types into formats like JSON for APIs.
- Validating and converting incoming data back into Python objects.

#### Types of Django Serializers:

1. **ModelSerializer**:  
   Automatically generates serializer fields based on a Django model.

2. **Serializer**:  
   Offers more flexibility for custom data validation and representation.


---

### JWT (General)

**JSON Web Token (JWT)** is a compact, self-contained, and secure way to transmit information between parties as a JSON object. It is widely used for authentication and authorization in web applications. JWTs are signed using a secret (HMAC) or a public/private key pair (RSA/ECDSA), ensuring data integrity and authenticity.

#### Key Components of a JWT:
1. **Header**: Specifies the type of token (JWT) and the signing algorithm.
2. **Payload**: Contains claims (information) such as user ID, expiration time, etc.
3. **Signature**: Ensures the token hasn’t been tampered with.


### JWT Configurations in Django

In **Django**, JWT is typically implemented using the **Django REST framework (DRF)** along with the **djangorestframework-simplejwt** package.
