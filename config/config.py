import os

# Define the project root directory (one level up from config/)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")

    # MySQL Database URI
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://college:root@localhost/academic_data_management"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # File Upload Paths
    UPLOAD_FOLDER = os.path.join(PROJECT_ROOT, 'uploads')
    BACKUP_FOLDER = os.path.join(PROJECT_ROOT, 'backups')
