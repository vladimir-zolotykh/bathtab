from django.db import models
from django.utils import timezone


class PeeLog(models.Model):
    occurred_at = models.DateTimeField(default=timezone.now)
    volume_ml = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Volume in ml (optional)",
    )

    class Meta:
        ordering = ["-occurred_at"]

    def __str__(self):
        if self.volume_ml:
            return f"Pee {self.volume_ml} ml @ {self.occurred_at:%Y-%m-%d %H:%M}"
        return f"Pee @ {self.occurred_at:%Y-%m-%d %H:%M}"


class PooLog(models.Model):
    occurred_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-occurred_at"]

    def __str__(self):
        return f"Poo @ {self.occurred_at:%Y-%m-%d %H:%M}"


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
    taken_at = models.DateTimeField(default=timezone.now)
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
