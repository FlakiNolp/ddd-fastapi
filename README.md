# FastAPI project with DDD and microservices
Example of using DDD (Domain driven design) together with an event-driven architecture.

The plan is to develop 5 custom microservices. 
At present, the first and primary application service is being developed.

The development plan is indicated at the end.
## Current Technologies:
- **fastapi** - for implementing web application API
- **sqlalchemy** - for interaction with PostgreSQL database
- **pydantic** - for data validation in fastapi
- **punq** - for dependency injection
- **pytest** - for testing functionality
- **dataclasses** - for implementing data storage and simplifying class development
- **pydantic-settings** - for creating configuration classes
- **docker and docker compose** - for simplification application deployment
## How to Launch
1. Fork repository
2. Clone the forked repository
3. Switch to the repository directory
4. Create an .env file using the .env.example file

## Project Roadmap
1. Develop domain entities and value of the microservice `app` ✅
2. Develop tests for domain entities and value objects `app` ✅
3. Add domain commands, events, and their handlers using mediator `app` ✅
4. Develop first RESTFUL API endpoint with sqlalchemy and punq injection `app` ✅
5. Add application deployment via docker compose ✅ 
6. Write endpoints, methods in the repository and commands in the mediator for:
   - The ability to create and delete projects ⏳
   - Adding and removing users from projects by the admin ⏳
   - The ability to change user roles in the project ⏳
   - Adding and deleting bank cards by the user ⏳
   - Changing the user's notification services ⏳
7. Develop auth microservice - for authentication ⏳
8. Add mongodb storage in docker compose ⏳
9. Develop logs microservice ⏳
10. Develop notification microservice ⏳
11. Develop realtime (websocket) microservice ⏳
## The future design of the project
The overall architecture of the project is presented in the `design` C4 model.

The web application includes the app service, which will be responsible for the main part of the web application.

Auth - for authenticating users and issuing new jwt keys.

Logs - provides a public API for sending logs to the server.

Notification - to send notifications to various services, it will be linked to the Logs service using Kafka.

Realtime service - to be able to receive incoming logs from the Logs service using Kafka and return them in real time via websocket.