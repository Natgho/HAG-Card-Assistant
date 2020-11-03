# Generated by Django 3.1.2 on 2020-11-03 13:23

from django.conf import settings
from django.contrib.auth.models import User
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models

from restApi.models import Article


def create_superuser(apps, schema_editor):
    superuser = User()
    superuser.is_active = True
    superuser.is_superuser = True
    superuser.is_staff = True
    superuser.username = 'admin'
    superuser.email = 'admin@admin.com'
    superuser.set_password('123')
    superuser.save()

    mock_article = Article()
    mock_article.title = "HUAWEI Mate40 Series Online Global Launch Event"
    mock_article.image1_url = "https://consumer-img.huawei.com/content/dam/huawei-cbg-site/common/mkt/" + \
                              "pdp/phones/mate40-pro-plus/images/security/unlock/n-plus.jpg"
    mock_article.image2_url = "https://consumer-img.huawei.com/content/dam/huawei-cbg-site/common/mkt/" + \
                              "pdp/phones/mate40-pro-plus/images/photo/portrait/intro/n.jpg"
    mock_article.video_link = "https://youtu.be/oH7H4wnjeYA"
    mock_article.content = ' <iframe width="900" height="506" src="https://www.youtube.com/embed/oH7H4wnjeYA" ' + \
                           'frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;' + \
                           'gyroscope; picture-in-picture" allowfullscreen></iframe>'
    mock_article.author = superuser
    mock_article.lang = "en"
    mock_article.save()

    mock_article = Article()
    mock_article.title = "HUAWEI Mate40 Serisi Çevrimiçi Küresel Lansman Etkinliği"
    mock_article.image1_url = "https://consumer-img.huawei.com/content/dam/huawei-cbg-site/common/mkt/" + \
                              "pdp/phones/mate40-pro-plus/images/security/unlock/n-plus.jpg"
    mock_article.image2_url = "https://consumer-img.huawei.com/content/dam/huawei-cbg-site/common/mkt/" + \
                              "pdp/phones/mate40-pro-plus/images/photo/portrait/intro/n.jpg"
    mock_article.video_link = "https://youtu.be/oH7H4wnjeYA"
    mock_article.content = ' <iframe width="900" height="506" src="https://www.youtube.com/embed/oH7H4wnjeYA" ' + \
                           'frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;' + \
                           'gyroscope; picture-in-picture" allowfullscreen></iframe>'
    mock_article.author = superuser
    mock_article.lang = "tr"
    mock_article.save()

    mock_article = Article()
    mock_article.title = "Evento de lanzamiento global en línea de la serie HUAWEI Mate40"
    mock_article.image1_url = "https://consumer-img.huawei.com/content/dam/huawei-cbg-site/common/mkt/" + \
                              "pdp/phones/mate40-pro-plus/images/security/unlock/n-plus.jpg"
    mock_article.image2_url = "https://consumer-img.huawei.com/content/dam/huawei-cbg-site/common/mkt/" + \
                              "pdp/phones/mate40-pro-plus/images/photo/portrait/intro/n.jpg"
    mock_article.video_link = "https://youtu.be/oH7H4wnjeYA"
    mock_article.content = ' <iframe width="900" height="506" src="https://www.youtube.com/embed/oH7H4wnjeYA" ' + \
                           'frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;' + \
                           'gyroscope; picture-in-picture" allowfullscreen></iframe>'
    mock_article.author = superuser
    mock_article.lang = "sp"
    mock_article.save()


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('article_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('image1_url', models.URLField(max_length=255)),
                ('image2_url', models.URLField(max_length=255)),
                ('video_link', models.URLField(max_length=255)),
                ('content', tinymce.models.HTMLField()),
                ('lang', models.CharField(max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'article',
            },
        ),
        migrations.RunPython(create_superuser)
    ]
