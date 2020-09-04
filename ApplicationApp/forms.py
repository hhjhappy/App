# -*- coding: utf-8 -*-
"""
@Author : hejian
@File   : forms.py
@Project: Application
@Time   : 2020-08-25 16:23:29
@Desc   : The file is ...
@Version: v1.0
"""

from . import models
from django import forms
import time


def grantOrderNumber():
    struct_time = time.localtime(time.time())
    number = time.strftime("%Y%m%d%H%M%S", struct_time)
    return number


'''class applicationUnitInformationforms(forms.ModelForm):

    class Meta:
        model = models.applicationUnitInformation
        fields = '__all__'
        exclude = ['applicationUnitInformationlink']

class applicantInformationForms(forms.ModelForm):
    telephoneNumber = forms.IntegerField(label='电话号码',required=False)
    phoneNumber = forms.IntegerField(label='手机号码',required=False)
    mail = forms.EmailField(label='邮箱地址',required=False)

    class Meta:
        model = models.applicantInformation
        fields = ['name','telephoneNumber','phoneNumber','mail']
        exclude = ['applicantInformationlink']

class resourceTypeForm(forms.ModelForm):
    typelist = (
        (1,'专线IP'),
        (2,'电信专线'),
        (3,'联通专线'),
        (4,'其他(请填写)'),
    )
    devices = (
        (1,'无线路由器'),
        (2,'交换机'),
        (3,'录像机'),
        (4,'无'),
        (5,'其他(请填写)'),
    )
    Type = forms.ChoiceField(label='资源类型',choices=typelist,widget=forms.RadioSelect)
    otherDevices = forms.ChoiceField(label='其他设备', choices=devices, widget=forms.RadioSelect,required=False)
    typeRemark = forms.CharField(label='资源类型备注',required=False)
    DevicesRemark = forms.CharField(label='网络设备备注',required=False)
    class Meta:
        model = models.resourceType
        fields = '__all__'
        exclude = ['resourceTypelink']'''




class otherforms(forms.ModelForm):
    typelist = (
        (1,'专线IP'),
        (2,'电信专线'),
        (3,'联通专线'),
        (4,'其他(请填写)'),
    )
    devices = (
        (1,'无线路由器'),
        (2,'交换机'),
        (3,'录像机'),
        (4,'无'),
        (5,'其他(请填写)'),
    )
    Type = forms.ChoiceField(label='资源类型',choices=typelist,widget=forms.RadioSelect)
    otherDevices = forms.ChoiceField(label='其他设备', choices=devices, widget=forms.RadioSelect,required=False)
    typeRemark = forms.CharField(label='资源类型备注',required=False)
    DevicesRemark = forms.CharField(label='网络设备备注',required=False)
    theTerm = forms.CharField(label='到期时间',widget=forms.TextInput(attrs={'type':'date'}))
    telephoneNumber = forms.IntegerField(label='电话号码',required=False)
    phoneNumber = forms.IntegerField(label='手机号码',required=False)
    mail = forms.EmailField(label='邮箱地址',required=False)


    class Meta:
        model = models.Other
        fields = '__all__'
        exclude = ['applicationTime','Numbering']


class backstageforms(forms.ModelForm):

    class Meta:
        model = models.backstage
        fields = ['filesname']
        exclude = ['link']