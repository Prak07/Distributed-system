# Distributed System Simulation with Django

This project demonstrates a distributed system simulation using Django where different types of data (Users, Orders, Products) are stored in separate SQLite databases. The program also simulates concurrent insertions into these databases using threads.

## Features
- Separate SQLite databases for `Users`, `Products`, and `Orders`.
- Models for `Users`, `Products`, and `Orders` with application-level validation.
- A management command to handle concurrent data insertions using threading.
- Easy-to-extend and modular architecture.

## Setup Instructions

### Prerequisites
- Python 3.8+
- Django 4.x

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Prak07/distributed-system.git
   cd distributed-system
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations to set up the databases:
   ```bash
   python manage.py makemigrations
   python manage.py migrate --database=users
   python manage.py migrate --database=products
   python manage.py migrate --database=orders
   ```

### Usage
1. Run the management command to insert data concurrently:
   ```bash
   python manage.py insert_data
   ```


## Configuration
### Database Settings
Three separate SQLite databases are configured in `settings.py`:
- `users.db`: Stores `Users` model data.
- `products.db`: Stores `Products` model data.
- `orders.db`: Stores `Orders` model data.

Database routing is managed in `core/routers.py`.

### Validation Rules
All validation is handled in the application logic:
- `Users` table: Ensures no duplicate emails.
- `Products` table: Ensures `price` is a positive number.
- `Orders` table: Ensures valid `user_id`, `product_id`, and `quantity`.



