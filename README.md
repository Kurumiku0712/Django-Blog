# Personal Blog Website

This is a personal blog website built using Django 5.0.6 and Bootstrap. The website is designed to be simple yet functional, allowing users to post and view blog articles. The project uses MySQL as the database.
Here is the website link to my personal blog: https://kurumiku.pythonanywhere.com/

## Installation

### Prerequisites

- Python 3.10
- Django 5.0.6
- MySQL 5.7

### Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Install `pymysql` for MySQL integration:**

    ```sh
    pip install pymysql
    ```

5. **Set up the MySQL database:**

    - Create a new MySQL database.
    - Update the `DATABASES` setting in `settings.py` with your MySQL database credentials:

      ```python
      DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.mysql',
              'NAME': 'your_database_name',
              'USER': 'your_database_user',
              'PASSWORD': 'your_database_password',
              'HOST': 'localhost',  # Or the IP address of your database server
              'PORT': '3306',
          }
      }
      ```

6. **Apply the database migrations:**

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```


7. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

