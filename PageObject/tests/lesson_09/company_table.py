from sqlalchemy import create_engine, text


class Database:
    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    # ===== SUBJECT =====
    def get_subjects(self):
        with self.db.connect() as conn:
            result = conn.execute(text("SELECT * FROM subject WHERE deleted_at IS NULL"))
            return result.mappings().all()

    def create_subject(self, subject_id, name):
        with self.db.connect() as conn:
            conn.execute(
                text("INSERT INTO subject(subject_id, subject_title) VALUES (:id, :name)"),
                {"id": subject_id, "name": name}
            )
            conn.commit()

    def update_subject(self, subject_id, new_name):
        with self.db.connect() as conn:
            conn.execute(
                text("UPDATE subject SET subject_title = :name WHERE subject_id = :id"),
                {"id": subject_id, "name": new_name}
            )
            conn.commit()

    def soft_delete_subject(self, subject_id):
        with self.db.connect() as conn:
            conn.execute(
                text("UPDATE subject SET deleted_at = NOW() WHERE subject_id = :id"),
                {"id": subject_id}
            )
            conn.commit()

    def delete_subject(self, subject_id):
        with self.db.connect() as conn:
            conn.execute(
                text("DELETE FROM subject WHERE subject_id = :id"),
                {"id": subject_id}
            )
            conn.commit()

    def get_max_subject_id(self):
        with self.db.connect() as conn:
            result = conn.execute(text("SELECT MAX(subject_id) FROM subject WHERE deleted_at IS NULL"))
            return result.scalar()

    def get_max_user_id(self):
        with self.db.connect() as conn:
            result = conn.execute(text("SELECT MAX(user_id) FROM users WHERE deleted_at IS NULL"))
            return result.scalar()

    def create_user(self, user_id, email, subject_id):
        with self.db.connect() as conn:
            conn.execute(
                text("INSERT INTO users(user_id, user_email, subject_id) VALUES (:id, :email, :subject_id)"),
                {"id": user_id, "email": email, "subject_id": subject_id}
            )
            conn.commit()

    def delete_user(self, user_id):
        with self.db.connect() as conn:
            conn.execute(
                text("DELETE FROM users WHERE user_id = :id"),
                {"id": user_id}
            )
            conn.commit()

    def get_users(self):
        with self.db.connect() as conn:
            result = conn.execute(text("SELECT * FROM users WHERE deleted_at IS NULL"))
            return result.mappings().all()
