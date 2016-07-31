import random
import string

from django.core.urlresolvers import reverse
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

SLUG_CHARSET = getattr(settings, 'SHORTENER_SLUG_CHARSET',
                       string.ascii_lowercase + string.uppercase + string.digits)
SLUG_LENGTH = getattr(settings, 'SHORTENER_SLUG_LENGTH', 8)


def generate_random_slug():
    return ''.join([random.choice(SLUG_CHARSET) for _ in range(SLUG_LENGTH)])


class ShortLink(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=200)
    url = models.URLField(unique=True)
    slug = models.CharField(verbose_name=_('Slug'), max_length=SLUG_LENGTH, unique=True,
                            blank=True)
    views_count = models.PositiveIntegerField(verbose_name=_('Views Count'), default=0,
                                              editable=False)
    submit_time = models.DateTimeField(verbose_name=_('Submit Time'), auto_now_add=True)
    last_change = models.DateTimeField(verbose_name=_('Last Change'), auto_now=True)

    @property
    def short_url(self):
        return reverse('shortener_redirect_view', args=(self.slug,))

    def save(self, *args, **kwargs):
        if not self.id:
            slug = generate_random_slug()
            while ShortLink.objects.filter(slug=slug).exists():
                slug = generate_random_slug()
            self.slug = slug
        super(ShortLink, self).save(*args, **kwargs)

    def __unicode__(self):
        return '{%s -> %s}' % (self.short_url, self.url)

    class Meta:
        verbose_name = _("Short Link")
        verbose_name_plural = _("Short Links")
        ordering = ('submit_time',)
        get_latest_by = 'submit_time'
