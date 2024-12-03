# WebSite/models.py
from django.db import models
from parler.models import TranslatableModel, TranslatedFields

# HomePageContent model to store homepage information
# WebSite/models.py
from django.db import models
from parler.models import TranslatableModel, TranslatedFields

# HomePageContent model to store homepage information
class HomePageContent(TranslatableModel):
    translations = TranslatedFields(
        headline=models.CharField(max_length=200),  # Title of the homepage section
        subheadline=models.TextField(),  # Subtitle or detailed description
    )
    promotional_image = models.ImageField(upload_to='homepage/')  # Image for promotional purposes

    def __str__(self):
        return self.safe_translation_getter('headline', any_language=True)


# Toolbar model to manage toolbar links and labels
class Toolbar(TranslatableModel):
    APP_LINKS = {
        'home': '/',
        'news': '/news/',
        'products': '/products/',
        'media': '/media/library/',
        'account': '/account/login/',
    }
    translations = TranslatedFields(
        label=models.CharField(max_length=100),  # Label for the toolbar link
    )
    link = models.CharField(max_length=100, choices=[(key, key.capitalize()) for key in Toolbar.APP_LINKS.keys()])  # URL link for the toolbar item
    order = models.PositiveIntegerField(default=0)  # Order of the toolbar item

    class Meta:
        ordering = ['order']  # Ensure toolbar items are displayed in the specified order

    def __str__(self):
        return self.safe_translation_getter('label', any_language=True)

    # Method to render toolbar links in HTML
    def to_html(self):
        link_url = self.APP_LINKS.get(self.link, self.link)
        return f'<li><a href="{link_url}">{self.safe_translation_getter("label", any_language=True)}</a></li>'



