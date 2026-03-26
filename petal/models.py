from django.db import models

class PetalMessage(models.Model):
    # This saves the "For Whom" name
    recipient = models.CharField(max_length=100)
    
    # This saves the personal message or song link
    message = models.TextField()
    
    # This automatically records when the message was sent
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message for {self.recipient}"