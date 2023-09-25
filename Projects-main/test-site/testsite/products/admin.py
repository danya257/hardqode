from django.contrib import admin

from .models import Product, Lesson, Owner, Access

@admin.register(Access)
class AccesAdmin(admin.ModelAdmin):
    list_display = ('user', 'product')

class ProductsInline(admin.TabularInline):
    model = Product
    fields = ('id', 'title', 'is_published')
    readonly_fields = ('id', 'created', 'updated')
    show_change_link = True
    extra = 1
    max_num = 0


class LessonInline(admin.TabularInline):
    model = Lesson.products.through
    autocomplete_fields = ('product', 'lesson')


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_published')
    list_display_links = ('id', 'name',)
    list_filter = ('is_published', 'created', 'updated')
    list_editable = ('is_published',)
    search_fields = ('id', 'name', )
    readonly_fields = ('id', 'created', 'updated')
    fieldsets = [
        (None, {
            "fields": ['id', 'name', 'is_published', 'created', 'updated'],
        },),
    ]
    actions_selection_counter = True
    show_full_result_count = True


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published')
    list_display_links = ('id', 'title')
    list_filter = ('is_published', 'created', 'updated')
    list_editable = ('is_published',)
    search_fields = ('id', 'title')
    readonly_fields = ('id', 'created', 'updated')
    fieldsets = [
        (None, {
            "fields": ['id', 'viewer', 'owner', 'title',
                       'is_published'],
        },),
        ('Даты', {
            'classes': ['collapse'],
            'fields': ['created', 'updated'],
        },),
    ]
    actions_selection_counter = True
    show_full_result_count = True


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published')
    list_display_links = ('id', 'title',)
    list_filter = ('is_published', 'created', 'updated',
                   )
    list_editable = ('is_published',)
    search_fields = ('id', 'title',)
    readonly_fields = ('id', 'created', 'updated', 'duration')
    fieldsets = [
        (None, {
            "fields": ['id', 'title',
                       'is_published', 'products'],
        },),
        ('Видео', {
            "fields": ['video', 'duration'],
        },),
        ('Даты', {
            'classes': ['collapse'],
            'fields': ['created', 'updated'],
        },),
    ]
    actions_selection_counter = True
    show_full_result_count = True






