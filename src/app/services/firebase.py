def init(service_account_path: str):
    """
    Initialize Firebase service with the given service account key and database URL.

    :param service_account_key: Path to the service account key file.
    """

    import firebase_admin
    from firebase_admin import credentials

    # Initialize Firebase service
    cred = credentials.Certificate(service_account_path)
    firebase_admin.initialize_app(cred)
    print('Khởi tạo firebase thành công.')

def on_datachange(path: str, callback):
    """
    Listen to data changes at the given path.

    :param path: Path to the data.
    :param callback: Callback function to be called when data changes.
    """

    from firebase_admin import db

    # Get a database reference
    ref = db.reference(path)

    # Listen to data changes
    ref.listen(callback)
