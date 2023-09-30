# Generated by Django 4.1 on 2023-09-30 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('actions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actions',
            name='target_ct',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='target_obj', to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='actions',
            name='target_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddIndex(
            model_name='actions',
            index=models.Index(fields=['target_ct', 'target_id'], name='actions_act_target__5ecc2e_idx'),
        ),
    ]