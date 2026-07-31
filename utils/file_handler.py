import os
from flask import current_app
from werkzeug.utils import secure_filename

def get_upload_path(subfolder=None):
    """
    Returns the absolute path to the upload directory.
    If subfolder is provided, it is appended to the base upload path.
    Creates the directory if it does not exist.
    """
    base = current_app.config.get('UPLOAD_FOLDER')
    if not base:
        # Fallback if config is not loaded (though it should be)
        base = os.path.join(os.getcwd(), 'uploads')
        
    path = base
    if subfolder:
        path = os.path.join(base, subfolder)
    
    os.makedirs(path, exist_ok=True)
    return path

def get_backup_path():
    """
    Returns the absolute path to the backup directory.
    Creates the directory if it does not exist.
    """
    path = current_app.config.get('BACKUP_FOLDER')
    if not path:
        path = os.path.join(os.getcwd(), 'backups')
        
    os.makedirs(path, exist_ok=True)
    return path

def save_file(file, subfolder=None, filename=None):
    """
    Saves a Flask file object to the configured upload directory (or subfolder).
    Returns the absolute path of the saved file.
    """
    if not filename:
        filename = secure_filename(file.filename)
    
    directory = get_upload_path(subfolder)
    file_path = os.path.join(directory, filename)
    file.save(file_path)
    return file_path
