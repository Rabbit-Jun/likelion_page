from django.db import models
from django.conf import settings
from accounts.models import User

class Quest(models.Model):
    qid = models.AutoField(primary_key=True, null=False, blank=False)
    quser = models.ForeignKey(User, on_delete=models.CASCADE)
    qtitle = models.CharField(max_length=50)
    quest_text = models.TextField()
    qimage = models.ImageField(null=True, blank=True)
    qcreated_at = models.DateTimeField(auto_now_add=True)
    qupdated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.qtitle

#댓글
class QComment(models.Model):
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE, related_name='qcomments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.comment_text
