from celery.task import periodic_task
from datetime import timedelta
from api import dp
from .models import Item

def update_database(items):
    for item in items:
        new_item, created = Item.objects.update_or_create(item_number=item['item_number'], defaults=item)


@periodic_task(ignore_result=True, run_every=timedelta(minutes=10))
def task_run_update():
    dp.refresh_data()
    update_database(dp.collected_items)
    print(f"Data updated: {dp.last_update}")