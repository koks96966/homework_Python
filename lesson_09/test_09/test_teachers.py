from sqlalchemy import text


def test_delete_teacher(session):
    # Уникальный ID для теста, чтобы не задеть реальные данные
    test_teacher_id = 99961
    test_email = f"test-teacher-{test_teacher_id}@example.com"
    test_group_id = 101

    # 1. Создаём тестовую строку
    session.execute(
        text("""
            INSERT INTO teacher (teacher_id, email, group_id)
            VALUES (:tid, :em, :gid)
        """),
        {"tid": test_teacher_id, "em": test_email, "gid": test_group_id}
    )
    session.commit()

    # Проверяем, что строка действительно появилась
    check_insert = session.execute(
        text("SELECT email FROM teacher WHERE teacher_id = :tid"),
        {"tid": test_teacher_id}
    )
    inserted_email = check_insert.scalar()
    assert inserted_email == test_email, (
        f"Строка не была создана: ожидали email '{test_email}', "
        f"получили '{inserted_email}'"
    )

    # 2. Удаляем строку по teacher_id
    session.execute(
        text("DELETE FROM teacher WHERE teacher_id = :tid"),
        {"tid": test_teacher_id}
    )
    session.commit()

    # 3. Проверяем, что строки больше нет (COUNT = 0)
    check_delete = session.execute(
        text(
            "SELECT COUNT(*) FROM teacher WHERE teacher_id = :tid"
        ),
        {"tid": test_teacher_id}
    )
    count_after_delete = check_delete.scalar()
    assert count_after_delete == 0, (
        f"Строка с teacher_id={test_teacher_id} не была удалена "
        f"(count={count_after_delete})"
    )
