apiVersion: apps/v1
kind: Deployment
metadata:
  name: flask-app
  labels:
    app: flask
spec:
  replicas: 1
  selector:
    matchLabels:
      app: flask
  template:
    metadata:
      labels:
        app: flask
    spec:
      containers:
        - name: flask
          image: LOCATION-docker.pkg.dev/PROJECT_ID/REPO/IMAGE:SHORT_SHA
          ports:
            - containerPort: 8080
          resources:
            requests:
              cpu: 100m
              memory: 128Mi
            limits:
              cpu: 100m
              memory: 128Mi
---
apiVersion: v1
kind: Service
metadata:
  name: flask-svc
  labels:
    app: flask
spec:
  selector:
    app: flask
  ports:
    - port: 80
      targetPort: 8080
  type: LoadBalancer
