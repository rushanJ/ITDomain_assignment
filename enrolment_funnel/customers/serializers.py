from rest_framework import serializers
from .models import Customer,FunnelAssignment
from funnel.models import Funnel
from funnel.serializers import FunnelSerializer
from django.shortcuts import get_object_or_404
 
class FunnelAssignmentSerializer(serializers.ModelSerializer):
    funnel_id = serializers.PrimaryKeyRelatedField(
        queryset=Funnel.objects.all(),
        source='funnel'
    )

    class Meta:
        model = FunnelAssignment
        fields = ['id', 'funnel_id', 'customer', 'added_at']

    def create(self, validated_data):
        print (validated_data)
        funnel_instance = validated_data.pop('funnel')
        funnel_assignment = FunnelAssignment.objects.create(funnel=funnel_instance, **validated_data)
        print (funnel_assignment.funnel_id)
        return funnel_assignment
    
    

class CustomerSerializer(serializers.ModelSerializer):
    funnels = FunnelAssignmentSerializer(many=True, read_only=True, source='funnelassignment_set')
    class Meta:
        model = Customer
        fields = ['id', 'created', 'name', 'email', 'funnels']

    
    def create(self, validated_data):
        funnels_data = validated_data.pop('funnel',[])
        print (validated_data)
        customer = Customer.objects.create(**validated_data)
        funnel_instance = get_object_or_404(Funnel, pk=1)
        print (funnel_instance)

        funnel_assignment=FunnelAssignment.objects.create(customer=customer,funnel=funnel_instance)
        for funnel_data in funnels_data:
            FunnelAssignment.objects.create(customer=customer, **funnel_data)

        return customer
        

    def update(self, instance, validated_data):
        funnels_data = validated_data.pop('funnels', [])

        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        # Remove existing funnels
        instance.funnels.all().delete()

        # Create new FunnelAssignment instances
        for funnel_data in funnels_data:
            FunnelAssignment.objects.create(customer=instance, **funnel_data)

        return instance

    