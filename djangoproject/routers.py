"""
router file
"""


class HistoryRouter:
    """
    history router class
    """

    history_app = {"history_app"}

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.history_app:  # noqa: SLF001
            return "history_db"
        return "default"

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.history_app:  # noqa: SLF001
            return "history_db"
        return "default"

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.history_app  # noqa: SLF001
            or obj2._meta.app_label in self.history_app  # noqa: SLF001
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'auth_db' database.
        """

        if (
            db == "history_db"
            and app_label in self.history_app
            or db == "default"
            and app_label not in self.history_app
        ):
            return True
        return False
