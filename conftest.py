import pytest
import zipfile
import shutil
from settings import archive_path, extract_path


@pytest.fixture(scope='session', autouse=True)
def extraction_and_cleanup():
    """Фикстура с говорящим названием. Распаковывает архив и удаляет распакованное после тестов"""
    with zipfile.ZipFile(archive_path) as zf:
        zf.extractall(extract_path)

    yield

    shutil.rmtree(extract_path)
