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
