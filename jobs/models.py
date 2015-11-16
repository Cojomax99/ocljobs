from django.db import models


class JobsQuery(models.Model):
    description = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    full_time = models.BooleanField(default=False)

    def __str__(self):
        return "Query " + str(self.id)


class JobsEntry(models.Model):
    query = models.ForeignKey(to=JobsQuery)
    title = models.CharField(max_length=150)
    company = models.CharField(max_length=100)
    company_url = models.URLField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    how_to_apply = models.CharField(max_length=2000)
    created_at = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    internal_id = models.CharField(max_length=64)
    company_logo = models.URLField(blank=True, null=True)
    description = models.CharField(max_length=5000)
    type = models.CharField(max_length=20)

    def __str__(self):
        return "Entry for " + str(self.query.id)


def get_model_from_entry(query, entry):
    temp = JobsEntry()
    temp.query = query
    temp.title = entry.title
    temp.company = entry.company
    temp.company_url = entry.company_url
    temp.url = entry.url
    temp.how_to_apply = entry.how_to_apply
    temp.created_at = entry.created_at
    temp.location = entry.location
    temp.internal_id = entry.id
    temp.company_logo = entry.company_logo
    temp.description = entry.description
    temp.type = entry.type

    return temp
