from django.db import models

# Create your models here.

class Node(models.Model):
    title = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Edge(models.Model):
    from_node = models.ForeignKey(Node, related_name="edges_from", on_delete=models.CASCADE)
    to_node = models.ForeignKey(Node, related_name="edges_to", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.from_node} → {self.to_node}"