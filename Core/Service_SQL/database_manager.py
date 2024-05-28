from Core.Service_SQL.sql import SQL
from Core.Service_SQL.select_sql import SelectSQL
from Core.Service_SQL.query import Query

from datetime import datetime

class DatabaseManager:

    @staticmethod
    def get_document_invoice(db: SQL):
        """Получить счет"""
        select = SelectSQL()
        select.set_db(db.get_db())
        select.set_query(Query.get_Document_Invoice())
        select.execute()
        return select.get_result()

    @staticmethod
    def get_shipment_notification_document(db: SQL):
        """Получить извещения об отгрузке"""
        select = SelectSQL()
        select.set_db(db.get_db())
        select.set_query(Query.get_Shipment_Notification_Document())
        select.execute()
        return select.get_result()

    @staticmethod
    def get_document_application_for_production(db: SQL):
        """Получить заявки на производтсво"""
        select = SelectSQL()
        select.set_db(db.get_db())
        select.set_query(Query.get_Document_application_for_production())
        select.execute()
        return select.get_result()

    @staticmethod
    def get_reference_book_approval_log(db: SQL):
        """Получить служебные записки"""
        select = SelectSQL()
        select.set_db(db.get_db())
        select.set_query(Query.get_Reference_Book_Approval_Log())
        select.execute()
        return select.get_result()


    @staticmethod
    def get_find_no_document_invoice(db: SQL):
        """Получить несогласованные документы счета"""
        select = SelectSQL()
        select.set_db(db.get_db())
        select.set_query(Query.find_no_Document_Invoice())
        select.execute()
        return select.get_result()

    @staticmethod
    def get_find_no_Shipment_Notification_Document(db: SQL):
        """Получить несогласованные документы об отправке"""
        select = SelectSQL()
        select.set_db(db.get_db())
        select.set_query(Query.find_no_Shipment_Notification_Document())
        select.execute()
        return select.get_result()

    @staticmethod
    def get_find_no_Document_application_for_production(db: SQL):
        """Получить несогласованные заявки на призводство"""
        select = SelectSQL()
        select.set_db(db.get_db())
        select.set_query(Query.find_no_Document_application_for_production())
        select.execute()
        return select.get_result()

    @staticmethod
    def get_find_no_Reference_Book_Approval_Log(db: SQL):
        """Получить несогласованные заявки на призводство"""
        select = SelectSQL()
        select.set_db(db.get_db())
        select.set_query(Query.find_no_Reference_Book_Approval_Log())
        select.execute()
        return select.get_result()


    @staticmethod
    def get_find_yes_document_invoice(db: SQL):
        """Получить согласованные документы счета"""
        select = SelectSQL()
        select.set_db(db.get_db())
        select.set_query(Query.find_yes_Document_Invoice())
        select.execute()
        return select.get_result()

    @staticmethod
    def get_find_yes_Shipment_Notification_Document(db: SQL):
        """Получить согласованные документы об отправке"""
        select = SelectSQL()
        select.set_db(db.get_db())
        select.set_query(Query.find_yes_Shipment_Notification_Document())
        select.execute()
        return select.get_result()

    @staticmethod
    def get_find_yes_Document_application_for_production(db: SQL):
        """Получить согласованные заявки на призводство"""
        select = SelectSQL()
        select.set_db(db.get_db())
        select.set_query(Query.find_yes_Document_application_for_production())
        select.execute()
        return select.get_result()

    @staticmethod
    def get_find_yes_Reference_Book_Approval_Log(db: SQL):
        """Получить согласованные заявки на призводство"""
        select = SelectSQL()
        select.set_db(db.get_db())
        select.set_query(Query.find_yes_Reference_Book_Approval_Log())
        select.execute()
        return select.get_result()


