from django.db import models

# Create your models here.

class Node(models.Model):
    title = models.CharField(max_length=255, unique=True)
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

class TagSet(models.Model):
    title = models.CharField(max_length=255, unique=True)
    given_tag = models.ForeignKey(Tag, related_name="set_tag", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} : {self.given_tag.title}"
    
class FilesToTagSet(models.Model):
    set_title = models.OneToOneField(TagSet, related_name="files_set_title", on_delete=models.CASCADE, unique=True)
    file_path = models.CharField(max_length=255)

    def __str__(self):
        return f"File {self.set_title} at {self.file_path}"
    