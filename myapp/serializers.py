import re

from django.template.defaultfilters import slugify
from rest_framework import serializers
from .models import EmployeeTable, TimingCreateTable


class EmpSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()

    class Meta:
        model = EmployeeTable
        fields = "__all__"

    def get_slug(self, obj):
        return slugify(obj.company_name)

    # first method of validation in serializers class
    # def validate(self,validated_data):
    #
    #     print(validated_data)
    #     if validated_data.get('company_name'):
    #         company_name = validated_data['company_name']
    #         regex = re.compile('[@_!#%^&*()<>?/\|}{~:]')
    #         if len(company_name) <3:
    #             raise serializers.ValidationError("Company name shuld be more than 3 characters")
    #         if not regex.search(company_name)==None:
    #             raise serializers.ValidationError('Company name cannot contain special character')
    #     return validated_data
    #

    def validate_company_name(self, data):

        print(data)
        if data:
            company_name = data
            regex = re.compile('[@_!#%^&*()<>?/\|}{~:]')
            if len(company_name) < 3:
                raise serializers.ValidationError("Company name shuld be more than 3 characters")
            if not regex.search(company_name) == None:
                raise serializers.ValidationError('Company name cannot contain special character')
        return data


class TimingCreateTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimingCreateTable
        exclude = ['created_at', 'updated_at']
        depth = 1 #is used to diplay the data with timeCreatetable..

