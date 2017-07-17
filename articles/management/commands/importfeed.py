from time import mktime
from datetime import datetime, timedelta

import feedparser

from django.core.management.base import BaseCommand
from django.utils import timezone

from articles.models import Article

# add other feeds and/or not working ones
FEEDS = [
    'http://planetpython.org/rss20.xml',
    'https://pybit.es/feeds/all.rss.xml',
]
GO_BACK = datetime.now() - timedelta(days=1)


def _get_entries():
    for feed in FEEDS:
        yield from feedparser.parse(feed)['entries']


class Command(BaseCommand):
    help = 'Imports new Planet Python feed entries into articles table'

    def handle(self, *args, **options):
        count = 0

        for entry in sorted(_get_entries(),
                            key=lambda e: e['published_parsed'],
                            reverse=True):
            title = entry['title']
            url = entry['link']
            summary = entry.get('summary', 'No summary available')
            published = entry['published_parsed']
            dt = datetime.fromtimestamp(mktime(published))
            if dt < GO_BACK:
                continue
            dt = timezone.make_aware(dt, timezone.get_current_timezone())

            obj, created = Article.objects.get_or_create(
                title=title,
                url=url,
                summary=summary,
                published=dt,
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
