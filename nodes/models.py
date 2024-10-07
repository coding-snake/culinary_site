from django.db import models

# Create your models here.

class Node(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    tags = models.ManyToManyField('Tag', related_name='nodes')
    def __str__(self):
        return self.title
    
class Edge(models.Model):
    EDGE_TYPE_CHOICES = (
        (1, 'next'),
        (2, 'required-prev')
    )

    from_node = models.ForeignKey(Node, related_name="edge_from", on_delete=models.CASCADE)
    to_node = models.ForeignKey(Node, related_name="edge_to", on_delete=models.CASCADE)
    edge_type = models.IntegerField(choices=EDGE_TYPE_CHOICES, default=1)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['from_node', 'to_node', 'edge_type'], name='unique_edge')
        ]

    def __str__(self):
        edge_type_in_str = dict(self.EDGE_TYPE_CHOICES).get(self.edge_type, "unknown")
        return f"{self.from_node} → {self.to_node} ({edge_type_in_str})"
    
class Tag(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title

class FilesToNode(models.Model):
    node = models.ForeignKey(Node, related_name="file", on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name="file_tags")
    file_path = models.CharField(max_length=255)

    def __str__(self):
        tag_list = ", ".join([tag.title for tag in self.tags.all()])
        return f"File {self.node.title} with tags [{tag_list}] at {self.file_path}"