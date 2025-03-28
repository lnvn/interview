## Explaination for design

![API Gateway Architecture](./api-gateway-high-level-design.svg)

### 1. Load Balancer (Top Layer):
The load balancer is the entry point for incoming requests. It distributes traffic evenly among the API Gateways to ensure high availability and efficient use of resources.

It can be implemented using tools such as AWS Elastic Load Balancer (ELB), NGINX, etc., with sticky sessions enabled to ensure traffic remains directed to the same API Gateway. This helps optimize the efficiency of the core functionalities provided by the API Gateway.

### 2. API Gateway (Middle Layer):
The API Gateways handle the core functionalities of the system, such as:

- Authentication and Authorization.
- Request validation.
- Routing requests to appropriate backend services.
- Rate limiting and caching, this will implement by rate-limit core function built in part 1

Each API Gateway acts as a proxy between the client and the backend services.

### 3. Backend Services (Bottom Layer):
- These are the core application services responsible for executing the business logic.

- Services are divided into Service 1 and Service 2, ..., representing different functionalities or microservices.

- The architecture is designed to support scalability, as additional backend services can be added seamlessly.

- Each API Gateway can route requests to multiple backend service instances, improving fault tolerance and load distribution.

### Key Features of This Architecture:
- Scalability: Both the API Gateway layer and backend services can scale horizontally to handle increased load.

- Fault Tolerance: The use of a load balancer and multiple instances ensures the system remains operational even if one component fails.

- Modularity: Backend services are decoupled, making the architecture suitable for a microservices-based design.