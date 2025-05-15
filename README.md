# landmarks-bih-backend
A backend service built with FastAPI that provides detailed data on landmarks, their associated cities, events, nearby restaurants, and accommodations — all within a specific country.

## 🧭 Overview
This project serves as a structured and efficient API for accessing information about:
  - 🗽 Landmarks: Cultural, historical, and natural sites.
  - 🏙️ Cities: Locations that contain landmarks.
  - 🎉 Events: Activities and occasions occurring near landmarks or within the city.
  - 🍽️ Restaurants: Dining options near landmarks or cities.
  - 🛏️ Accommodations: Lodging facilities available around landmarks or cities.

The system uses modern Python tooling and best practices to ensure a clean, maintainable, and high-performing backend.
## 🛠️ Tech Stack
  - Python 🐍 with FastAPI 🚀 for API development
  - Pydantic for data validation and serialization
  - Alembic 🛤️ for database migrations
  - PostgreSQL 🐘 as the primary relational database
  - Docker & Docker Compose 🐳 for containerization and orchestration

## 🚀 Getting Started
Prerequisites
Ensure you have the following installed:
  - Docker
  - Docker Compose

## 🔧 Run the Application
From the root of the project, start all services using:
  ```bash 
  docker-compose -f ./docker-compose.yaml up
  ```
This will:
  - Launch the FastAPI server
  - Set up and connect to a PostgreSQL database
  - Apply Alembic migrations (if configured to run on startup)

The API will be available at:
📍 http://localhost:8000

You can explore the API documentation via Swagger UI:
  📚 http://localhost:8000/docs

## 📂 Project Structure
```
.
├── src/
|   ├── app/
│   │   ├── database/         # Database setup and session management
│   │   ├── dto/              # Data Transfer Objects used across layers
│   │   ├── enums/            # Enum definitions for consistent values
│   │   ├── factory/          # Service object generators
│   │   ├── models/           # SQLAlchemy ORM models
│   │   ├── repositories/     # Data access layer interacting with the database
│   │   ├── routers/          # API route definitions and endpoints
│   │   ├── schemas/          # Shared Pydantic models (e.g., pagination) for request/query validation
│   │   ├── services/         # Business logic and service classes
│   │   ├── utils/            # Utility functions and helpers
│   │   └── main.py           # Entry point for the FastAPI app
├── migrations/               # Database migrations
├── docker-compose.yaml       # Docker Compose configuration
├── .docker/                  # Docker configuration
├── requirements.txt          # Python dependencies for the Landmarks Explorer API
└── README.md
```

## 📌 Notes
This project is designed to be easily extendable with new entities (e.g., tours, guides, reviews).
Environment-specific variables can be configured via a .env file (not included in repo).
All dependencies are pinned in requirements.txt.

## 📫 Contact
For questions or feedback, feel free to open an issue or reach out via GitHub.
