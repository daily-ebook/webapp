from celery import Celery
import mongoengine

# for tasks
celery = Celery('tasks',
            broker="redis://localhost:6379/0",
            backend="redis://localhost:6379/0")

#mongoengine.connect('celery_beat_daily_epub') useless for now
confs = {
    "CELERY_MONGODB_SCHEDULER_DB": "celery_beat_daily_epub",
    "CELERY_MONGODB_SCHEDULER_COLLECTION" : "schedules", # we can't really change this, there is no current_app according to
    "CELERY_MONGODB_SCHEDULER_URL" : "mongodb://localhost:27017"
}
celery.conf.update(confs)