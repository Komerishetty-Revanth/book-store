from django.contrib import admin



class Notebook(admin.ModelAdmin):
    list_display = ('brand', 'pages', 'size', 'type', 'price', 'author')
    search_fields = ('brand', 'author')


