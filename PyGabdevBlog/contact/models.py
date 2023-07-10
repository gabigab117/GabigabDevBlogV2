from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel
from wagtail.contrib.forms.models import AbstractFormField, AbstractEmailForm
from wagtail.fields import RichTextField

from wagtailcaptcha.models import WagtailCaptchaEmailForm


class FormField(AbstractFormField):
    page = ParentalKey("ContactPage", on_delete=models.CASCADE, related_name="form_fields")


class ContactPage(WagtailCaptchaEmailForm):
    # Hérite de AbstractEmailForm
    template = "contact/contact_page.html"
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro'),
        InlinePanel('form_fields', label="Champs du formulaire"),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col-6"),
                FieldPanel('to_address', classname="col-6"),
            ]),
            FieldPanel('subject')
        ], heading="Configurations des adresses"),
    ]
