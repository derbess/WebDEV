from rest_framework import serializers
from api.models import TaskList, Task
from api import models


class TaskListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True),
    name = serializers.CharField(max_length=200)

    def create(self, validated_data):
        task_list = TaskList(**validated_data)
        task_list.save()
        return task_list

    def update(self, instance, validated_data):
        instance.name= validated_data.get('name', instance.name)
        instance.save()
        return instance


class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    task_list = TaskListSerializer(required=False)
    created_at = serializers.DateTimeField(required=False)
    due_on = serializers.DateTimeField(required=False)

    class Meta:
        model = Task
        fields = '__all__'