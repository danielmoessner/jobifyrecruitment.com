from django.utils.translation import gettext_lazy as _

LANGUAGE_CHOICES_RAW = [
    "Javanese",
    "Afghan",
    "Afrikaans",
    "Albanian",
    "Amharic",
    "Arabic",
    "Aramaic",
    "Armenian",
    "Azerbaijanian",
    "Bahasa",
    "Bahasa Malaysia",
    "Balinese",
    "Bambara",
    "Bangladeshi",
    "Bassa",
    "Belgian",
    "Balochi",
    "Bengali",
    "Bangladeshi",
    "Bhojpuri",
    "Bicol",
    "Bosnian",
    "Bulgarian",
    "Burmese",
    "Cebuano",
    "Chichewa (Nyabja)",
    "Contonese",
    "Danish",
    "German",
    "Dhivehi",
    "English",
    "Estonian",
    "Fiji",
    "Finnish",
    "French",
    "Gan",
    "Georgian",
    "Gilaki",
    "Greek",
    "Gujarati",
    "Hainan",
    "Hakka",
    "Hausa",
    "Hebrew",
    "Hiligaynon",
    "Hiligayon",
    "Hindi",
    "Hindko",
    "Hokkien (Chuanchew - Changchew)",
    "Igbo",
    "Ilokano",
    "Indian",
    "Indonesian",
    "Indonesian",
    "Iranian",
    "Irish",
    "Icelandic",
    "Italian",
    "Jamaican Creole",
    "Japanese",
    "Kanuri",
    "Kazakh",
    "Kashmiri",
    "Catalan",
    "Khmer",
    "Kimbundu",
    "Kyrgyz",
    "Kirundi",
    "Konkani",
    "Korean",
    "Croatian",
    "Kurdish",
    "Laotian",
    "Latvian",
    "Lithuanian",
    "Luganda",
    "Luxembourgian",
    "Madurese",
    "Maithili",
    "Makhuwa",
    "Malagasy",
    "Malay",
    "Malayalam",
    "Maltese",
    "Mandarin",
    "Marathi",
    "Moroccan",
    "Mazanderani",
    "Macedonian",
    "Mazedonian",
    "Mongolian",
    "Nepali",
    "Dutch",
    "Northern Sotho (sePedi)",
    "Norwegian",
    "Oriya",
    "Oromo",
    "Pahari-Potwari",
    "Papiamento",
    "Pashto",
    "Persian (Farsi)",
    "Filipino",
    "Piemonteis",
    "Polish",
    "Portuguese",
    "Punjabi",
    "Quechua",
    "Rajasthani",
    "Rhaeto-Romanic",
    "Romani",
    "Romanian",
    "Russian",
    "Samoan",
    "Santali",
    "Sardinian",
    "Swedish",
    "Swiss German",
    "Senegalese",
    "Serbian",
    "Serbo-Croatian",
    "Sesotho (southern)",
    "Setswana",
    "Shona",
    "Sindhi",
    "Singhalese",
    "Sinhalese",
    "Siraiki",
    "Slovak",
    "Slovenian",
    "Somali",
    "Spain",
    "Sundanese",
    "Swahili",
    "Swahili (Kishuaheli)",
    "Swahili (Kisuaheli)",
    "Tadjik",
    "Tagalog",
    "Tahitian",
    "Taiwanese",
    "Tajik",
    "Tamazight (Berber)",
    "Tamil",
    "Tatar",
    "Telugu",
    "Teochew",
    "Thai",
    "Thailand",
    "Theochew",
    "Tibetan",
    "Tigrinya",
    "Czech",
    "Turkish",
    "Turkmen",
    "Ukrainian",
    "Hungarian",
    "Urdu",
    "Usbek",
    "Uyghur",
    "Uzbek",
    "Vietnamese",
    "Waray-Waray",
    "Belarusian",
    "Wolof",
    "Wu",
    "Xhosa",
    "Yi",
    "Yoruba",
    "Zulu",
]

LANGUAGE_CHOICES = [('', '---------')] + list(map(lambda x: (x, x), LANGUAGE_CHOICES_RAW))

PRIVACY_LABEL = _('Privacy: Of course, your data will be treated confidentially and only passed on to third '
                  'parties after your consent. Yes, I agree to the data protection regulations.')

