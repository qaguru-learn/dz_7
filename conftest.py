import os
import pytest
import zipfile
import shutil
from settings import archive_path, files_path, archive


@pytest.fixture(scope='session', autouse=True)
def zip_to_archive():
    """Запаковывает в архив файлы и удаляет архив после тестов"""
    if not os.path.exists(archive_path):
        os.mkdir(archive_path)
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as zp:
        for file in os.listdir(files_path):
            zp.write(os.path.join(files_path, file), file, compress_type=zipfile.ZIP_DEFLATED)

    yield

    shutil.rmtree(archive_path)
