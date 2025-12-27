from django import forms
from .models import PillLog, PillNote


class PillLogForm(forms.ModelForm):
    note_text = forms.CharField(
        required=False,
        label="Note",
        help_text="Select existing or type a new note",
        widget=forms.TextInput(attrs={"list": "pill-note-list"}),
    )

    class Meta:
        model = PillLog
        fields = []

    def save(self, commit=True):
        note_text = self.cleaned_data.get("note_text", "").strip()
        note = None

        if note_text:
            note, _ = PillNote.objects.get_or_create(text=note_text)

        self.instance.note = note
        return super().save(commit)
