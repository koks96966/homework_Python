import pytest
from sqlalchemy import text
from db import SessionLocal


@pytest.fixture
def session():
    """Отдельная сессия на каждый тест; в конце — откат и закрытие."""
    s = SessionLocal()
    try:
        yield s
    finally:
        s.rollback()
        s.close()


@pytest.fixture
def cleanup():
    """
    Возвращает колбэк, который нужно вызвать с SQL-запросом очистки.
    Гарантирует удаление данных даже при падении assert'ов.
    """
    queries = []
    yield queries

# Выполняем очистку в отдельной сессии, чтобы не зависеть от той, где упал тест
    s = SessionLocal()
    try:
        for q in queries:
            s.execute(text(q))
        s.commit()
    finally:
        s.close()
