from django.contrib import admin
from .models import Author, Book, Genre, Language, Status, BookInstance


#admin.site.register(Author)
#admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)
#admin.site.register(BookInstance)
class BookInstanceInline(admin.TabularInline):
    model = BookInstance


class AuthorAdmin(admin.ModelAdmin):
    list_display= ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
admin.site.register(Author, AuthorAdmin)

# регистрируем классы администратора для книг
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author')
    list_filter = ('genre', 'author')
    inlines = [BookInstanceInline]


# регистрируем классы администратора для экземпляра книг
@admin.register(BookInstance)
class BookInstance(admin.ModelAdmin):
    list_filter = ('book', 'status')


class BookInstanceInline(admin.TabularInline):
    model = BookInstance

