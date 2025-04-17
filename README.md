# Employee Data API (3-Hour Challenge)

This project is a Django REST Framework-based backend system for generating, storing, and analyzing synthetic employee data.

## Setup

1. **Clone the repository**:
   ```bash
   git clone <your-repository-link>
   cd <your-project-directory>
2. **Install dependencies:**:
   ```
   pip install -r requirements.txt
   ```
3. **Create a .env file using .env.example:**:
   ```
   cp .env.example .env
   Update your .env with the PostgreSQL connection string.
   ```
4. **Run migrations:**:
   ```
   python manage.py migrate
   ```
   
5. **Run Tests:**:
   ```
   python manage.py test
   ```
5. **Run the development server:**:
   ```
   python manage.py runserver
   ```
6. **Endpoint API Docs:**:
   ```
   http://localhost:8000/swagger/
   ```
7. **Endpoint For Chart of Employee Performance:**:
   ```
   http://localhost:8000/charts/
   ```
7. **Final:**:
   ```
   Enjoy API Endpoints
   ```