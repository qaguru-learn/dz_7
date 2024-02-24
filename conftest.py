import os

import pytest
import zipfile
import shutil
from settings import archive_path, extract_path, files_path

archive = os.path.join(archive_path, 'archive.zip')


@pytest.fixture(scope='session', autouse=True)
def zip_to_archive():
    """Запаковывает в архив файлы и удаляет архив после тестов"""
    os.mkdir(archive_path)
    with zipfile.ZipFile(archive, 'w') as zp:
        for file in os.listdir(files_path):
            zp.write(os.path.join(files_path, file), compress_type=zipfile.ZIP_DEFLATED)

    yield

    shutil.rmtree(archive_path)


@pytest.fixture(scope='function', autouse=True)
def extract_archive():
    """Распаковывает архив"""
    os.mkdir(extract_path)
    with zipfile.ZipFile(archive, 'w') as zp:
        zp.extractall(extract_path)
    yield
    shutil.rmtree(extract_path)
