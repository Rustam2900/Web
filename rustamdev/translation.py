from modeltranslation.translator import TranslationOptions, register
from rustamdev import models


@register(models.Portfolio)
class CustomUserTranslation(TranslationOptions):
    fields = ('title', 'description')


@register(models.ClientFeedback)
class CustomUserTranslation(TranslationOptions):
    fields = ('name', 'company_name', 'comment')


@register(models.Service)
class ProductTranslation(TranslationOptions):
    fields = ('title', 'description')


@register(models.Team)
class ProductTranslation(TranslationOptions):
    fields = ('full_name', 'bio', 'position')
