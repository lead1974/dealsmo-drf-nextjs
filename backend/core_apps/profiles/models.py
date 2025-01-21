from autoslug import AutoSlugField
from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from core_apps.common.models import TimeStampedModel

User = get_user_model()


def get_user_username(instance: "Profile") -> str:
    return instance.user.username


class Profile(TimeStampedModel):
    class Gender(models.TextChoices):
        MALE = ("male", _("Male"))
        FEMALE = ("female", _("Female"))
        OTHER = ("other", _("Other"))

    class Occupation(models.TextChoices):
        Developer = ("developer", _("Developer"))
        Content_Manager = ("content_manager", _("Content Manager"))
        Digital_Marketing = ("digital_marketing", _("Digital Marketing"))
        Customer_Support = ("customer_support", _("Customer Support"))
        Data_Analyst = ("data_analyst", _("Data Analyst"))
        Graphic_Designer = ("graphic_designer", _("Graphic Designer"))
        Legal_Compliance = ("lega_compliance", _("Legal Compliance"))
        User = ("user", _("User"))

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = CloudinaryField(verbose_name=_("Avatar"), blank=True, null=True)
    gender = models.CharField(
        verbose_name=_("Gender"),
        max_length=10,
        choices=Gender.choices,
        default=Gender.OTHER,
    )
    bio = models.TextField(verbose_name=_("Bio"), blank=True, null=True)
    occupation = models.CharField(
        verbose_name=_("Occupation"),
        max_length=20,
        choices=Occupation.choices,
        default=Occupation.User,
    )
    phone_number = PhoneNumberField(
        verbose_name=_("Phone Number"), max_length=30, default="+250784123456"
    )
    country_of_origin = CountryField(verbose_name=_("Country"), default="USA")
    city_of_origin = models.CharField(
        verbose_name=_("City"), max_length=180, default="Los Angeles"
    )
    report_count = models.IntegerField(verbose_name=_("Report Count"), default=0)
    reputation = models.IntegerField(verbose_name=_("Reputation"), default=100)
    slug = AutoSlugField(populate_from=get_user_username, unique=True)

    @property
    def is_banned(self) -> bool:
        return self.report_count >= 5

    def update_reputation(self):
        self.reputation = max(0, 100 - self.report_count * 20)

    def save(self, *args, **kwargs):
        self.update_reputation()
        super().save(*args, **kwargs)