from django import forms
from .models import Video
# from .models import Comment


# class VideoForm(forms.ModelForm):
#     class Meta:
#         model = Video
#         fields = ['title', 'description', 'video_file']

#     def clean_video_file(self):
#         video_file = self.cleaned_data.get('video_file')
#         if video_file:
#             # Check if the video file size is less than 100 MB
#             if video_file.size > 100 * 1024 * 1024:
#                 raise forms.ValidationError(
#                     'The video file size must be less than 100 MB.')
#             # Check if the video file format is supported
#             if not video_file.name.endswith(('.mp4', '.mov', '.avi')):
#                 raise forms.ValidationError(
#                     'The video file format is not supported. Please upload a .mp4, .mov, or .avi file.')
#         return video_file


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['text']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['text'].widget.attrs.update({'class': 'form-control'})

#     def clean(self):
#         cleaned_data = super().clean()
#         text = cleaned_data.get('text')
#         if len(text) < 10:
#             raise forms.ValidationError(
#                 'The comment must be at least 10 characters long.')
#         return cleaned_data
