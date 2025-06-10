# IPC Web Application

This is a Django-based web application for IPC monitoring and machine learning services.

## Prerequisites

- Python 3.x
- Django (latest version)
- Web browser (Chrome, Firefox, Safari, or Edge)

## Getting Started

Follow these steps to run the application locally:

1. Open a terminal or command prompt

2. Navigate to the project directory:
   ```bash
   cd path/to/PFE/IPC/web
   ```
dir instead of ls

3. Install required dependencies (if not already installed):
   ```bash
   pip install django
   ```

4. Start the Django development server:
   ```bash
   python manage.py runserver
   ```

5. Open your web browser and visit:
   ```
   http://localhost:8000
   ```
   or
   ```
   http://127.0.0.1:8000
   ```

## Project Structure

- `api/` - API endpoints
- `sensor_ml/` - Sensor machine learning components
- `ml_monitor/` - Machine learning monitoring
- `ml_service/` - Machine learning services
- `monitoring/` - Monitoring components
- `dashboard/` - Main dashboard application
- `manage.py` - Django management script

## Stopping the Server

To stop the server, press `Ctrl+C` in the terminal where the server is running.

## Troubleshooting

If you encounter any issues:

1. Make sure you're in the correct directory (PFE/IPC/web)
2. Check if Django is properly installed
3. Ensure port 8000 is not being used by another application
4. Try running the server on a different port if 8000 is occupied:
   ```bash
   python manage.py runserver 8001
   ```

## Additional Notes

- This is a development server, not suitable for production use
- The server will automatically reload when you make changes to the code
- Database is using SQLite (db.sqlite3) 