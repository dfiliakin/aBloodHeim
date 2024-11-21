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
curl -X POST http://127.0.0.1:8080/v0/auth/login -H "Content-Type: application/x-www-form-urlencoded" -d "username=a&password=a"
```
