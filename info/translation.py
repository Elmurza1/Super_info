from modeltranslation.translator import register, TranslationOptions

from info.models import Publication, PublicationComment, Category

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)



@register(Publication)
class PublicationTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'short_description')
