from django.db import models

class PetalMessage(models.Model):
    # This stores the "For Whom" name from your form
    recipient = models.CharField(max_length=100)
    
    # This stores the long message or song link
    message = models.TextField()
    
    # This automatically records exactly when the message was sent
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"To: {self.recipient} - {self.message[:20]}..."