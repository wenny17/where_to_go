from django.contrib import admin
from django.utils.html import format_html

from adminsortable2.admin import SortableInlineAdminMixin

from .models import Place, PlaceImage
# Register your models here.


class PlaceImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = PlaceImage
    readonly_fields = ['preview']
    extra = 0

    def preview(self, image):
        return format_html('<img src="{}" height="200"></img>', image.image.url)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [PlaceImageInline]
