from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bebida',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Cesta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.TextField()),
                ('total', models.FloatField()),
                ('litros', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Loja',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=60)),
                ('volume', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('preco_unidade', models.FloatField()),
                ('preco_litro', models.FloatField()),
                ('ultima_atualizacao', models.DateField()),
                ('bebida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Bebida')),
                ('loja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Loja')),
            ],
        ),
        migrations.AddField(
            model_name='cesta',
            name='produtos',
            field=models.ManyToManyField(to='api.Produto', verbose_name='produtos'),
        ),
        migrations.AddField(
            model_name='bebida',
            name='marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Marca'),
        ),
        migrations.AddField(
            model_name='bebida',
            name='modelo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Modelo'),
        ),
    ]
