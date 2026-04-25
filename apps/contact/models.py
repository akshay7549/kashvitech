from django.db import models
from django.utils import timezone


class ContactMessage(models.Model):

    # =========================
    # 📊 CHOICES
    # =========================
    STATUS_CHOICES = [
        ('new', 'New'),
        ('read', 'Read'),
        ('replied', 'Replied'),
    ]

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    # =========================
    # 👤 USER INFO
    # =========================
    name = models.CharField(max_length=100)
    email = models.EmailField(db_index=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    # =========================
    # 📩 MESSAGE INFO
    # =========================
    subject = models.CharField(max_length=150, blank=True, default='')
    message = models.TextField()

    # =========================
    # 📊 STATUS TRACKING
    # =========================
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='new',
        db_index=True
    )

    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='medium',
        db_index=True
    )

    is_important = models.BooleanField(default=False)

    # =========================
    # 🌐 REQUEST INFO
    # =========================
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.TextField(blank=True)

    # =========================
    # ⏱️ TIMESTAMPS
    # =========================
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    replied_at = models.DateTimeField(blank=True, null=True)

    # =========================
    # 🔁 METHODS
    # =========================
    def __str__(self):
        return f"{self.name} - {self.subject or 'No Subject'}"

    def mark_as_read(self):
        if self.status == 'new':
            self.status = 'read'
            self.save(update_fields=['status'])

    def mark_as_replied(self):
        if self.status != 'replied':
            self.status = 'replied'
            self.replied_at = timezone.now()
            self.save(update_fields=['status', 'replied_at'])

    # Auto-set replied_at when status changes
    def save(self, *args, **kwargs):
        if self.status == 'replied' and not self.replied_at:
            self.replied_at = timezone.now()
        super().save(*args, **kwargs)

    # =========================
    # ⚙️ META
    # =========================
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['created_at']),
            models.Index(fields=['email']),
        ]