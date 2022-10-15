from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class ArticleSerializer(serializers.Serializer):
    article_file = serializers.FileField(required=False)
    article = serializers.CharField(required=False)

    def validate_article_file(self, article_file):
        if not article_file.name.endswith('.xlsx'):
            raise ValidationError("File type should be xlsx")
        return article_file

    # class Meta:
    #     extra_kwargs = {
    #         "article_file": {"required": False},
    #         "article": {"required": False}
    #     }
