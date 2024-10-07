from django.db import models

# Create your models here.

class Node(models.Model):
    title = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Edge(models.Model):
    EDGE_TYPE_CHOICES = (
        (1, 'next'),
        (2, 'required-prev')
    )

    from_node = models.ForeignKey(Node, related_name="edges_from", on_delete=models.CASCADE)
    to_node = models.ForeignKey(Node, related_name="edges_to", on_delete=models.CASCADE)
    edge_type = models.IntegerField(choices=EDGE_TYPE_CHOICES, default=1)
    
    def __str__(self):
        edge_type_in_str = dict(self.EDGE_TYPE_CHOICES).get(self.edge_type, "unknown")
        return f"{self.from_node} → {self.to_node} ({edge_type_in_str})"
    