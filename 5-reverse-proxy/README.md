
```bash
cd 5-reverse-proxy
docker-compose down
docker-compose up -d --build
```

```
GET http://localhost:8080/api
```

Réponse attendue :

```json
{ "service": "Flask API", "message": "Hello from Flask!" }
```

Dans le navigateur : http://localhost:8080/site
