from django.contrib import admin
from django.conf import settings
from shortener.models import ShortLink

def short_link(obj):
    return u"<a href='%s'>%s</a>" % (obj.short_url, obj.short_url)

short_link.short_description = 'Short Link'
short_link.allow_tags = True

if getattr(settings, 'USE_MODELTRANSLATION', False):
    from modeltranslation.admin import TranslationAdmin
    
    class ShortLinkAdmin(TranslationAdmin):
        fields = ('title', 'url', short_link, 'views_count', 'submit_time')
        readonly_fields = (short_link, 'views_count', 'submit_time')
        list_display = ('title', 'url', short_link, 'views_count', 'submit_time')
else:
    class ShortLinkAdmin(admin.ModelAdmin):
        fields = ('title', 'url', short_link, 'views_count', 'submit_time')
        readonly_fields = (short_link, 'views_count', 'submit_time')
        list_display = ('title', 'url', short_link, 'views_count', 'submit_time')

admin.site.register(ShortLink, ShortLinkAdmin)
