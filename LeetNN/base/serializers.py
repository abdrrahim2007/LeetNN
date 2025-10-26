
from rest_framework import serializers
from .models import Library


class LibrarySerializer(serializers.ModelSerializer):
	thumbnail_url = serializers.ReadOnlyField()
	file_url = serializers.ReadOnlyField()


	class Meta:
		model = Library
		fields = ["id", "title", "author", "category", "year", "format", "thumbnail_url", "file_url"]