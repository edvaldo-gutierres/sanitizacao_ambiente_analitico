from service.database import DatabaseService
from sqlalchemy import text


def test_database_connection():
    db_service = DatabaseService()
    session = db_service.get_session()
    session.close()
    assert True


def test_table_exists():
    db_service = DatabaseService()
    session = db_service.get_session()
    cursor = session.execute(
        text(
            "SELECT COUNT(*) FROM dw_hml.information_schema.tables WHERE table_name = 'tab_analytical_tables_sanitization'"
        )
    )
    result = cursor.fetchone()
    session.close()
    assert result[0] == 1


def test_qty_days_greater_than_60():
    db_service = DatabaseService()
    session = db_service.get_session()
    cursor = session.execute(
        text(
            """
            SELECT COUNT(*)
            FROM dw_hml.data_engineer.tab_analytical_tables_sanitization
            WHERE qty_days > 60
        """
        )
    )
    result = cursor.fetchone()
    session.close()
    assert result[0] > 0
