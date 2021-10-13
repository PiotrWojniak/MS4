from django.db import models


SUBJECT_MENU = (
    ('General query', 'GENERAL QUERY'),
    ('Where is my order', 'WHERE IS MY ORDER?'),
    ('Update my order', 'UPDATE MY ORDER'),
    ('Return or exchange of my order', 'RETURN OR EXCHANGE OF MY ORDER'),
    ('Complaint', 'COMPLAINT'),
)


class Contact(models.Model):
    """
    A Contact model for admin to view users queries
    """
    class Meta:
        verbose_name_plural = 'Queries'

    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=150, null=False, blank=False)
    subject = models.CharField(max_length=100, choices=SUBJECT_MENU,
                               default='general_query',
                               null=False, blank=False)
    message = models.TextField(blank=False, null=False)
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
