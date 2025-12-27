from django.db import models


class WeightLog(models.Model):
    weight = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        help_text="Body weight in kg",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.weight} kg @ {self.created_at:%Y-%m-%d %H:%M}"


class PillNote(models.Model):
    text = models.CharField(max_length=200, unique=True, help_text="Reusable pill note")

    class Meta:
        ordering = ["text"]

    def __str__(self):
        return self.text


class PillLog(models.Model):
    taken_at = models.DateTimeField(
        auto_now_add=True, help_text="When the pill was taken"
    )
    note = models.ForeignKey(
        PillNote,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="pill_logs",
    )

    class Meta:
        ordering = ["-taken_at"]

    def __str__(self):
        return f"Pill @ {self.taken_at:%Y-%m-%d %H:%M}"
