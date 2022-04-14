from modeltranslation.translator import translator, TranslationOptions
from apps.content.models import WhyToWorkWithUsPage, Service, SubmitReferralPage, StaffCategory, \
    ApplicantsHowItWorksPage, WorkingInAustriaPage, VideoResumePage, EmployerFaqPage, StaffingSolutionsPage, \
    SubmitPositionPage, ServicesPage, AboutPage, MemberCategory, Member, PortalPage, ContactPage


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


class MemberCategoryTranslateOptions(TranslationOptions):
    fields = ['title']


class MemberTranslateOptionsOptions(TranslationOptions):
    fields = ['role']


# not pages
translator.register(MemberCategory, MemberCategoryTranslateOptions)
translator.register(Member, MemberTranslateOptionsOptions)
translator.register(Service, AllFields(Service))
translator.register(StaffCategory, AllFields(StaffCategory))
# page
translator.register(PortalPage, AllFields(PortalPage))
translator.register(WhyToWorkWithUsPage, AllFields(WhyToWorkWithUsPage))
translator.register(SubmitReferralPage, AllFields(SubmitReferralPage))
translator.register(ApplicantsHowItWorksPage, AllFields(ApplicantsHowItWorksPage))
translator.register(WorkingInAustriaPage, AllFields(WorkingInAustriaPage))
translator.register(VideoResumePage, AllFields(VideoResumePage))
translator.register(EmployerFaqPage, AllFields(EmployerFaqPage))
translator.register(StaffingSolutionsPage, AllFields(StaffingSolutionsPage))
translator.register(SubmitPositionPage, AllFields(SubmitPositionPage))
translator.register(ServicesPage, AllFields(ServicesPage))
translator.register(AboutPage, AllFields(AboutPage))
translator.register(ContactPage, AllFields(ContactPage))
