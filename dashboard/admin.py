from django.contrib import admin

from dashboard.models import Book, Author
from quote.models import Quote , LineItem , Company, Company_Contact, Item

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Quote)
admin.site.register(Company)
admin.site.register(Company_Contact)
admin.site.register(LineItem)
admin.site.register(Item)

admin.site.site_title = 'Secureway'
admin.site.site_header = 'Secureway Admin'