<h1>FastAPI project with DDD and microservices</h1>
Example of using DDD (Domain driven design) together with an event-driven architecture. The plan is to develop 5 custom microservices. 
At present, the first and primary application service is being developed. The development plan is indicated at the end.
<h2>Current Technologies:</h2>
<ul>
    <li>fastapi - for implementing web application API</li>
    <li>sqlalchemy - for interaction with PostgreSQL database</li>
    <li>pydantic - for data validation in fastapi</li>
    <li>punq - for dependency injection</li>
    <li>pytest - for testing functionality</li>
    <li>dataclasses - for implementing data storage and simplifying class development</li>
    <li>pydantic-settings - for creating configuration classes</li>
    <li>docker and docker compose - for simplification application deployment</li>
</ul>
<h2>How to Launch</h2>
<ol>
    <li>Fork repository</li>
    <li>Clone the forked repository</li>
    <li>Switch to the repository directory</li>
    <li>Create an .env file using the .env.example file</li>
</ol>

<h2>Project Roadmap</h2>
<ol>
    <li>Develop domain entities and value of the microservice `app` ✅</li>
    <li>Develop tests for domain entities and value objects `app` ✅</li>
    <li>Add domain commands, events, and their handlers using mediator `app` ✅</li>
    <li>Develop first RESTFUL API endpoint with sqlalchemy and punq injection `app` ✅</li>
    <li>Add application deployment via docker compose ✅ </li>
    <li>Write endpoints, methods in the repository and commands in the mediator for: ⏳</li>
    <ul>
        <li>The ability to create and delete projects.</li>
        <li>Adding and removing users from projects by the admin.</li>
        <li>The ability to change user roles in the project.</li>
        <li>Adding and deleting bank cards by the user.</li>
        <li>Changing the user's notification services.</li>
    </ul>
    <li>Develop auth microservice - for authentication</li>
    <li>Add mongodb storage in docker compose</li>
    <li>Develop logs microservice</li>
    <li>Develop notification microservice</li>
    <li>Develop realtime (websocket) microservice</li>
</ol>
<h2>The future design of the project</h2>
The overall architecture of the project is presented in the `design` C4 model.<br>
The web application includes the app service, which will be responsible for the main part of the web application.<br>
Auth - for authenticating users and issuing new jwt keys.<br>
Logs - provides a public API for sending logs to the server.<br>
Notification - to send notifications to various services, it will be linked to the Logs service using Kafka.<br>
Realtime service - to be able to receive incoming logs from the Logs service using Kafka and return them in real time via websocket.