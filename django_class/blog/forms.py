from django import forms
from .models import Post


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100, label="نام", widget=forms.TextInput(attrs={"placeholder": "نام خود را وارد کنید"})
    )
    email = forms.EmailField(label="ایمیل", widget=forms.EmailInput(attrs={"placeholder": "example#gmail.com"}))
    subject = forms.CharField(max_length=200, label="موضوع", required=False)
    message = forms.CharField(label="پیام", widget=forms.Textarea(attrs={"rows": 5}))

    def clean_message(self):
        message = self.cleaned_data["message"]
        if len(message) < 20:
            raise forms.ValidationError("پیام باید حداقل 20 کاراکتر باشد")
        return message

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name", "")
        email = cleaned_data.get("email", "")
        if name and email and name.lower() in email.lower():
            raise forms.ValidationError("ایمیل نباید داخل  نام باشد")
        return cleaned_data


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "content", "image", "is_published", "price")
        labels = {"title": "عنوان", "content": "محتوا"}
        help_texts = {"title": "عنوان پست باید بیشتر از سه کاراکتر داشته باشد"}
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "عنوان پست را وارد کنید",
                    "maxlength": 120,
                }
            )
        }

    def clean_title(self):
        title = self.cleaned_data["title"]
        if len(title) < 5:
            raise forms.ValidationError("عنوان باید حداقل 3 کاراکتر باشد")
        return title.strip()


class SearchForm(forms.Form):
    query = forms.CharField()
