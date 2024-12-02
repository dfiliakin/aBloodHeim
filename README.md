# aBloodHeim

## Setup
Setting up Python Virtual Environment
```
python -m venv .venv
source .venv/Scripts/activate
```

Setting up Node.js with TypeScript
```
npm install
```

## Client
Scripts
```
npm test
npm build
npm start:dev
npm start
```

## Server
uvicorn main:app --host 0.0.0.0 --port 8080 --reload

## Debugging
Testing login
```
# fail
curl -k -X POST https://127.0.0.1:8080/v0/auth/login -H "Content-Type: application/x-www-form-urlencoded" -d "username=a&password=a"

# success after verification (admin/admin should be created on db init step)
curl -k -X POST https://127.0.0.1:8080/v0/auth/login -H "Content-Type: application/x-www-form-urlencoded" -d "username=admin&password=admin"

# success with no verification (because of username == test)
curl -k -X POST https://127.0.0.1:8080/v0/auth/login -H "Content-Type: application/x-www-form-urlencoded" -d "username=test&password=any"
```

## Database
PostgreSQL latest
```
psql -U postgres
password: ****

CREATE DATABASE bloodheim;
\c bloodheim;

CREATE TABLE users;

INSERT INTO users (login, name, password)
VALUES
('admin', 'admin', 'admin');

curl -k https://127.0.0.1:8080/v0/users/admin
```
