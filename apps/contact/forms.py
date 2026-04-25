from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number',
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subject',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your Message...',
                'rows': 5,
            }),
        }

    # ✅ Better Labels + Required Handling
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].label = "Full Name"
        self.fields['email'].label = "Email Address"
        self.fields['phone'].label = "Phone Number"
        self.fields['subject'].label = "Subject"
        self.fields['message'].label = "Message"

        # Set required fields properly (backend validation, not just HTML)
        self.fields['name'].required = True
        self.fields['email'].required = True
        self.fields['message'].required = True

    # ✅ Name Validation
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name:
            name = name.strip()
            if len(name) < 3:
                raise forms.ValidationError("Name must be at least 3 characters")
        return name

    # ✅ Phone Validation (Improved)
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone:
            phone = phone.strip()

            if not phone.isdigit():
                raise forms.ValidationError("Only digits allowed")

            if len(phone) != 10:
                raise forms.ValidationError("Phone must be exactly 10 digits")

        return phone

    # ✅ Subject Validation
    def clean_subject(self):
        subject = self.cleaned_data.get('subject')
        if subject:
            subject = subject.strip()
            if len(subject) < 5:
                raise forms.ValidationError("Subject must be at least 5 characters")
        return subject

    # ✅ Message Validation
    def clean_message(self):
        message = self.cleaned_data.get('message')
        if message:
            message = message.strip()
            if len(message) < 10:
                raise forms.ValidationError("Message must be at least 10 characters")
        return message

    # 🔥 Global Clean (Optional Advanced Validation)
    def clean(self):
        cleaned_data = super().clean()

        email = cleaned_data.get('email')
        message = cleaned_data.get('message')

        if email and message:
            if email in message:
                self.add_error('message', "Message should not contain your email")

        return cleaned_data