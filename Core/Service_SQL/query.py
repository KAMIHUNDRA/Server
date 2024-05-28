class Query:

    @staticmethod
    def get_Document_Invoice() -> str:
        """Получить счет"""
        return "SELECT * FROM Document_Invoice"

    @staticmethod
    def get_Shipment_Notification_Document() -> str:
        """Получить извещения об отгрузке"""
        return "SELECT * FROM Shipment_Notification_Document"

    @staticmethod
    def get_Document_application_for_production() -> str:
        """Получить заявки на производтсво"""
        return "SELECT * FROM Document_application_for_production"

    @staticmethod
    def get_Reference_Book_Approval_Log() -> str:
        """Получить служебные записки"""
        return "SELECT * FROM Reference_Book_Approval_Log"



    @staticmethod
    def find_no_Document_Invoice() -> str:
        """Получить несогласованные документы счета"""
        return "SELECT * FROM Reference_Book_Approval_Log WHERE Agreed_upon = 'нет'"

    @staticmethod
    def find_no_Shipment_Notification_Document() -> str:
        """Получить несогласованные документы об отправке"""
        return "SELECT * FROM Shipment_Notification_Document WHERE Agreed_upon = 'нет'"

    @staticmethod
    def find_no_Document_application_for_production() -> str:
        """Получить несогласованные заявки на призводство"""
        return "SELECT * FROM Document_application_for_production WHERE Agreed_upon = 'нет'"

    @staticmethod
    def find_no_Reference_Book_Approval_Log() -> str:
        """Получить несогласованные служебные записки"""
        return "SELECT * FROM Reference_Book_Approval_Log WHERE Agreed_upon = 'нет'"



    @staticmethod
    def find_yes_Document_Invoice() -> str:
        """Получить согласованные документы счета"""
        return "SELECT * FROM Document_Invoice WHERE Agreed_upon = 'да'"

    @staticmethod
    def find_yes_Shipment_Notification_Document() -> str:
        """Получить согласованные документы об отправке"""
        return "SELECT * FROM Shipment_Notification_Document WHERE Agreed_upon = 'да'"

    @staticmethod
    def find_yes_Document_application_for_production() -> str:
        """Получить согласованные заявки на призводство"""
        return "SELECT * FROM Document_application_for_production WHERE Agreed_upon = 'да'"

    @staticmethod
    def find_yes_Reference_Book_Approval_Log() -> str:
        """Получить согласованные служебные записки"""
        return "SELECT * FROM Reference_Book_Approval_Log WHERE Agreed_upon = 'да'"
