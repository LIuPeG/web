#coding=utf-8
from django import forms
from focus.models import Comment

###评论表单
class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = "__all__"

###注册表单
class RegForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username","required":"required"}),
	                           max_length=50,error_messages={"required":"Username不能为空",})
	email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "Email", "required": "required"}),
	                           max_length=50, error_messages={"required": "email不能为空", })
	url = forms.URLField(widget=forms.TextInput(attrs={"placeholder": "Url",}),
	                           max_length=100, required=False)
	password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password", "required": "required"}),
	                           max_length=50, error_messages={"required": "Password不能为空", })

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username","required":"required"},),
	                                                  max_length=50,error_messages={"required":"username不能为空",})
	password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password","required":"required",}),
	                           max_length=50,error_messages={"required":"password不能为空",})

