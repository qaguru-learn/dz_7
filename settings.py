import os

current_file = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file)
files_path = os.path.join(current_dir, 'files')
archive_path = os.path.abspath('source')
archive = os.path.join(archive_path, 'archive.zip')
