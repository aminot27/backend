# Generated by Django 3.2.4 on 2022-01-31 15:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lov',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='Modified')),
                ('status', models.CharField(choices=[('CREATED', 'CREATED'), ('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE'), ('DELETED', 'DELETED')], default='CREATED', help_text='Current register status', max_length=15, verbose_name='Status')),
                ('lov_id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=10)),
                ('type_description', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=20)),
                ('code_description', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'LOV',
                'verbose_name_plural': 'LOVs',
                'db_table': 'master_lov',
                'ordering': ['lov_id'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='Modified')),
                ('status', models.CharField(choices=[('CREATED', 'CREATED'), ('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE'), ('DELETED', 'DELETED')], default='CREATED', help_text='Current register status', max_length=15, verbose_name='Status')),
                ('profile_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('domain', models.CharField(max_length=20)),
                ('type', models.CharField(blank=True, max_length=15, null=True)),
                ('icon', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
                'db_table': 'master_profile',
                'ordering': ['profile_id'],
            },
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='Modified')),
                ('status', models.CharField(choices=[('CREATED', 'CREATED'), ('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE'), ('DELETED', 'DELETED')], default='CREATED', help_text='Current register status', max_length=15, verbose_name='Status')),
                ('system_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('icon', models.CharField(blank=True, max_length=30, null=True)),
                ('color', models.CharField(blank=True, max_length=10, null=True)),
                ('version', models.CharField(blank=True, max_length=5, null=True)),
                ('order', models.IntegerField()),
                ('url', models.CharField(blank=True, max_length=80, null=True)),
            ],
            options={
                'verbose_name': 'System',
                'verbose_name_plural': 'Systems',
                'db_table': 'master_system',
                'ordering': ['system_id'],
            },
        ),
        migrations.CreateModel(
            name='SystemUser',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='Modified')),
                ('status', models.CharField(choices=[('CREATED', 'CREATED'), ('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE'), ('DELETED', 'DELETED')], default='CREATED', help_text='Current register status', max_length=15, verbose_name='Status')),
                ('system_user_id', models.AutoField(primary_key=True, serialize=False, verbose_name='System User Id')),
                ('document_type', models.CharField(blank=True, default='DNI', max_length=10, null=True)),
                ('document', models.CharField(blank=True, max_length=8, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('phone', models.CharField(blank=True, max_length=9, null=True)),
                ('entity', models.CharField(blank=True, max_length=200, null=True)),
                ('avatar', models.CharField(blank=True, max_length=200, null=True)),
                ('auth_user', models.OneToOneField(db_column='auth_user_id', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'System User',
                'verbose_name_plural': 'System Users',
                'db_table': 'master_system_user',
                'ordering': ['system_user_id'],
            },
        ),
        migrations.CreateModel(
            name='SystemUserProfile',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='Modified')),
                ('status', models.CharField(choices=[('CREATED', 'CREATED'), ('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE'), ('DELETED', 'DELETED')], default='CREATED', help_text='Current register status', max_length=15, verbose_name='Status')),
                ('system_user_profile_id', models.AutoField(primary_key=True, serialize=False)),
                ('profile', models.ForeignKey(db_column='profile_id', on_delete=django.db.models.deletion.DO_NOTHING, to='master.profile')),
                ('system_user', models.ForeignKey(db_column='system_user_id', on_delete=django.db.models.deletion.DO_NOTHING, to='master.systemuser')),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'User Profiles',
                'db_table': 'master_system_user_profile',
                'ordering': ['system_user_profile_id'],
            },
        ),
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='Modified')),
                ('status', models.CharField(choices=[('CREATED', 'CREATED'), ('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE'), ('DELETED', 'DELETED')], default='CREATED', help_text='Current register status', max_length=15, verbose_name='Status')),
                ('movement_id', models.AutoField(primary_key=True, serialize=False)),
                ('movement_type', models.CharField(blank=True, max_length=10, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('ip', models.CharField(blank=True, max_length=30, null=True)),
                ('table', models.CharField(blank=True, max_length=30, null=True)),
                ('system_user', models.ForeignKey(db_column='system_user_id', on_delete=django.db.models.deletion.DO_NOTHING, to='master.systemuser')),
            ],
            options={
                'verbose_name': 'Movement',
                'verbose_name_plural': 'Movements',
                'db_table': 'master_movement',
                'ordering': ['movement_id'],
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='Modified')),
                ('status', models.CharField(choices=[('CREATED', 'CREATED'), ('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE'), ('DELETED', 'DELETED')], default='CREATED', help_text='Current register status', max_length=15, verbose_name='Status')),
                ('module_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('version', models.CharField(blank=True, max_length=10, null=True)),
                ('url', models.CharField(blank=True, max_length=100, null=True)),
                ('order', models.IntegerField()),
                ('icon', models.CharField(blank=True, max_length=30, null=True)),
                ('system', models.ForeignKey(db_column='system_id', on_delete=django.db.models.deletion.DO_NOTHING, to='master.system')),
            ],
            options={
                'verbose_name': 'Module',
                'verbose_name_plural': 'Modules',
                'db_table': 'master_module',
                'ordering': ['module_id'],
            },
        ),
        migrations.CreateModel(
            name='Access',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='Modified')),
                ('status', models.CharField(choices=[('CREATED', 'CREATED'), ('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE'), ('DELETED', 'DELETED')], default='CREATED', help_text='Current register status', max_length=15, verbose_name='Status')),
                ('access_id', models.AutoField(primary_key=True, serialize=False)),
                ('module', models.ForeignKey(db_column='module_id', on_delete=django.db.models.deletion.DO_NOTHING, to='master.module')),
                ('profile', models.ForeignKey(db_column='profile_id', on_delete=django.db.models.deletion.DO_NOTHING, to='master.profile')),
            ],
            options={
                'verbose_name': 'Access',
                'verbose_name_plural': 'Access',
                'db_table': 'master_access',
                'ordering': ['access_id'],
            },
        ),
    ]
