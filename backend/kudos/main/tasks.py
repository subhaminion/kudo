from __future__ import absolute_import
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from django.utils import timezone
from .dbapi import (
	reset_kudos_count_for_all_users
)

from django.conf import settings
logger = get_task_logger(__name__)



@periodic_task(
    run_every=(crontab(minute='*/1')), # For running every minute
    # run_every=(crontab(minute=0, hour=0, day_of_week=setting.DAY_OF_THE_WEEK)) # For running every week
    name="reset_kudo_count",
    ignore_result=True
)
def reset_kudo_count():
	logger.info(" Brace yourself! Mega Update is coming!!!")
	reset_kudos_count_for_all_users()
	return "Updated all user kudo count at {}".format(timezone.now())
