"""
Tests for models.
"""
from django.test import TestCase
import pytest
from django.contrib.auth import get_user_model
from django.db.models import Avg
from core_apps.profiles.models import Profile

User = get_user_model()

class ProfileModelTests(TestCase):
    """Test models."""
    
    @pytest.mark.django_db
    def test_profile_default_values(self):
        user = User.objects.create(username='testuser1')
        profile = user.profile  # Retrieve the automatically created profile
        assert profile.gender == Profile.Gender.OTHER
        assert profile.occupation == Profile.Occupation.TENANT
        assert profile.phone_number == '+250784123456'
        assert profile.country_of_origin == 'US'
        assert profile.city_of_origin == 'Los Angeles'
        assert profile.report_count == 0
        assert profile.reputation == 100

    @pytest.mark.django_db
    def test_profile_slug_generation(self):
        user = User.objects.create(username='testuser2')
        profile = user.profile  # Retrieve the automatically created profile
        assert profile.slug == 'testuser2'

    # @pytest.mark.django_db
    # def test_profile_is_banned_property(self):
    #     user = User.objects.create(username='testuser3')
    #     profile = user.profile
    #     assert profile.is_banned is True
    #     profile.report_count = 4
    #     profile.save()
    #     assert profile.is_banned is False

    @pytest.mark.django_db
    def test_profile_update_reputation(self):
        user = User.objects.create(username='testuser4')
        profile = user.profile
        profile.report_count = 3  # Ensure the condition for updating reputation is met
        profile.update_reputation()
        assert profile.reputation == 40

    @pytest.mark.django_db
    def test_profile_save_method(self):
        user = User.objects.create(username='testuser5')
        profile = user.profile
        profile.report_count = 3  # Ensure the condition for updating reputation is met
        profile.save()
        assert profile.reputation == 40

    @pytest.mark.django_db
    def test_profile_get_average_rating(self):
        user = User.objects.create(username='testuser6')
        profile = user.profile
        assert profile.get_average_rating() == 0.0
        # Assuming a Rating model exists and is related to User
        # Rating.objects.create(user=user, rating=4)
        # Rating.objects.create(user=user, rating=5)
        # assert profile.get_average_rating() == 4.5 