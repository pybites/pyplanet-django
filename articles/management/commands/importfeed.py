import feedparser

from django.core.management.base import BaseCommand
from articles.models import Article

FEED = 'http://planetpython.org/rss20.xml'


class Command(BaseCommand):
    help = 'Imports new Planet Python feed entries into articles table'

    def handle(self, *args, **options):
        count = 0

        for entry in feedparser.parse(FEED)['entries']:
            title = entry['title']
            url = entry['link']
            summary = entry.get('summary', 'No summary available')

            obj, created = Article.objects.get_or_create(
                title=title,
                url=url,
                summary=summary,
            )

            if created:
                confirm_msg = 'created'
                count += 1
            else:
                confirm_msg = 'already in DB'

            self.stdout.write('Article id {} {}'.format(obj.id, confirm_msg))

        self.stdout.write(
            self.style.SUCCESS(
                '{} articles added'.format(count)
            )
        )
