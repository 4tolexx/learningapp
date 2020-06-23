# Generated by Django 2.2 on 2020-06-23 13:47

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
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('html', models.TextField(verbose_name='Question Text')),
                ('is_published', models.BooleanField(default=False, verbose_name='Has been published?')),
                ('maximum_marks', models.DecimalField(decimal_places=2, default=4, max_digits=6, verbose_name='Maximum Marks')),
            ],
        ),
        migrations.CreateModel(
            name='QuizProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_score', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Total Score')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_correct', models.BooleanField(default=False, verbose_name='Is this answer correct?')),
                ('html', models.TextField(verbose_name='Choice Text')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='quiz.Question')),
            ],
        ),
        migrations.CreateModel(
            name='AttemptedQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_correct', models.BooleanField(default=False, verbose_name='Was this attempt correct?')),
                ('marks_obtained', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Marks Obtained')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Question')),
                ('quiz_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attempts', to='quiz.QuizProfile')),
                ('selected_choice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.Choice')),
            ],
        ),
    ]
