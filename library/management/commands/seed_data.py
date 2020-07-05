from django.core.management.base import BaseCommand, CommandError
from library.models import Book, Library
from utility.bulk_create_manager import BulkCreateManager
from django.utils import timezone
from faker import Faker
import random
import time


class Command(BaseCommand):
    help = 'Populated seed data'
    NO_OF_SEED_LIBRARY = 5
    MIN_NO_OF_BOOKS_PER_LIBRARY = 50000
    MAX_NO_OF_BOOKS_PER_LIBRARY = 100000

    def add_arguments(self, parser):
        parser.add_argument("-c", "--chunk", type=int, default=100)

    def handle(self, *args, **options):
        chunk_size = options.get("chunk")
        bulk_mngr = BulkCreateManager(chunk_size)
        fake = Faker()
        for counter in range(self.NO_OF_SEED_LIBRARY):
            library = Library(
                name = fake.name() + " Library",
                updated_at = timezone.now(),
                archived=False
            )
            bulk_mngr.add(library)
        bulk_mngr.done()
        library_qs = Library.objects.all()
        print("-- Done creating libraries --")
        for library in library_qs:
            no_of_books_for_library = random.randint(
                self.MIN_NO_OF_BOOKS_PER_LIBRARY,
                self.MAX_NO_OF_BOOKS_PER_LIBRARY
            )
            print("-- Adding %s books to %s(%s) --" % (
                no_of_books_for_library, library.name, library.id
            ))
            for counter in range(no_of_books_for_library):
                book = Book(
                    title=fake.sentence(),
                    publisher=fake.company(),
                    library=library,
                    updated_at=timezone.now(),
                    archived=False
                )
                bulk_mngr.add(book)
            bulk_mngr.done()

