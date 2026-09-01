from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100, label="نام", widget=forms.TextInput(attrs={"placeholder": "نام خود را وارد کنید"})
    )
    email = forms.EmailField(label="ایمیل", widget=forms.EmailInput(attrs={"placeholder": "example#gmail.com"}))
    subject = forms.CharField(max_length=200, label="موضوع")
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


class PostForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        label="عنوان",
        widget=forms.TextInput(attrs={"placeholder": "عنوان پست ...", "class": "form-control"}),
    )
    content = forms.CharField(
        label="متن", widget=forms.Textarea(attrs={"placeholder": "عنوان پست ...", "class": "form-control"})
    )
    price = forms.CharField(
        max_length=100,
        label="قیمت",
        widget=forms.TextInput(attrs={"placeholder": "قیمت پست ...", "class": "form-control"}),
    )
