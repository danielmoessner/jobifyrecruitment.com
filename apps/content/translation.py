from modeltranslation.translator import translator, TranslationOptions
from apps.content.models import WhyToWorkWithUsPage, Service


def get_fields_from_model_class(model_class):
    fields = model_class._meta.fields
    fields = [f.name for f in fields]
    for name in ['id', 'created', 'updated', 'image', 'ordering']:
        if name in fields:
            fields.remove(name)
    return fields


class AllFields:
    def __new__(cls, model_class, *args, **kwargs):
        class AllFieldsTranslateOptions(TranslationOptions):
            fields = get_fields_from_model_class(model_class)

        return AllFieldsTranslateOptions


translator.register(WhyToWorkWithUsPage, AllFields(WhyToWorkWithUsPage))
translator.register(Service, AllFields(Service))
