from django import forms
from .models import PillLog, PillNote, PeeLog, PooLog


class PeeLogForm(forms.ModelForm):
    class Meta:
        model = PeeLog
        fields = ["occurred_at", "volume_ml"]
        widgets = {
            "occurred_at": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }


class PooLogForm(forms.ModelForm):
    class Meta:
        model = PooLog
        fields = ["occurred_at"]
        widgets = {
            "occurred_at": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }


class PillLogForm(forms.ModelForm):
    class Meta:
        model = PillLog
        fields = ["taken_at", "note_text"]
        widgets = {
            "taken_at": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }

    note_text = forms.CharField(
        required=False,
        label="Note",
        help_text="Select existing or type a new note",
        widget=forms.TextInput(attrs={"list": "pill-note-list"}),
    )

    def save(self, commit=True):
        note_text = self.cleaned_data.get("note_text", "").strip()
        note = None

        if note_text:
            note, _ = PillNote.objects.get_or_create(text=note_text)

        self.instance.note = note
        return super().save(commit)
