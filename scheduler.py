from celery import Celery
import mongoengine

# for tasks
celery = Celery('daily-ebook',
            broker="redis://redis:6379/0",
            backend="redis://redis:6379/0")
celery.conf.task_routes = ([
    ('ebook_generator.*', {'queue': 'eg'}),
    ('data_provider.*', {'queue': 'dp'})
],)

#mongoengine.connect('celery_beat_daily_epub') useless for now
"""confs = {
    "CELERY_MONGODB_SCHEDULER_DB": "celery_beat_daily_epub",
    "CELERY_MONGODB_SCHEDULER_COLLECTION" : "schedules", # we can't really change this, there is no current_app according to
    "CELERY_MONGODB_SCHEDULER_URL" : "mongodb://mongo:27017"
}
celery.conf.update(confs)"""