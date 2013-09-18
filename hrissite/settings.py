"""
Django settings for hrissite project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
gettext = lambda s: s
PROJECT_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd!4k3joz3@(wxlqnp!!knu-m+c#4&%-rps$x7qfn-(-&$ert6b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cms',
    'mptt',
    'menus',
    'south',
    'sekizai',
    'cms.plugins.file',
    'cms.plugins.flash',
    'cms.plugins.googlemap',
    'cms.plugins.link',
    'cms.plugins.picture',
    'cms.plugins.snippet',
    'cms.plugins.teaser',
    'cms.plugins.text',
    'cms.plugins.video',
    'cms.plugins.twitter',
    'cms_redirects',
    'easy_thumbnails',
    'cms.plugins.inherit',
   
    
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms_redirects.middleware.RedirectFallbackMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',   
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)  

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
)    




ROOT_URLCONF = 'hrissite.urls'

WSGI_APPLICATION = 'hrissite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'hrissite',
        'HOST': 'localhost',
        'PASSWORD':'kevdom',
        'PORT':'5433',
        'USER':'kelvin',
         
    }
}



# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
TEMPLATE_DIRS = (
    # The docs say it should be absolute path: PROJECT_PATH is precisely one.
    # Life is wonderful!
    os.path.join(PROJECT_PATH, "templates"),
)

LANGUAGES = [
    ('en', 'English'),
]

CMS_TEMPLATES = ( 
	('twitter1.html', gettext('home page template by bootstrap')),
	('twitter5.html', gettext('other pages template by bootstrap')),
	('twitter6.html', gettext('downloads template by bootstrap')),
	('twitter2.html', gettext('two column template by bootstrap')),
	('twitter3.html', gettext('two rows template by bootstrap')),
	('twitter4.html', gettext('three column template by bootstrap')),  
              
   )
#SITE_ID:
CMS_LANGUAGES = {
    1: [
        {
            'code': 'en',
            'name': gettext('English'),
            'fallbacks': ['de', 'fr'],
            'public': True,
            'hide_untranslated': True,
            'redirect_on_fallback':False,
        },
        {
            'code': 'de',
            'name': gettext('Deutsch'),
            'fallbacks': ['en', 'fr'],
            'public': True,
        },
        {
            'code': 'fr',
            'name': gettext('French'),
            'public': False,
        },
    ],
    2: [
        {
            'code': 'nl',
            'name': gettext('Dutch'),
            'public': True,
            'fallbacks': ['en'],
        },
    ],
    'default': {
        'fallbacks': ['en', 'de', 'fr'],
        'redirect_on_fallback':True,
        'public': False,
        'hide_untranslated': False,
    }
}

SITE_ID=1

#customization on django cms placeholder
CMS_PLACEHOLDER_CONF = {
'news':{
"plugins": ['LinkPlugin'],
'limits':{
'LinkPlugin': 10,
}
},

'article_tab_1':{
"plugins":['TextPlugin'],
'limits':{
'TextPlugin':1,
}
},
'article_tab_2':{
"plugins":['TextPlugin'],
'limits':{
'TextPlugin':1,
}
},
'article_tab_3':{
"plugins":['TextPlugin'],
'limits':{
'TextPlugin':1,
}
},
'main-contents':{
"plugins":['TextPlugin'],
'limits':{
'TextPlugin':10,
}
},
}

#enable CMS_SOFTROOT
CMS_SOFTROOT = True
MEDIA_ROOT = os.path.join(PROJECT_PATH, "media")
MEDIA_URL = "/media/"


STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
