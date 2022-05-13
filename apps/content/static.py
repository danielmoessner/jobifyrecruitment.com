from django.utils.translation import gettext_lazy as _

LANGUAGE_CHOICES = [
    ('', '---------'),
    ('deu', 'German'),
    ('eng', 'English'),
    ('tgl', 'Tagalog'),
    ('taw', 'Tai')
]

PRIVACY_LABEL = _('Datenschutzhinweis: Selbstverständlich werden Ihre Daten vertraulich behandelt und erst nach ' \
                  'Ihrer Zustimmung an Dritte weitergegeben. Ja, ich erkläre mich mit den Datenschutzbestimmungen ' \
                  'einverstanden.')
