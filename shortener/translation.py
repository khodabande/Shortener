from modeltranslation.translator import register, TranslationOptions
from shortener.models import ShortLink


@register(ShortLink)
class TranslatedShortLink(TranslationOptions):
    fields = ('title',)
