# Docker 
- Build Docker Image
```sudo docker build -t flask-name-age-sql .```

- Run Docker with Persistent Volume
```sudo docker run -d -p 5000:5000 -v ~/docker-learnings/flask-app-sqllite/flask-data:/app/data flask-name-age-sql```


