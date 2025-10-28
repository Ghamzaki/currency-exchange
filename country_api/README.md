# Country Currency & Exchange API

This is a FastAPI application that provides a RESTful API for retrieving and managing country and currency exchange information. It fetches country data from an external API (restcountries.com) and stores it in a MySQL database.

## Features

- Fetch country data from `restcountries.com`.
- Store country data in a MySQL database.
- CRUD operations for country data via API endpoints.
- Robust error handling for external API calls and database operations.

## Setup Instructions

### 1. Database Setup

Ensure you have a MySQL database server running. Create a new database for this project (e.g., `country_db`).

### 2. Environment Variables

Create a `.env` file in the `country_api` directory with your database credentials:

```
DB_HOST=your_database_host
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_NAME=your_database_name
```

### 3. Install Dependencies

Navigate to the `country_api` directory and install the required Python packages:

```bash
pip install fastapi uvicorn mysql-connector-python python-dotenv requests
```

## How to Run the Application

1.  Navigate to the `country_api` directory in your terminal:

    ```bash
    cd country_api
    ```

2.  Run the FastAPI application using Uvicorn:

    ```bash
    uvicorn main:app --reload
    ```

    The `--reload` flag will make the server restart automatically on code changes.

3.  Once the server is running, you can access the API documentation (Swagger UI) at `http://127.0.0.1:8000/api/v1/docs`.

## API Endpoints

All API endpoints are prefixed with `/api/v1`.

-   **GET `/api/v1/countries`**: Retrieve a list of all countries.
-   **GET `/api/v1/countries/{country_id}`**: Retrieve a single country by its ID.
-   **POST `/api/v1/countries`**: Add a new country to the database.
    *   **Request Body Example**:
        ```json
        {
            "name": "New Country",
            "capital": "New Capital",
            "region": "New Region",
            "population": 1000000,
            "flag": "https://example.com/flag.svg",
            "currency_code": "XYZ"
        }
        ```
-   **PUT `/api/v1/countries/{country_id}`**: Update an existing country by its ID.
    *   **Request Body Example**:
        ```json
        {
            "name": "Updated Country Name",
            "capital": "Updated Capital"
        }
        ```
-   **DELETE `/api/v1/countries/{country_id}`**: Delete a country by its ID.
-   **POST `/api/v1/fetch-countries`**: Fetch country data from `restcountries.com` and store it in the database.
