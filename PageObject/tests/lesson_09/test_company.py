def test_get_subjects(db):
    subjects = db.get_subjects()
    for subject in subjects:
        assert subject["deleted_at"] is None
    print(f"Найдено активных предметов: {len(subjects)}")


def test_create_subject(db):
    max_id = db.get_max_subject_id() or 0
    new_id = max_id + 1

    db.create_subject(new_id, "Autotest Subject")

    subjects = db.get_subjects()
    found = False
    for subject in subjects:
        if subject["subject_id"] == new_id:
            found = True
            assert subject["subject_title"] == "Autotest Subject"
            break

    db.delete_subject(new_id)
    assert found


def test_update_subject(db):
    max_id = db.get_max_subject_id() or 0
    new_id = max_id + 1

    db.create_subject(new_id, "Old Name")
    db.update_subject(new_id, "New Name")

    subjects = db.get_subjects()
    found = False
    for subject in subjects:
        if subject["subject_id"] == new_id:
            found = True
            assert subject["subject_title"] == "New Name"
            break

    db.delete_subject(new_id)
    assert found


def test_soft_delete_subject(db):
    max_id = db.get_max_subject_id() or 0
    new_id = max_id + 1

    db.create_subject(new_id, "To Delete")
    db.soft_delete_subject(new_id)

    subjects = db.get_subjects()
    found = False
    for subject in subjects:
        if subject["subject_id"] == new_id:
            found = True
            break

    db.delete_subject(new_id)
    assert not found, "Предмет найден среди активных после мягкого удаления"


def test_create_user(db):
    max_id = db.get_max_user_id() or 0
    new_id = max_id + 1

    db.create_user(new_id, "test@example.com", 1)

    users = db.get_users()
    found = False
    for user in users:
        if user["user_id"] == new_id:
            found = True
            assert user["user_email"] == "test@example.com"
            break

    db.delete_user(new_id)
    assert found
