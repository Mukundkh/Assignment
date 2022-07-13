from rest_framework import serializers

class ScrapingSerializers(serializers.ModelSerializer):

    model = Book;
    fields = '__all__'

