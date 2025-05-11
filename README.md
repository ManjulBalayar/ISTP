# ISTP Research Website

A Django-based web application for displaying and analyzing Quality of Life (QOL) survey data across different towns and demographics. Link to website: www.agpolicyiowastate.org

## Features

- Interactive data visualization of QOL metrics
- Search functionality for towns
- Demographic filtering
- Multi-year comparison capabilities

## Technology Stack

- Python 3.9+
- Django 4.2
- MySQL 8+
- HTML/CSS/JavaScript
- Bootstrap for UI

## Local Development Setup

### Prerequisites

- Python 3.9 or higher
- MySQL 8.0 or higher
- pip (Python package manager)
- virtualenv (recommended)

### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd Django\ App
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv virt
   source virt/bin/activate  # On Windows, use `virt\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the `ISTP_website` directory with the following variables:
   ```
   DJANGO_SECRET_KEY=your_secret_key
   DJANGO_DEBUG=True
   DB_NAME=ISTP_SCHEMA
   DB_HOST=127.0.0.1
   DB_PORT=3306
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

5. Run migrations:
   ```
   cd ISTP_website
   python manage.py migrate
   ```

6. Start the development server:
   ```
   python manage.py runserver
   ```

## Testing

Run the test suite with:
```
python manage.py test webapp
```

## Deployment

### PythonAnywhere Deployment

1. Sign up for a PythonAnywhere account

2. Upload your code:
   - Via Git: `git push` to a repository, then clone on PythonAnywhere
   - Via direct upload: Upload files through PythonAnywhere dashboard

3. Create a virtualenv on PythonAnywhere and install requirements

4. Configure the web app in PythonAnywhere:
   - Set the WSGI configuration file to point to your project's wsgi.py
   - Configure static files
   - Set up environment variables

5. Set up MySQL database on PythonAnywhere

6. Run migrations and populate the database

Detailed deployment instructions can be found in the deployment documentation.

## Project Structure

- `ISTP_website/` - Main Django project directory
  - `webapp/` - Main application with views, models, and templates
  - `static/` - Static files (CSS, JS, images)
  - `logs/` - Application logs

## License

[Your License Information]

## Contact

[Your Contact Information]
