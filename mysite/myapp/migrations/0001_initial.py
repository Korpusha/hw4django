# Generated by Django 3.2.9 on 2021-11-23 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_author', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('do_you_like_it', models.BooleanField(verbose_name='Do you like it?')),
                ('article_name', models.CharField(max_length=120)),
                ('article_body', models.TextField(default=0)),
                ('date_of_publicity', models.DateField(null=True)),
            ],
            options={
                'ordering': ['article_name'],
            },
        ),
        migrations.CreateModel(
            name='BlogUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_user_name', models.CharField(max_length=120)),
                ('email', models.EmailField(default=0, max_length=254)),
                ('password', models.CharField(default=0, max_length=120)),
            ],
            options={
                'ordering': ['-blog_user_name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_book', models.CharField(max_length=120)),
                ('year_of_public', models.DateField(null=True)),
                ('available', models.BooleanField()),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='myapp.author')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_user', models.CharField(max_length=120)),
                ('books_available', models.ForeignKey(limit_choices_to={'available': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='available_books', to='myapp.book')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('do_you_like_it', models.BooleanField(verbose_name='Do you like it?')),
                ('comment', models.TextField()),
                ('blog_blog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='myapp.blog')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to='myapp.bloguser'),
        ),
    ]