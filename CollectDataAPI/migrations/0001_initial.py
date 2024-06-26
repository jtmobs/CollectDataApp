# Generated by Django 3.2.12 on 2024-04-03 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sessions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sequence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('support', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WebPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, max_length=1024, null=True)),
                ('eventType', models.CharField(blank=True, max_length=100, null=True)),
                ('pageStructure', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('timeStamp', models.FloatField(blank=True, null=True)),
                ('tag', models.CharField(max_length=50)),
                ('targetId', models.CharField(blank=True, max_length=1000, null=True)),
                ('classes', models.CharField(blank=True, max_length=1000, null=True)),
                ('xpath', models.TextField()),
                ('fullXpath', models.TextField()),
                ('cssPath', models.TextField()),
                ('sessionId', models.TextField()),
                ('textContent', models.TextField(blank=True, null=True)),
                ('mouseX', models.IntegerField(blank=True, null=True)),
                ('mouseY', models.IntegerField(blank=True, null=True)),
                ('key', models.CharField(blank=True, max_length=50, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sessions.session')),
            ],
        ),
        migrations.CreateModel(
            name='WebPageIdentifier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=1024)),
                ('pageStructure', models.TextField()),
                ('similarityMethod', models.CharField(choices=[('1', 'MS'), ('2', 'APTED'), ('3', 'MS_Optimized'), ('4', 'APTED_Optimized')], default='3', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='WebSite',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='WebPageIdentifierWebPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('similarity', models.DecimalField(decimal_places=2, max_digits=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('webPage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CollectDataAPI.webpage')),
                ('webPageIdentifier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CollectDataAPI.webpageidentifier')),
            ],
        ),
        migrations.AddField(
            model_name='webpageidentifier',
            name='webPages',
            field=models.ManyToManyField(through='CollectDataAPI.WebPageIdentifierWebPage', to='CollectDataAPI.WebPage'),
        ),
        migrations.AddField(
            model_name='webpage',
            name='webSite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CollectDataAPI.website'),
        ),
        migrations.CreateModel(
            name='SequenceIdentifier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('sequence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CollectDataAPI.sequence')),
                ('webPageIdentifier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CollectDataAPI.webpageidentifier')),
            ],
        ),
        migrations.AddField(
            model_name='sequence',
            name='webPageIdentifiers',
            field=models.ManyToManyField(through='CollectDataAPI.SequenceIdentifier', to='CollectDataAPI.WebPageIdentifier'),
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.URLField(unique=True)),
                ('webSite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CollectDataAPI.website')),
            ],
        ),
    ]
