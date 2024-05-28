import datetime
from typing import List

from Core import app, HTTPException
from Core.Service_SQL.database_manager import DatabaseManager
from Core.Service_SQL.sql import SQL


@app.get("/document_invoice")
async def document_invoice():
    """Получить счет"""
    db = SQL()
    db.connect()
    try:
        document_invoice = DatabaseManager.get_document_invoice(db=db)
        return {document_invoice}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        db.close()


@app.get("/get_shipment_notification_document")
async def shipment_notification_document():
    """Получить извещения об отгрузке"""
    db = SQL()
    db.connect()
    try:
        shipment_notification_document = DatabaseManager.get_shipment_notification_document(db=db)
        return {shipment_notification_document}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        db.close()


@app.get("/get_document_application_for_production")
async def document_application_for_production():
    """Получить заявки на производтсво"""
    db = SQL()
    db.connect()
    try:
        document_application_for_production = DatabaseManager.get_document_application_for_production(db=db)
        return {document_application_for_production}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        db.close()


@app.get("/get_reference_book_approval_log")
async def reference_book_approval_log():
    """Получить служебные записки"""
    db = SQL()
    db.connect()
    try:
        reference_book_approval_log = DatabaseManager.get_reference_book_approval_log(db=db)
        return {reference_book_approval_log}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        db.close()


@app.get("/get_find_no_document_invoice")
async def find_no_document_invoice():
    """Получить несогласованные документы счета"""
    db = SQL()
    db.connect()
    try:
        find_no_document_invoice = DatabaseManager.get_find_no_document_invoice(db=db)
        return {find_no_document_invoice}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        db.close()

@app.get("/get_find_yes_document_invoice")
async def find_yes_document_invoice():
    """Получить согласованные документы счета"""
    db = SQL()
    db.connect()
    try:
        find_yes_document_invoice = DatabaseManager.get_find_yes_document_invoice(db=db)
        return {find_yes_document_invoice}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        db.close()


@app.get("/get_find_no_Shipment_Notification_Document")
async def find_no_Shipment_Notification_Document():
    """Получить несогласованные документы об отправке"""
    db = SQL()
    db.connect()
    try:
        find_no_Shipment_Notification_Document = DatabaseManager.get_find_no_Shipment_Notification_Document(db=db)
        return {find_no_Shipment_Notification_Document}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        db.close()


@app.get("/get_find_yes_Shipment_Notification_Document")
async def find_yes_Shipment_Notification_Document():
    """олучить согласованные документы об отправке"""
    db = SQL()
    db.connect()
    try:
        find_yes_Shipment_Notification_Document = DatabaseManager.get_find_yes_Shipment_Notification_Document(db=db)
        return {find_yes_Shipment_Notification_Document}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        db.close()


@app.get("/get_find_no_Document_application_for_production")
async def find_no_Document_application_for_production():
    """Получить несогласованные заявки на призводство"""
    db = SQL()
    db.connect()
    try:
        find_no_Document_application_for_production = DatabaseManager.get_find_no_Document_application_for_production(db=db)
        return {find_no_Document_application_for_production}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        db.close()


@app.get("/get_find_yes_Document_application_for_production")
async def find_yes_Document_application_for_production():
    """Получить согласованные заявки на призводство"""
    db = SQL()
    db.connect()
    try:
        find_yes_Document_application_for_production = DatabaseManager.get_find_yes_Document_application_for_production(db=db)
        return {find_yes_Document_application_for_production}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        db.close()


@app.get("/get_find_no_Reference_Book_Approval_Log")
async def find_no_Reference_Book_Approval_Log():
    """Получить несогласованные служебные записки"""
    db = SQL()
    db.connect()
    try:
        find_no_Reference_Book_Approval_Log = DatabaseManager.get_find_no_Reference_Book_Approval_Log(db=db)
        return {find_no_Reference_Book_Approval_Log}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        db.close()


@app.get("/get_find_yes_Reference_Book_Approval_Log")
async def find_yes_Reference_Book_Approval_Log():
    """Получить согласованные служебные записки"""
    db = SQL()
    db.connect()
    try:
        find_yes_Reference_Book_Approval_Log = DatabaseManager.get_find_yes_Reference_Book_Approval_Log(db=db)
        return {find_yes_Reference_Book_Approval_Log}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        db.close()

