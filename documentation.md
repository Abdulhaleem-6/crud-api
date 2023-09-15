# API Documentation

This document provides detailed information about the API endpoints, request/response formats, and usage examples.

## List and Create Persons

- **Endpoint**: `/api/`
- **Method**: `GET` (List) and `POST` (Create)

### List Persons

**Request**
```http
GET /api/

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
POST /api/

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
**Endpoint**: /api/<person_id>/
**Method**: GET (Retrieve), PUT (Update), and DELETE (Delete)

### Retrieve Person

**Request**

```http
GET /api/{person_id}/

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
PUT /api/{person_id}/

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
DELETE /api/{person_id}/

**Response**

{
    "success": true,
    "message": "Person deleted successfully"
}

This API documentation provides information about the available endpoints, their methods, request/response formats, and usage examples.







