from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.conf import settings

class Command(BaseCommand):
    help = "Creates new user with admin role"

    def handle(self, *args, **options):
        for user in settings.ADMINS:
            username = user[0].replace(" ","")
            email = user[1]
            password = user[2]
            self.stdout.write("Adding new admin user '%s'(%s)" % (username, email))

            try:
                User.objects.create_superuser(username, email, password)
            except IntegrityError:
                raise CommandError("Can't create admin user with name '%s'" % username)
            self.stdout.write(self.style.SUCCESS("Admin user '%s' is registered" % username))
        
