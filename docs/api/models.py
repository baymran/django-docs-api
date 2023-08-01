from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class DocumentType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Document(models.Model):
    type = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    series = models.CharField(max_length=10)
    number = models.CharField(max_length=10)
    date_of_issue = models.DateField()
    department_code = models.CharField(max_length=10)
    main = models.BooleanField()
    archival = models.BooleanField()

    def __str__(self):
        return f"{self.type} - {self.organization}"
