# Django REST Framework Complete Authentication API with Simple JWT

This project implements a complete authentication system using **Django REST Framework (DRF)** and **Simple JWT** for token-based authentication. It allows users to register, log in, refresh their tokens, and access protected endpoints, making it ideal for applications requiring secure user authentication.

## Features

- **User Registration**: Create new users with custom user fields.
- **User Login**: Authenticate users using JWT tokens.
- **Token Refresh**: Refresh JWT tokens without re-authenticating.
- **Secure Endpoints**: Protect endpoints with JWT authentication.
- **Postman Collection**: Pre-configured Postman collection for easy API testing.

## Installation

Follow the steps below to set up the project on your local machine.

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/abdurrahimcs50/django-rest-auth-api-jwt.git
   cd django-rest-auth-api-jwt
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv env
   ```

3. **Activate the virtual environment**:

   - On Windows:

     ```bash
     env\Scripts\activate
     ```

   - On Mac/Linux:

     ```bash
     source env/bin/activate
     ```

4. **Install the required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

5. **Run migrations**:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Start the server**:

   ```bash
   python manage.py runserver
   ```

   After running the server, the application will be available at `http://localhost:8000`.

### Postman Collection

The project includes a **Postman Collection** to easily test the authentication endpoints. Import the file `django_auth_api_jwt.postman_collection` into Postman and start testing the authentication flow.

## API Endpoints

1. **POST** `/api/register/` - Register a new user.
   - **Request Body**:
     ```json
     {
       "username": "user_name",
       "password": "user_password",
       "email": "user_email"
     }
     ```

2. **POST** `/api/login/` - Log in and receive JWT tokens.
   - **Request Body**:
     ```json
     {
       "username": "user_name",
       "password": "user_password"
     }
     ```

   - **Response**:
     ```json
     {
       "access": "JWT_ACCESS_TOKEN",
       "refresh": "JWT_REFRESH_TOKEN"
     }
     ```

3. **POST** `/api/token/refresh/` - Refresh the JWT token.
   - **Request Body**:
     ```json
     {
       "refresh": "JWT_REFRESH_TOKEN"
     }
     ```

   - **Response**:
     ```json
     {
       "access": "NEW_JWT_ACCESS_TOKEN"
     }
     ```

## Running the Application

Once the server is running, you can access the application in your web browser at `http://localhost:8000`.

- **Registration**: Use the `POST /api/register/` endpoint to create a new user.
- **Login**: Use the `POST /api/login/` endpoint to authenticate the user and retrieve the JWT tokens.
- **Refresh Token**: Use the `POST /api/token/refresh/` endpoint to refresh the access token when expired.

## Contributing

We welcome contributions! If you find any bugs or have suggestions for improvements, feel free to create an issue or submit a pull request.

### How to Contribute

1. Fork the repository.
2. Clone your fork to your local machine:
   ```bash
   git clone https://github.com/your_username/django-rest-auth-api-jwt.git
   cd django-rest-auth-api-jwt
   ```

3. Create a new branch for your changes:
   ```bash
   git checkout -b feature/YourFeatureName
   ```

4. Make your changes and commit them:
   ```bash
   git commit -m "Add a descriptive commit message"
   ```

5. Push your changes to your fork:
   ```bash
   git push origin feature/YourFeatureName
   ```

6. Open a pull request to the main repository.

### Guidelines

- **Code Quality**: Please ensure your code follows best practices and is well-documented.
- **Testing**: If applicable, include tests to verify your changes.
- **Documentation**: Update the README or other documentation if your changes affect usage.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.

## Contact

For any questions or suggestions, feel free to reach out:

- **Email**: admin@rahim.com.bd
- **LinkedIn**: [MD Abdur Rahim](https://www.linkedin.com/in/abdurrahimcs50/)
- **Website**: [www.rahim.com.bd](http://www.rahim.com.bd)
```

