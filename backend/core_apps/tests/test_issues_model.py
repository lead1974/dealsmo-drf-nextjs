"""
Tests for models.
"""

from django.test import TestCase
import pytest
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from core_apps.issues.models import Issue

User = get_user_model()

class IssueModelTests(TestCase):
    """Test models."""

    @pytest.mark.django_db
    def test_issue_creation(self):
        user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpass')
        issue = Issue.objects.create(
            reported_by=user,
            title='Test Issue',
            description='This is a test issue.'
        )
        assert issue.title == 'Test Issue'
        assert issue.status == Issue.IssueStatus.REPORTED
        assert issue.priority == Issue.Priority.LOW

    @pytest.mark.django_db
    def test_issue_str_method(self):
        user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpass')
        issue = Issue.objects.create(
            reported_by=user,
            title='Test Issue',
            description='This is a test issue.'
        )
        assert str(issue) == 'Test Issue'


    @pytest.mark.django_db
    def test_issue_invalid_status_choice(self):
        user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpass')
        issue = Issue(
            reported_by=user,
            title='Test Issue',
            description='This is a test issue.',
            status='invalid_status'
        )
        with pytest.raises(ValidationError):
            issue.full_clean()

    @pytest.mark.django_db
    def test_issue_relationships(self):
        user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpass')
        assigned_user = User.objects.create_user(username='assigneduser', email='assigneduser@example.com', password='testpass')
        issue = Issue.objects.create(
            reported_by=user,
            assigned_to=assigned_user,
            title='Test Issue',
            description='This is a test issue.'
        )
        assert issue.reported_by == user
        assert issue.assigned_to == assigned_user 

    # @pytest.mark.django_db
    # def test_issue_save_method_calls_notify_assigned_user(self, mocker):
    #     user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpass')
    #     assigned_user = User.objects.create_user(username='assigneduser', email='assigneduser@example.com', password='testpass')
    #     issue = Issue.objects.create(
    #         reported_by=user,
    #         title='Test Issue',
    #         description='This is a test issue.'
    #     )
    #     mock_notify = mocker.patch.object(issue, 'notify_assigned_user')
    #     issue.assigned_to = assigned_user
    #     issue.save()
    #     mock_notify.assert_called_once()