import re

from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from xmodule.modulestore.django import modulestore
from xmodule.modulestore.exceptions import ItemNotFoundError
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from student.models import UserProfile, CourseEnrollment
from certificates.models import certificate_status_for_student, CertificateStatuses
from certificates.api import get_certificate_url
from openedx.core.djangoapps.lang_pref import LANGUAGE_KEY
from openedx.core.djangoapps.user_api.preferences import api as preferences_api



class UserSerializer(serializers.ModelSerializer):
    """
    Serializes user and corresponding profile to unite object

    Represents username as uid (since it's a technical field),
    profile.name as name
    """
    uid = serializers.CharField(source='username', required=True, allow_blank=False, validators=[UniqueValidator(queryset=User.objects)])
    email = serializers.EmailField(required=False, allow_null=False, validators=[UniqueValidator(queryset=User.objects)])

    name = serializers.CharField(source='profile.name', default='', max_length=255, required=False, allow_blank=True)
    nickname = serializers.CharField(source='profile.nickname', default='', max_length=255, required=False, allow_blank=True)
    first_name = serializers.CharField(source='profile.first_name', default='', max_length=255, required=False, allow_blank=True)
    last_name = serializers.CharField(source='profile.last_name', default='', max_length=255, required=False, allow_blank=True)
    birthdate = serializers.DateField(source='profile.birthdate', default=None, required=False, allow_null=True)
    city = serializers.CharField(source='profile.city', default='', required=False, allow_blank=True)
    gender = serializers.ChoiceField(source='profile.gender', choices=UserProfile.GENDER_CHOICES,
                                     default=None, required=False, allow_null=True)

    class Meta:
        model = User
        fields = ('uid', 'email', 'name', 'nickname', 'first_name', 'last_name',
                  'birthdate', 'city', 'gender')
        lookup_field = 'uid'
