# DistributedSystemsLab
## 12 FACTOR APP APPLICATION

Twelve-factor apps are a set of good practices designed to create cloud-native web applications.

---

### 1. Unique codebase
- We have one Git repository containing all our app code:  
  https://github.com/849183/DistributedSystemsLab/tree/main  
- We work mainly on the `main` branch, with feature/testing branches that all derive from the same codebase.  
- Evidence: see the `.gitignore` file—no parallel copies of code.

---

### 2. Dependencies
- All dependencies are listed in `requirements.txt`:  
  https://github.com/849183/DistributedSystemsLab/blob/main/app/backend/requirements.txt  
- We use containers and virtual environments to isolate and install those dependencies.

---

### 3. Config
- Configuration is stored in environment variables.  
- In `app/backend/src/main.py` we load:  
  ```python
  DATABASE_URL = os.getenv(
      "DATABASE_URL",
      "postgresql://user:Welcome1.@db:5432/shopApp"
  )
  ```

---
### 4. Backing services
  Databases, message queues, cache stores, etc., are attached as backing services and connected via URLs or credentials in configuration.The `docker-compose.yml` is an example of using backing services as external resources.   
  In `docker-compose.yml`, the database is defined as an external resource:
  ```yaml
  services:
    backend:
      environment:
        DATABASE_URL: postgresql://user:Welcome1.@db:5432/shopApp
```
---

### 5. Build, Release, Run
Strictly separate build and run stages.
-	Build: the backend image is constructed with docker-compose build according to the dockerfile
- Release: when `docker_compose` up is executed, the service with the external configuration is created
- Run: execute the app in the execution environment via docker-compose up

---
### 6. Port binding
Export services via port binding. At the `docker-compose.yml` the API is exposed towards the port 8000:8000
•	The app is self-contained and serves HTTP by binding to a port.
•	No external web server is required

```yaml
services:
  backend:
    build:
      context: ./app/backend
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    depends_on:
      - db
    environment:
      DATABASE_URL: postgresql://user:Welcome1.@db:5432/shopApp
```
---

### 7.Concurrency
Scale out via the process model.
•	Use multiple processes (workers, web dynos) to handle different workloads.
•	Define process types in a process formation.
Kubernetes manifests are an exaplme of how this factor is used.
`.yaml manifests` (deployment manifests).

---

### 8. Disposability
Maximize robustness with fast startup and graceful shutdown.
•	Processes should start up quickly and handle SIGTERM properly.
•	Enables rapid scaling and deployment.
At the `deploy.yaml` file the `readinessProbe` ensures disposability that grants the orchester when will the pod be ready.

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: postgres
  namespace: shopapp
spec:
  serviceName: postgres-headless
  replicas: 1
  …
  containers:
    - image: postgres:16
      env:
        - name: POSTGRES_USER   # …
      volumeMounts:
        - name: data
          mountPath: /var/lib/postgresql/data
        - name: init-sql
          mountPath: /docker-entrypoint-initdb.d
      readinessProbe:
        exec: ["pg_isready","-U","user"]
        initialDelaySeconds: 10
        periodSeconds: 10
  volumeClaimTemplates:
    - name: data
      resources:
        requests:
          storage: 5Gi
```
---
### 9.Dev/Prod Parity

Keep development, staging, and production as similar as possible.
The dockerfile is both used in development (docker-compose) as in production (Kubernetes).

---

### 10.Logs
There are no `.logs` files, the messages are redirected to STDOUT and collected by the orchestrer.

---
### 11. Admin processes
Any administrative task (data base migrations…) must be executed as a unique and isolated process but always:
Use the same codebase and config as the regular app processes.
At `app/DB/db_init.sql` and `basic_commands.txt` scripts information about administration processes can be found.

---

### 12. Processes
Execute the app as one or more stateless processes. Any data that needs to persist must be stored in a backing service.
At the `tests/ ` it can be appreciated that the app runs as a light web process (uvicorn) and in a separate way the tests in another autonomous process `(pytest tests/)`.




