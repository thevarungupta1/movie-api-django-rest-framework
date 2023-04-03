from rest_framework import serializers
from watchlist_app.models import Movie

# 3 - validators method for validation
# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError('Name must be at least 2 characters')
       


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     # 2 - object level validation
#     def validate(name, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('name and description cannot be same')
#         else:
#             return data
    
    # 1 - filed level validation
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError('Name must be at least 2 characters')
    #     return value
            
        
        
class MovieSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Movie
        fields = "__all__"
        #fields = ['id', 'name', 'description']
        #exclude = ['active']
    
    def get_len_name(self, object):        
        return len(object.name)
        
    def validate(name, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('name and description cannot be same')
        else:
            return data
    
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError('Name must be at least 2 characters')
        return value