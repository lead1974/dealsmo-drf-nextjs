from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.exceptions import PermissionDenied, ValidationError, NotFound
from rest_framework.response import Response
from core_apps.common.renderers import GenericJSONRenderer
from core_apps.profiles.models import Profile
from .serializers import RatingSerializer

User = get_user_model()


class RatingCreateAPIView(generics.CreateAPIView):
    serializer_class = RatingSerializer
    renderer_classes = [GenericJSONRenderer]
    object_label = "rating"

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        rated_user_username = serializer.validated_data.get("rated_user_username")
        try:
            rated_user = User.objects.get(username=rated_user_username)
        except User.DoesNotExist as e:
            raise NotFound(
                f"User with username '{rated_user_username}' does not exist."
            ) from e
        rating_user = request.user

        if rating_user == rated_user:
            raise PermissionDenied("You cannot review yourself.")

        try:
            rating_user_occupation = rating_user.profile.occupation
            rated_user_occupation = rated_user.profile.occupation
        except Profile.DoesNotExist as exc:
            raise ValidationError("Both users must have a valid occupation.") from exc

        # if (
        #     rating_user_occupation == Profile.Occupation.TENANT
        #     and rated_user_occupation == Profile.Occupation.TENANT
        # ):
        #     raise PermissionDenied("A tenant cannot review another tenant.")

        allowed_occupations = [
            Profile.Occupation.Admin,
            Profile.Occupation.Content_Manager,
            Profile.Occupation.Customer_Support,
            Profile.Occupation.Data_Analyst,
            Profile.Occupation.Digital_Marketing,
            Profile.Occupation.Graphic_Designer,
            Profile.Occupation.Legal_Compliance,
        ]

        # if (
        #     rating_user_occupation == Profile.Occupation.TENANT
        #     and rated_user_occupation not in allowed_occupations
        # ):
        #     raise PermissionDenied(
        #         "A tenant can only review staff members and not other tenants!"
        #     )

        if (
            rating_user_occupation != Profile.Occupation.TENANT
            and rating_user == rated_user
        ):
            raise PermissionDenied("A staff members cannot review themselves.")

        if (
            rating_user_occupation != Profile.Occupation.TENANT
            and rated_user_occupation != Profile.Occupation.TENANT
        ):
            raise PermissionDenied("A staff members cannot review another staff members.")

        rating = serializer.save(rating_user=rating_user, rated_user=rated_user)

        serializer = self.get_serializer(rating)
        headers = self.get_success_headers(serializer.data)

        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )