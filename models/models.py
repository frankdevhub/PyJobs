# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BlogDocumentBrief(models.Model):
    id = models.BigAutoField(primary_key=True)
    blog_domain = models.CharField(max_length=255, blank=True, null=True)
    doc_title = models.CharField(max_length=100, blank=True, null=True)
    doc_brief = models.CharField(max_length=255, blank=True, null=True)
    publish_date = models.CharField(max_length=50, blank=True, null=True)
    context = models.TextField(blank=True, null=True)
    html = models.TextField(blank=True, null=True)
    old_data = models.TextField(blank=True, null=True)
    renew_data = models.TextField(blank=True, null=True)
    compare_data = models.TextField(blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    ext1 = models.CharField(max_length=255, blank=True, null=True)
    ext2 = models.CharField(max_length=255, blank=True, null=True)
    ext3 = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '51cto_blog_docs_brief'
