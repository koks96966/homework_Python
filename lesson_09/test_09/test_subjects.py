from sqlalchemy import text


def test_update_existing_subject_id_9(session):
    target_id = 9
    new_title = "History of Russia"

    # 1. Получаем исходное название, чтобы потом вернуть
    check_original = session.execute(
        text("SELECT subject_title FROM subject WHERE subject_id = :id"),
        {"id": target_id}
    )
    original_title = check_original.scalar()

    assert original_title is not None, (
        f"Строка с subject_id={target_id} не найдена — "
        f"тест не может выполниться"
    )

    # 2. Обновляем на новое название
    session.execute(
        text("UPDATE subject SET subject_title = :new WHERE subject_id = :id"),
        {"new": new_title, "id": target_id}
    )
    session.commit()

    # 3. Проверяем, что обновилось
    check_after = session.execute(
        text("SELECT subject_title FROM subject WHERE subject_id = :id"),
        {"id": target_id}
    )
    current_title = check_after.scalar()
    assert current_title == new_title, (
        f"Ожидали '{new_title}', но получили '{current_title}'"
    )

    # 4. Возвращаем исходное название
    session.execute(
        text(
            "UPDATE subject SET subject_title = :orig WHERE subject_id = :id"
        ),
        {"orig": original_title, "id": target_id}
    )
    session.commit()

    # 5. Проверяем, что вернули как было
    check_restored = session.execute(
        text("SELECT subject_title FROM subject WHERE subject_id = :id"),
        {"id": target_id}
    )
    restored_title = check_restored.scalar()
    assert restored_title == original_title, (
        f"Не удалось вернуть исходное название: "
        f"ожидали '{original_title}', получили '{restored_title}'"
    )
