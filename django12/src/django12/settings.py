"""
Django settings for django12 project.

Generated by 'django-admin startproject' using Django 2.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from django.urls.base import reverse_lazy
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#LOGIN_URL: login_required 데코레이터/LoginRequiredMixin 클래스를 통해 비로그인 회원이 이동할 로그인 페이지의 주소
LOGIN_URL= reverse_lazy('login:signin')
#소셜로그인을 한 뒤 이동할 주소(기본값이 /account/profile/)
LOGIN_REDIRECT_URL='/'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '34l75#i5xl*)_5!e_@d(z1a7za^^+l_l*qj35ia$5@v6akd5h!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
#인증관련 모듈을 추가하는 변수
AUTHENTICATION_BACKENDS=(
    #구글로그인 처리 관련 파이썬 클래스 추가
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.google.GoogleOpenId',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.google.GooglePlusAuth',
    #소셜로그인 정보를 Django의 User모델클레스에 저장하는 파이썬 클래스 추가
    'django.contrib.auth.backends.ModelBackend',
    
    )
#구글개발자 사이트에서 발급받은 ID저장변수
SOCIAL_AUTH_GOOGLE_PLUS_KEY='571524753149-a5nepv0v1m2avjk7faqggll018p41qas.apps.googleusercontent.com'
#구글개발자 사이트에서 발급받은 보안비밀 저장변수
SOCIAL_AUTH_GOOGLE_PLUS_SECRET='FYiSGHOV4kmhvdkij68DsH4h'
# Application definition
# 프로젝트 내에서 실행할 어플리케이션을 등록하는 변수
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookmark', #bookmark 어플리케이션을 프로젝트에 추가
    'vote',
    'customlogin',
    #social-auth-app-django 모듈이 설치되야 사용가능
    'social_django', #소셜로그인에 관련된 처리를 하는 어플리케이션
    'blog',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django12.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                #소셜로그인을 처리하기 위한 템플릿 관련 함수추가
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'django12.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ko'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
#URL 주소로 파일주소를 접근할 때 사용하는 변수
#127.0.0.1:8000/files/로 싲ㄱ하는 경로는 미디어파일을 불러오는것으로 판단
MEDIA_URL=''
#실제로 파일이 저장되는 하드웨어 경로
#c:/files에다가 저장하도록 설정-> MEDIA_ROOT = 'c:/files/'
#현재 프로젝트 폴더/files/에 업로드한 파일들을 저장하도록 설정
#os.path.join(기존경로, 새경로): 기존경로에 새경로를 붙인 문자열을 반환
#BASE_DIR: 웹프로젝트가 저장된 경로
MEDIA_ROOT=os.path.join(BASE_DIR,'files')#django12/src/files에다가 저장되도록 설정
MEDIA_ROOT=''
