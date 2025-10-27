# 🍋 LittleLemon API — Django REST Framework

## Overview

The **LittleLemon API** is a RESTful backend built with **Django** and **Django REST Framework (DRF)** for managing restaurant operations such as **menu items**, **table bookings**, and **user accounts**.

It exposes endpoints for CRUD operations and user authentication, following REST best practices with clear separation of concerns between models, serializers, and view logic.

---

## 🧩 Architecture Overview

| Component        | Description                                                               |
| ---------------- | ------------------------------------------------------------------------- |
| **Framework**    | Django 5.x, Django REST Framework                                         |
| **Database**     | MySQL / SQLite (configurable in `settings.py`)                            |
| **Auth System**  | Token-based authentication via `rest_framework.authtoken` and `djoser`    |
| **Core Modules** | `Menu` and `Booking` models within the `restaurant` app                   |
| **API Format**   | JSON-based RESTful API with standard HTTP methods and status codes        |
| **Tests**        | Unit tests for models and views using Django’s built-in testing framework |

---

## 📂 Project Structure

```

littlelemon/
│
├── restaurant/
│   ├── models.py          # Defines Menu and Booking models
│   ├── serializers.py     # Serializers for Menu, Booking, and User models
│   ├── views.py           # DRF views and viewsets
│   ├── urls.py            # App-level routes (/menu/, /booking/)
│
├── littlelemon/
│   ├── urls.py            # Root URL config and DRF router registrations
│
├── tests/
│   ├── test_models.py     # Unit tests for model **str**() methods
│   ├── test_views.py      # API tests for Menu and Booking endpoints
│
└── manage.py

```

---

## 🧱 Data Models

### **Menu**

Represents individual dishes or food items.

| Field       | Type                                            | Description                    |
| ----------- | ----------------------------------------------- | ------------------------------ |
| `title`     | `CharField(max_length=255)`                     | Name of the dish               |
| `price`     | `DecimalField(max_digits=10, decimal_places=2)` | Price of the item              |
| `inventory` | `IntegerField`                                  | Available stock                |
| `__str__`   | returns `"<title> : <price>"`                   | Readable string representation |

---

### **Booking**

Represents a restaurant table booking.

| Field          | Type                                  | Description                      |
| -------------- | ------------------------------------- | -------------------------------- |
| `name`         | `CharField(max_length=255)`           | Customer’s name                  |
| `no_of_guests` | `PositiveIntegerField`                | Number of guests                 |
| `booking_date` | `DateTimeField(default=timezone.now)` | Date and time of the reservation |
| `__str__`      | returns `"<name> @ <date>"`           | Readable string representation   |

---

## 🔐 Authentication

The API uses **token-based authentication**.  
You can obtain an authentication token using:

**POST** `/api-token-auth/`

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

Response:

```json
{ "token": "<YOUR_AUTH_TOKEN>" }
```

Include the token in subsequent requests:

```
Authorization: Token <YOUR_AUTH_TOKEN>
```

---

## 🌐 API Endpoints

### **Menu Endpoints** (Public)

| Method          | Endpoint                 | Description                  |
| --------------- | ------------------------ | ---------------------------- |
| `GET`           | `/restaurant/menu/`      | List all menu items          |
| `POST`          | `/restaurant/menu/`      | Create a new menu item       |
| `GET`           | `/restaurant/menu/<id>/` | Retrieve a single menu item  |
| `PUT` / `PATCH` | `/restaurant/menu/<id>/` | Update an existing menu item |
| `DELETE`        | `/restaurant/menu/<id>/` | Delete a menu item           |

**Example Request:**

```json
POST /restaurant/menu/
{
  "title": "Pasta Alfredo",
  "price": "12.99",
  "inventory": 25
}
```

---

### **Booking Endpoints** (Authenticated)

| Method          | Endpoint                           | Description                        |
| --------------- | ---------------------------------- | ---------------------------------- |
| `GET`           | `/restaurant/booking/tables/`      | List all bookings (requires token) |
| `POST`          | `/restaurant/booking/tables/`      | Create a new booking               |
| `GET`           | `/restaurant/booking/tables/<id>/` | Retrieve a booking by ID           |
| `PUT` / `PATCH` | `/restaurant/booking/tables/<id>/` | Update a booking                   |
| `DELETE`        | `/restaurant/booking/tables/<id>/` | Cancel a booking                   |

**Example Request:**

```json
POST /restaurant/booking/tables/
{
  "name": "Arpita",
  "no_of_guests": 2,
  "booking_date": "2025-10-27T18:30:00Z"
}
```

---

### **User Endpoints** (Authenticated)

| Method | Endpoint                          | Description               |
| ------ | --------------------------------- | ------------------------- |
| `GET`  | `/restaurant/booking/users/`      | List all registered users |
| `GET`  | `/restaurant/booking/users/<id>/` | Retrieve user details     |

**Response Example:**

```json
{
  "id": 1,
  "username": "admin",
  "email": "admin@example.com",
  "is_staff": true
}
```

---

## ⚙️ Running the Project Locally

```bash
# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Create a superuser (optional)
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

Visit:

- **API Root** → [http://localhost:8000/](http://localhost:8000/)
- **Menu Endpoint** → [http://localhost:8000/restaurant/menu/](http://localhost:8000/restaurant/menu/)
- **Bookings Endpoint** → [http://localhost:8000/restaurant/booking/tables/](http://localhost:8000/restaurant/booking/tables/)

---

## 🧪 Running Tests

The project includes tests for models and views.

```bash
python manage.py test
```

**Test coverage:**

- `test_models.py` — Validates string representation of models
- `test_views.py` — Tests `GET /restaurant/menu/` API response

---

## 🧰 Testing the API in Insomnia

You can test all endpoints using **Insomnia**, **Postman**, or any REST client:

1. **Start the Django server:**

   ```bash
   python manage.py runserver
   ```

2. **Create a new request:**

   - Set **Method** → `GET`, `POST`, `PUT`, or `DELETE`
   - Set **URL** → `http://localhost:8000/restaurant/menu/` (or another endpoint)
   - For protected routes, go to **Headers** and add:

     ```
     Key: Authorization
     Value: Token <YOUR_AUTH_TOKEN>
     ```

   - For `POST` or `PUT` requests, choose **Body → JSON** and add:

     ```json
     {
       "title": "Pizza Margherita",
       "price": "9.99",
       "inventory": 20
     }
     ```

3. **Send the request** and inspect:

   - HTTP status codes (`200`, `201`, `400`, `401`)
   - Serialized response data
   - Authentication behavior and permissions

This approach helps verify all CRUD operations, authentication, and serialization correctness.

---

## 💡 Design Notes

- **Extensible Architecture:** Easy to add new models (e.g., Reviews, Orders).
- **DRF Router Integration:** Simplifies URL registration and versioning.
- **Token Auth:** Secures Booking and User endpoints.
- **Validation:** DRF handles request parsing, type validation, and error responses automatically.
- **Modularity:** Each app (e.g., `restaurant`) is independently testable and reusable.

---

## 🚀 Future Enhancements

- Add **pagination** and **filtering** for menu and booking queries.
- Integrate **JWT Authentication** for scalable token management.
- Add **rate limiting** and **role-based permissions**.
- Build **frontend integration** (React or Vue) for real-time booking management.
