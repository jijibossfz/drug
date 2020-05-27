# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2020-05-22 13:48
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import works.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.ASCIIUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(blank=True, max_length=10, null=True, verbose_name='username')),
                ('mobile', models.CharField(max_length=11, verbose_name='\u7535\u8bdd')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='email')),
                ('work_org', models.CharField(default='', max_length=20, verbose_name='work_org')),
                ('research_dir', models.CharField(default='', max_length=20, verbose_name='research_dir')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add_time')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '\u7528\u6237',
                'verbose_name_plural': '\u7528\u6237',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Admet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_name', models.CharField(max_length=20, verbose_name='\u4efb\u52a1\u540d\u79f0')),
                ('work_decs', models.CharField(default='', max_length=100, verbose_name='\u4efb\u52a1\u63cf\u8ff0')),
                ('mol_file', models.FileField(upload_to=works.models.upload_to, verbose_name='\u5c0f\u5206\u5b50\u6587\u4ef6')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237')),
            ],
            options={
                'verbose_name': 'ADMET\u9884\u6d4b',
                'verbose_name_plural': 'ADMET\u9884\u6d4b',
            },
        ),
        migrations.CreateModel(
            name='AutoDock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_name', models.CharField(max_length=20, unique=True, verbose_name='work_name')),
                ('work_decs', models.CharField(default='', max_length=100, verbose_name='work_decs')),
                ('size_x', models.FloatField(verbose_name='size_x')),
                ('size_y', models.FloatField(verbose_name='size_y')),
                ('size_z', models.FloatField(verbose_name='size_z')),
                ('center_x', models.FloatField(verbose_name='center_x')),
                ('center_y', models.FloatField(verbose_name='center_y')),
                ('center_z', models.FloatField(verbose_name='center_z')),
                ('pdb_file', models.FileField(upload_to=works.models.dock_upload_to, verbose_name='pdb_file')),
                ('lig_file', models.FileField(upload_to=works.models.dock_upload_to, verbose_name='lig_file')),
                ('price', models.IntegerField(default=10000, verbose_name='price')),
                ('status', models.CharField(default='waiting', max_length=10, verbose_name='status')),
                ('out_path', models.FileField(null=True, upload_to=b'', verbose_name='out_path')),
                ('affinity', models.CharField(default='the position is unreasonable', max_length=100, verbose_name='affinity')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add_time')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': '\u5206\u5b50\u5bf9\u63a5',
                'verbose_name_plural': '\u5206\u5b50\u5bf9\u63a5',
            },
        ),
        migrations.CreateModel(
            name='AutoDock2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_name', models.CharField(max_length=20, unique=True, verbose_name='work_name')),
                ('work_decs', models.CharField(default='', max_length=100, verbose_name='work_decs')),
                ('pdb_file', models.FileField(upload_to=works.models.dock2_upload_to, verbose_name='pdb_file')),
                ('lig_file', models.FileField(upload_to=works.models.dock2_upload_to, verbose_name='lig_file')),
                ('resi_file', models.FileField(upload_to=works.models.dock2_upload_to, verbose_name='resi_file')),
                ('price', models.IntegerField(default=10000, verbose_name='price')),
                ('status', models.CharField(default='waiting', max_length=10, verbose_name='status')),
                ('out_path', models.FileField(null=True, upload_to=b'', verbose_name='out_path')),
                ('affinity', models.CharField(default='the position is unreasonable', max_length=100, verbose_name='affinity')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add_time')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': '\u5206\u5b50\u5bf9\u63a52',
                'verbose_name_plural': '\u5206\u5b50\u5bf9\u63a52',
            },
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='banner/', verbose_name='\u8f6e\u64ad\u56fe\u7247')),
                ('index', models.IntegerField(verbose_name='\u8f6e\u64ad\u987a\u5e8f')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u9996\u9875\u8f6e\u64ad\u56fe',
                'verbose_name_plural': '\u9996\u9875\u8f6e\u64ad\u56fe',
            },
        ),
        migrations.CreateModel(
            name='Dock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_name', models.CharField(max_length=20, unique=True, verbose_name='work_name')),
                ('algorithm', models.CharField(choices=[('AutoDock', 'AutoDock'), ('AutoDock-vina', 'AutoDock-vina'), ('Glide', 'Glide')], max_length=20)),
                ('size_x', models.FloatField(null=True, verbose_name='size_x')),
                ('size_y', models.FloatField(null=True, verbose_name='size_y')),
                ('size_z', models.FloatField(null=True, verbose_name='size_z')),
                ('center_x', models.FloatField(null=True, verbose_name='center_x')),
                ('center_y', models.FloatField(null=True, verbose_name='center_y')),
                ('center_z', models.FloatField(null=True, verbose_name='center_z')),
                ('resn', models.CharField(max_length=100, null=True, verbose_name='resn')),
                ('pdb_file', models.FileField(upload_to=works.models.dock_upload_to, verbose_name='pdb_file')),
                ('lig_file', models.FileField(upload_to=works.models.dock_upload_to, verbose_name='lig_file')),
                ('reference_file', models.FileField(null=True, upload_to=works.models.dock_upload_to, verbose_name='reference_file')),
                ('status', models.CharField(default='waiting', max_length=10, verbose_name='status')),
                ('out_path', models.FileField(null=True, upload_to=b'', verbose_name='out_path')),
                ('affinity', models.CharField(default='the position is unreasonable', max_length=100, verbose_name='affinity')),
                ('email', models.CharField(max_length=100, verbose_name='email')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add_time')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': '\u5206\u5b50\u5bf9\u63a5',
                'verbose_name_plural': '\u5206\u5b50\u5bf9\u63a5',
            },
        ),
        migrations.CreateModel(
            name='Dynamic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_name', models.CharField(max_length=20, verbose_name='\u4efb\u52a1\u540d\u79f0')),
                ('work_decs', models.CharField(default='', max_length=100, verbose_name='\u4efb\u52a1\u63cf\u8ff0')),
                ('conf_info', models.CharField(choices=[(1, '\u901a\u7528\u8ba1\u7b97'), (2, '\u8ba1\u7b97\u7ed3\u5408\u80fd'), (3, '\u8ba1\u7b97\u6c22\u952e'), (4, '\u805a\u7c7b\u5206\u6790')], max_length=20, verbose_name='\u914d\u7f6e\u4fe1\u606f')),
                ('protein_file', models.FileField(upload_to=works.models.upload_to, verbose_name='\u86cb\u767d\u6587\u4ef6')),
                ('mol_file', models.FileField(upload_to=works.models.upload_to, verbose_name='\u5c0f\u5206\u5b50\u6587\u4ef6')),
                ('conf_project', models.CharField(choices=[(1, '\u6709\u6c34'), (2, '\u65e0\u6c34'), (3, '\u81ea\u8ba1\u7b97')], max_length=100, verbose_name='\u914d\u7f6e\u9879\u76ee')),
                ('s_file', models.FileField(default='', upload_to=works.models.upload_to, verbose_name='S\u4fe1\u606f\u6587\u4ef6')),
                ('lig_file', models.FileField(default='', upload_to=works.models.upload_to, verbose_name='lig\u6587\u4ef6')),
                ('frcmod_file', models.FileField(default='', upload_to=works.models.upload_to, verbose_name='frcmod\u6587\u4ef6')),
                ('res_num', models.IntegerField(default=0, verbose_name='\u6c28\u57fa\u9178\u6570\u76ee')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237')),
            ],
            options={
                'verbose_name': '\u52a8\u529b\u5b66\u6a21\u62df',
                'verbose_name_plural': '\u52a8\u529b\u5b66\u6a21\u62df',
            },
        ),
        migrations.CreateModel(
            name='Gbsa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_name', models.CharField(max_length=100, verbose_name='work_name')),
                ('pdb_file', models.FileField(upload_to=works.models.gbsa_upload_to, verbose_name='pdb_file')),
                ('lig_file', models.FileField(upload_to=works.models.gbsa_upload_to, verbose_name='lig_file')),
                ('complex_file', models.FileField(upload_to=works.models.gbsa_upload_to, verbose_name='complex_file')),
                ('status', models.CharField(default='waiting', max_length=20, verbose_name='status')),
                ('email', models.CharField(max_length=100, verbose_name='email')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add_time')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'gbsa',
                'verbose_name_plural': 'gbsa',
            },
        ),
        migrations.CreateModel(
            name='Passwordreset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, verbose_name='email')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add_time')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='\u670d\u52a1\u540d\u79f0')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u5185\u5bb9',
                'verbose_name_plural': '\u670d\u52a1\u5185\u5bb9',
            },
        ),
        migrations.CreateModel(
            name='ReverseVirtualScreen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_name', models.CharField(max_length=20, verbose_name='\u4efb\u52a1\u540d\u79f0')),
                ('work_decs', models.CharField(default='', max_length=100, verbose_name='\u4efb\u52a1\u63cf\u8ff0')),
                ('target_db', models.CharField(choices=[(1, 'zine'), (2, 'chembl')], max_length=10, verbose_name='\u9776\u70b9\u6570\u636e\u5e93')),
                ('mol_file', models.FileField(upload_to=works.models.upload_to, verbose_name='\u9776\u70b9\u6587\u4ef6')),
                ('top_n', models.IntegerField(verbose_name='\u8fd4\u56de\u7ed3\u679c\u6570\u76ee')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237')),
            ],
            options={
                'verbose_name': '\u53cd\u5411\u865a\u62df\u7b5b\u9009',
                'verbose_name_plural': '\u53cd\u5411\u865a\u62df\u7b5b\u9009',
            },
        ),
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_name', models.CharField(max_length=100, verbose_name='work_name')),
                ('screen_cat', models.CharField(max_length=10, verbose_name='\u7b5b\u9009\u7c7b\u522b')),
                ('affinity', models.FloatField(verbose_name='affinity')),
                ('path', models.FileField(upload_to=b'', verbose_name='out_file')),
            ],
            options={
                'verbose_name': '\u865a\u62df\u7b5b\u9009\u7ed3\u679c',
                'verbose_name_plural': '\u865a\u62df\u7b5b\u9009\u7ed3\u679c',
            },
        ),
        migrations.CreateModel(
            name='SeaTarget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_name', models.CharField(max_length=100, verbose_name='work_name')),
                ('smiles', models.CharField(max_length=200, verbose_name='smiles')),
                ('target', models.CharField(default='null', max_length=500, verbose_name='targets')),
            ],
            options={
                'verbose_name': 'SEA\u9884\u6d4b\u7ed3\u679c',
                'verbose_name_plural': 'SEA\u9884\u6d4b\u7ed3\u679c',
            },
        ),
        migrations.CreateModel(
            name='SeaVirScreen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_name', models.CharField(max_length=100, verbose_name='work_name')),
                ('affinity', models.FloatField(verbose_name='affinity')),
                ('path', models.FileField(upload_to=b'', verbose_name='out_file')),
            ],
            options={
                'verbose_name': '\u865a\u62df\u7b5b\u9009\u7ed3\u679c',
                'verbose_name_plural': '\u865a\u62df\u7b5b\u9009\u7ed3\u679c',
            },
        ),
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.CharField(max_length=20, verbose_name='\u9776\u70b9\u540d\u79f0')),
            ],
            options={
                'verbose_name': '\u9776\u70b9\u540d\u79f0',
                'verbose_name_plural': '\u9776\u70b9\u540d\u79f0',
            },
        ),
        migrations.CreateModel(
            name='VerifyCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=6, verbose_name='code')),
                ('email', models.CharField(max_length=100, verbose_name='email')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add_time')),
            ],
            options={
                'verbose_name': '\u9a8c\u8bc1\u7801',
                'verbose_name_plural': '\u9a8c\u8bc1\u7801',
            },
        ),
        migrations.CreateModel(
            name='VirScreen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_name', models.CharField(max_length=20, unique=True, verbose_name='work_name')),
                ('mol_db', models.CharField(choices=[('zinc', 'zinc'), ('chembl', 'chembl'), ('drugbank', 'drugbank'), ('chinese-medicine', 'chinese-medicine'), ('taosu', 'taosu'), ('bailingwei', 'bailingwei'), ('jianqiao', 'jianqiao')], max_length=20, null=True, verbose_name='mol_db')),
                ('target', models.CharField(max_length=100, null=True, verbose_name='target')),
                ('smiles', models.CharField(max_length=200, null=True, verbose_name='smiles')),
                ('pdb_file', models.FileField(null=True, upload_to=works.models.screen_upload_to, verbose_name='pdb_file')),
                ('resn', models.CharField(max_length=100, null=True, verbose_name='resn')),
                ('status', models.CharField(default='waiting', max_length=10, verbose_name='status')),
                ('email', models.CharField(default='', max_length=100, verbose_name='email')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add_time')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': '\u865a\u62df\u7b5b\u9009',
                'verbose_name_plural': '\u865a\u62df\u7b5b\u9009',
            },
        ),
        migrations.CreateModel(
            name='VirtualScreen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_name', models.CharField(max_length=20, unique=True, verbose_name='work_name')),
                ('work_decs', models.CharField(default='', max_length=100, verbose_name='work_decs')),
                ('size_x', models.FloatField(verbose_name='size_x')),
                ('size_y', models.FloatField(verbose_name='size_y')),
                ('size_z', models.FloatField(verbose_name='size_z')),
                ('center_x', models.FloatField(verbose_name='center_x')),
                ('center_y', models.FloatField(verbose_name='center_y')),
                ('center_z', models.FloatField(verbose_name='center_z')),
                ('target', models.CharField(default='', max_length=100000, verbose_name='target')),
                ('pdb_file', models.FileField(upload_to=works.models.screen_upload_to, verbose_name='pdb_file')),
                ('user_db', models.FileField(null=True, upload_to=works.models.screen_upload_to, verbose_name='user_db')),
                ('price', models.IntegerField(default=10000, verbose_name='price')),
                ('status', models.CharField(default='waiting', max_length=10, verbose_name='status')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add_time')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': '\u865a\u62df\u7b5b\u9009',
                'verbose_name_plural': '\u865a\u62df\u7b5b\u9009',
            },
        ),
        migrations.CreateModel(
            name='VirtualScreen2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_name', models.CharField(max_length=20, unique=True, verbose_name='work_name')),
                ('work_decs', models.CharField(default='', max_length=100, verbose_name='work_decs')),
                ('target', models.CharField(default='', max_length=100000, verbose_name='target')),
                ('pdb_file', models.FileField(upload_to=works.models.screen2_upload_to, verbose_name='pdb_file')),
                ('resi_file', models.FileField(upload_to=works.models.screen2_upload_to, verbose_name='resi_file')),
                ('user_db', models.FileField(null=True, upload_to=works.models.screen2_upload_to, verbose_name='user_db')),
                ('price', models.IntegerField(default=10000, verbose_name='price')),
                ('status', models.CharField(default='waiting', max_length=10, verbose_name='status')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add_time')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': '\u865a\u62df\u7b5b\u90092',
                'verbose_name_plural': '\u865a\u62df\u7b5b\u90092',
            },
        ),
        migrations.CreateModel(
            name='VsBlast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_name', models.CharField(max_length=20, verbose_name='\u4efb\u52a1\u540d\u79f0')),
                ('work_decs', models.CharField(default='', max_length=100, verbose_name='\u4efb\u52a1\u63cf\u8ff0')),
                ('sequence', models.CharField(max_length=1000, verbose_name='\u86cb\u767d\u5e8f\u5217')),
                ('protein_db', models.CharField(choices=[(1, 'zinc'), (2, 'chembl')], max_length=10)),
                ('e_value', models.CharField(choices=[(1, 1e-05), (2, 0.0001), (3, 0.001), (4, 0.01), (5, 0.01), (6, 1), (7, 10)], max_length=10, verbose_name='E\u503c\u9009\u62e9')),
                ('out_format', models.CharField(choices=[(1, 'pariwise'), (2, 'XML blast output'), (3, 'tabular')], max_length=10, verbose_name='\u8f93\u51fa\u683c\u5f0f\u9009\u62e9')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237')),
            ],
            options={
                'verbose_name': 'VsleadBlast',
                'verbose_name_plural': 'VsleadBlast',
            },
        ),
    ]
