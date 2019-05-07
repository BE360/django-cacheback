from celery import shared_task
from django.conf import settings


@shared_task(queue=getattr(settings, 'CACHEBACK_CELERY_TASK_QUEUE', 'cacheback'))
def refresh_cache(klass_str, obj_args, obj_kwargs, call_args, call_kwargs):
    from .base import Job
    Job.perform_async_refresh(klass_str, obj_args, obj_kwargs, call_args, call_kwargs)
