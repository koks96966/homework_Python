from sqlalchemy import text


def test_create_student(session):
    test_user_id = 99981  # уникальный ID для теста
    test_level = "Junior"

    # Вставляем с явным ID
    session.execute(
        text("INSERT INTO student (user_id, level) VALUES (:uid, :lvl)"),
        {"uid": test_user_id, "lvl": test_level}
    )
    session.commit()

    # Проверяем, что строка появилась
    check = session.execute(
        text("SELECT level FROM student WHERE user_id = :uid"),
        {"uid": test_user_id}
    )
    found_level = check.scalar()

    assert found_level == test_level, (
        f"Ожидали уровень '{test_level}', получили '{found_level}'"
    )

    # Очистка
    session.execute(
        text("DELETE FROM student WHERE user_id = :uid"),
        {"uid": test_user_id}
    )
    session.commit()
