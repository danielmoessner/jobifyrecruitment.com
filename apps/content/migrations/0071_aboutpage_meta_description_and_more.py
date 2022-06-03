# Generated by Django 4.0.3 on 2022-06-02 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0070_remove_applicant_profession_applicant_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='meta_description',
            field=models.TextField(blank=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='meta_description_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='meta_description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='meta_title',
            field=models.TextField(blank=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='meta_title_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='meta_title_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='agbpage',
            name='meta_description',
            field=models.TextField(blank=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='agbpage',
            name='meta_description_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='agbpage',
            name='meta_description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='agbpage',
            name='meta_title',
            field=models.TextField(blank=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='agbpage',
            name='meta_title_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='agbpage',
            name='meta_title_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='applicantshowitworkspage',
            name='meta_description',
            field=models.TextField(blank=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='applicantshowitworkspage',
            name='meta_description_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='applicantshowitworkspage',
            name='meta_description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='applicantshowitworkspage',
            name='meta_title',
            field=models.TextField(blank=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='applicantshowitworkspage',
            name='meta_title_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='applicantshowitworkspage',
            name='meta_title_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='meta_description',
            field=models.TextField(blank=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='meta_description_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='meta_description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='meta_title',
            field=models.TextField(blank=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='meta_title_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='meta_title_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='contactthankspage',
            name='meta_description',
            field=models.TextField(blank=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='contactthankspage',
            name='meta_description_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='contactthankspage',
            name='meta_description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='contactthankspage',
            name='meta_title',
            field=models.TextField(blank=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='contactthankspage',
            name='meta_title_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='contactthankspage',
            name='meta_title_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='meta_description',
            field=models.TextField(blank=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='meta_description_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='meta_description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='meta_title',
            field=models.TextField(blank=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='meta_title_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='meta_title_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='employerhowitworkspage',
            name='meta_description',
            field=models.TextField(blank=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='employerhowitworkspage',
            name='meta_description_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='employerhowitworkspage',
            name='meta_description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='employerhowitworkspage',
            name='meta_title',
            field=models.TextField(blank=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='employerhowitworkspage',
            name='meta_title_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='employerhowitworkspage',
            name='meta_title_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='imprintpage',
            name='meta_description',
            field=models.TextField(blank=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='imprintpage',
            name='meta_description_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='imprintpage',
            name='meta_description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='imprintpage',
            name='meta_title',
            field=models.TextField(blank=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='imprintpage',
            name='meta_title_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='imprintpage',
            name='meta_title_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='indexpage',
            name='meta_description',
            field=models.TextField(blank=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='indexpage',
            name='meta_description_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='indexpage',
            name='meta_description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='indexpage',
            name='meta_title',
            field=models.TextField(blank=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='indexpage',
            name='meta_title_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='indexpage',
            name='meta_title_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='initiativeapplicationpage',
            name='meta_description',
            field=models.TextField(blank=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='initiativeapplicationpage',
            name='meta_description_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='initiativeapplicationpage',
            name='meta_description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='initiativeapplicationpage',
            name='meta_title',
            field=models.TextField(blank=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='initiativeapplicationpage',
            name='meta_title_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='initiativeapplicationpage',
            name='meta_title_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='initiativeapplicationthankspage',
            name='meta_description',
            field=models.TextField(blank=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='initiativeapplicationthankspage',
            name='meta_description_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='initiativeapplicationthankspage',
            name='meta_description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='initiativeapplicationthankspage',
            name='meta_title',
            field=models.TextField(blank=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='initiativeapplicationthankspage',
            name='meta_title_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='initiativeapplicationthankspage',
            name='meta_title_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='jobseekerfaqpage',
            name='meta_description',
            field=models.TextField(blank=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='jobseekerfaqpage',
            name='meta_description_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='jobseekerfaqpage',
            name='meta_description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='jobseekerfaqpage',
            name='meta_title',
            field=models.TextField(blank=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='jobseekerfaqpage',
            name='meta_title_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='jobseekerfaqpage',
            name='meta_title_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='portalpage',
            name='meta_description',
            field=models.TextField(blank=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='portalpage',
            name='meta_description_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='portalpage',
            name='meta_description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='portalpage',
            name='meta_title',
            field=models.TextField(blank=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='portalpage',
            name='meta_title_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='portalpage',
            name='meta_title_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='privacypage',
            name='meta_description',
            field=models.TextField(blank=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='privacypage',
            name='meta_description_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='privacypage',
            name='meta_description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='privacypage',
            name='meta_title',
            field=models.TextField(blank=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='privacypage',
            name='meta_title_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='privacypage',
            name='meta_title_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='servicespage',
            name='meta_description',
            field=models.TextField(blank=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='servicespage',
            name='meta_description_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='servicespage',
            name='meta_description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='servicespage',
            name='meta_title',
            field=models.TextField(blank=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='servicespage',
            name='meta_title_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='servicespage',
            name='meta_title_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='staffingsolutionspage',
            name='meta_description',
            field=models.TextField(blank=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='staffingsolutionspage',
            name='meta_description_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='staffingsolutionspage',
            name='meta_description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='staffingsolutionspage',
            name='meta_title',
            field=models.TextField(blank=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='staffingsolutionspage',
            name='meta_title_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='staffingsolutionspage',
            name='meta_title_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='submitpositionpage',
            name='meta_description',
            field=models.TextField(blank=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='submitpositionpage',
            name='meta_description_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='submitpositionpage',
            name='meta_description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='submitpositionpage',
            name='meta_title',
            field=models.TextField(blank=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='submitpositionpage',
            name='meta_title_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='submitpositionpage',
            name='meta_title_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='submitpositionthankspage',
            name='meta_description',
            field=models.TextField(blank=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='submitpositionthankspage',
            name='meta_description_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='submitpositionthankspage',
            name='meta_description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='submitpositionthankspage',
            name='meta_title',
            field=models.TextField(blank=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='submitpositionthankspage',
            name='meta_title_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='submitpositionthankspage',
            name='meta_title_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='submitreferralpage',
            name='meta_description',
            field=models.TextField(blank=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='submitreferralpage',
            name='meta_description_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='submitreferralpage',
            name='meta_description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='submitreferralpage',
            name='meta_title',
            field=models.TextField(blank=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='submitreferralpage',
            name='meta_title_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='submitreferralpage',
            name='meta_title_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='submitreferralthankspage',
            name='meta_description',
            field=models.TextField(blank=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='submitreferralthankspage',
            name='meta_description_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='submitreferralthankspage',
            name='meta_description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='submitreferralthankspage',
            name='meta_title',
            field=models.TextField(blank=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='submitreferralthankspage',
            name='meta_title_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='submitreferralthankspage',
            name='meta_title_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='videoresumepage',
            name='meta_description',
            field=models.TextField(blank=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='videoresumepage',
            name='meta_description_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='videoresumepage',
            name='meta_description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='videoresumepage',
            name='meta_title',
            field=models.TextField(blank=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='videoresumepage',
            name='meta_title_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='videoresumepage',
            name='meta_title_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='whytoworkwithuspage',
            name='meta_description',
            field=models.TextField(blank=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='whytoworkwithuspage',
            name='meta_description_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='whytoworkwithuspage',
            name='meta_description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='whytoworkwithuspage',
            name='meta_title',
            field=models.TextField(blank=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='whytoworkwithuspage',
            name='meta_title_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='whytoworkwithuspage',
            name='meta_title_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='workinginaustriapage',
            name='meta_description',
            field=models.TextField(blank=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='workinginaustriapage',
            name='meta_description_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='workinginaustriapage',
            name='meta_description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Description'),
        ),
        migrations.AddField(
            model_name='workinginaustriapage',
            name='meta_title',
            field=models.TextField(blank=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='workinginaustriapage',
            name='meta_title_de',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
        migrations.AddField(
            model_name='workinginaustriapage',
            name='meta_title_en',
            field=models.TextField(blank=True, null=True, verbose_name='Meta > Title'),
        ),
    ]