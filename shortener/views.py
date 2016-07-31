from django.db.models import F
from django.shortcuts import render, get_object_or_404, redirect
from shortener.models import ShortLink


def shortener_redirect_view(*args, **kwargs):
    slug = kwargs['slug']
    short_link = get_object_or_404(ShortLink, slug=slug)
    short_link.views_count = F('views_count') + 1
    short_link.save()
    return redirect(short_link.url)
