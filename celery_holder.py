from celery import Celery
from config import Config

celery = Celery(
    __name__,
    backend=Config.CELERY_RESULT_BACKEND,
    broker=Config.CELERY_RESULT_BROKER,
    include=[
        # 'app.jobs.register.register_tasks',
        # 'app.jobs.reset_password.reset_password_tasks',
        # 'app.jobs.sms.sms_tasks',
        'app.jobs'
    ],
    # broker_transport_options=Config.BROKER_TRANSPORT_OPTIONS,
)