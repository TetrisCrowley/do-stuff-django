# Generated by Django 2.1 on 2018-09-24 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dostuff', '0015_merge_20180924_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='auth_key',
            field=models.CharField(default='33f063c4b614', max_length=16),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='key',
            field=models.TextField(default='70a21ac9a66eb2742146b99eb52fce44b02c80b3b86c8333d46710fc8c895bbcb4ae336d2bec4d0edbc4cdddfdf28df363048672f07510'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_login',
            field=models.IntegerField(default=1537820767.4778209),
        ),
    ]