NATIONALITY_CHOICES_RAW = [
    "Afghan",
    "Egyptian",
    "Albanian",
    "Algerian",
    "United States",
    "Andorran",
    "Angolan",
    "Arabic",
    "Arabic (Saudi Arabia)",
    "Argentinian",
    "Armenian",
    "Azerbaijani",
    "Hong Kong",
    "Ethiopian",
    "Australian",
    "Bahamian",
    "Bahraini",
    "Bangladeshi",
    "Barbadian",
    "Belgian",
    "Belizean",
    "Beninese",
    "Bhutanese",
    "Bolivian",
    "Bosnian",
    "Botswanan",
    "Brazilian",
    "British",
    "British Virgin Islands",
    "Bruneian",
    "Bugarian",
    "Burkinabe",
    "Burundian",
    "Capetonian",
    "Cayman Islands",
    "Chad",
    "Chilean",
    "Chinese",
    "Costa Rican",
    "Danish",
    "German",
    "Djibouti",
    "Dominican",
    "Ecuadorian",
    "Eritrean",
    "Estonian",
    "Fijian",
    "Finnish",
    "French",
    "French (Guadeloupe)",
    "French Polynesia",
    "Gabon",
    "Gambian",
    "Georgian",
    "Ghanaian",
    "Greek",
    "Guam",
    "Guatemalan",
    "Guyana",
    "Haitian",
    "Honduran",
    "Indian",
    "Indonesian",
    "Iraqi",
    "Iranian",
    "Irish",
    "Icelandic",
    "Israeli",
    "Italian",
    "Ivorian",
    "Jamaican",
    "Japanese",
    "Yemeni",
    "Jersey",
    "Jordanian",
    "Caledonian",
    "Cambodian",
    "Cameroonian",
    "Canadian",
    "Kazakh",
    "Kenyan",
    "Kyrgyzstan",
    "Colombian",
    "Congolese",
    "Korean",
    "Croatian",
    "Cuban",
    "Kuwaiti",
    "Laotian",
    "Latvian",
    "Lebanese",
    "Liechtenstein",
    "Lithuanian",
    "Luxembourgian",
    "Macao",
    "Madagascan",
    "Malaysian",
    "Maldivian",
    "Malian",
    "Moroccan",
    "Mauretanian",
    "Mauritius",
    "Mexican",
    "Micronesian",
    "Moldovan",
    "Monacan",
    "Mongolian",
    "Mozambican",
    "Burmese",
    "Namibian",
    "Nepali",
    "New Zealand",
    "Nicaragua",
    "Dutch",
    "Dutch (Aruba)",
    "Dutch (Netherlands Antilles)",
    "Nigerian",
    "North Korean",
    "Nothern Mariana Islands",
    "Norwegian",
    "Omani",
    "Austrian",
    "Pakistani",
    "Palestine",
    "Palau",
    "Panamanian",
    "Papua New Guninea",
    "Paraguay",
    "Peru",
    "Philippines",
    "Polish",
    "Portugal",
    "Puerto Rico",
    "Qatar",
    "Rwandan",
    "Romanian",
    "Russian",
    "Zambian",
    "Swedish",
    "Swiss",
    "Senegal",
    "Serbian",
    "Zimbabwean",
    "Singaporean",
    "Slovak",
    "Slovenian",
    "Somali",
    "Spanish",
    "Sri-Lankan",
    "St. Vincent &amp; The Grenadines",
    "South African",
    "Sudanese",
    "Syrian",
    "Taiwanese",
    "Tanzanian",
    "Thai",
    "Togolese",
    "Trinidad &amp; Tobago",
    "Czech",
    "Tunisian",
    "Turkish",
    "Turkmenian",
    "Ugandan",
    "Ukrainian",
    "Hungarian",
    "Uruguayan",
    "Uzbekistan",
    "Venezuelan",
    "Vietnamese",
    "Virgin Islands (USA)",
    "Byelorussian",
    "West Indies",
    "Cypriot"
]

NATIONALITY_CHOICES = [('', '---------')] + list(map(lambda x: (x, x), NATIONALITY_CHOICES_RAW))
