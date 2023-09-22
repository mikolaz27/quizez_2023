import random
import time

from celery import shared_task
from django.contrib.auth import get_user_model


@shared_task
def mine_bitcoin():
    time.sleep(60)


@shared_task
def normalize_email_task(filter):
    users = get_user_model().objects.filter(**filter)
    if users:
        for user in users:
            print(f'working with user: {user.email}')
            user.save()
    else:
        print('empty data')
    return f'Checked {len(users)} users'
