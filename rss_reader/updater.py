import feedparser

from .models import Feed, Article


def update_feeds():
    feeds = Feed
    for feed in feeds.feed_title:
        try:
            feed_items = feedparser.parse(feed.feed_url)
            for entry in feed_items['entries']:

                date_published = entry.get('published')

                article_guid = entry.get('id')

                items_count = Article.feed.filter(
                    article_feed=feed
                ).count()

                if items_count == 0:

                    article_description = entry.get('description')
                    if article_description is not None:
                        article_description = article_description[0]['value']

                else:
                    description = None

                i = Article(feed=feed,
                            article_title=entry.get('title'),
                            article_link=entry.get('link'),
                            article_description=entry.get('description'),
                            article_published=entry.get('published'),
                            article_guid=entry.get('id')
                            )
                i.save()
        except Exception as e:
            print(e)



