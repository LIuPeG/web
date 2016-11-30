#coding=utf-8
from django import forms
from focus.models import Comment

class CommentForm(forms.ModelForm):



	class Meta:
		model = Comment
		exclude = ("article",)

