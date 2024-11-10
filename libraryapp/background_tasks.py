from celery import shared_task
from datetime import datetime, timedelta
from .models import Book


@shared_task
def archived_old_books():
    old_books_time = datetime.now().date() - timedelta(days=365 * 10)
    old_books = Book.objects.filter(published_date__lte=old_books_time, is_archived=False)
    old_books.update(is_archived=True)
