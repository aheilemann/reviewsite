from .models import Review
import django_tables2 as tables

class ReviewTable(tables.Table):

    class Meta:
        model= Review
        template_name = "django_tables2/bootstrap4.html"
        fields = [
            'title',
            'category',
            'modified',
        ]
        order_by = '-modified'
    
    title = tables.Column(linkify=True)
    modified = tables.DateColumn()