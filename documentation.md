# API Documentation

This document provides detailed information about the API endpoints, request/response formats, and usage examples.

## List and Create Persons

- **Endpoint**: `/api/persons/`
- **Method**: `GET` (List) and `POST` (Create)

### List Persons

**Request**
```http
GET /api/persons/

**Response**

{
    "success": true,
    "message": "Persons retrieved successfully",
    "data": [
        {
            "id": 1,
            "name": "John Doe"
        },
        {
            "id": 2,
            "name": "Jane Smith"
        }
    ]
}

### Create Persons
**Request**
POST /api/persons/

**Request Body**
{
    "name": "New Person"
}

**Response**
{
    "success": true,
    "message": "Person created successfully",
    "data": {
        "id": 3,
        "name": "New Person"
    }
}

### Retrieve, Update, and Delete Person
**Endpoint**: /api/persons/<person_id>/
**Method**: GET (Retrieve), PUT (Update), and DELETE (Delete)

### Retrieve Person

**Request**

```http
GET /api/persons/1/

**Response**

{
    "success": true,
    "data": {
        "id": 1,
        "name": "John Doe"
    }
}

### Update Person

**Request**

```http
PUT /api/persons/1/

**Request Body**
{
    "name": "Updated Person"
}

**Response**

{
    "success": true,
    "message": "Person updated successfully",
    "data": {
        "id": 1,
        "name": "Updated Person"
    }
}

### Delete Person

**Request**

```http
DELETE /api/persons/1/

**Response**

{
    "success": true,
    "message": "Person deleted successfully"
}

This API documentation provides information about the available endpoints, their methods, request/response formats, and usage examples.







