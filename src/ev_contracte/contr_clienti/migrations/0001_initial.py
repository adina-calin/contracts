# Generated by Django 3.0.7 on 2020-07-07 10:35

import contr_clienti.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localitate', models.CharField(max_length=255)),
                ('strada', models.CharField(max_length=255)),
                ('numar', models.CharField(max_length=255)),
                ('judet', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Adrese',
            },
        ),
        migrations.CreateModel(
            name='AplicatiiInfo98',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aplicatie', models.CharField(max_length=255)),
                ('contravaloare_aplicatie', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('contravaloare_aplicatie_fara_tva', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('moneda_vanzare', models.IntegerField(choices=[(1, 'RON'), (2, 'EUR'), (3, 'USD')])),
                ('abonament_aplicatie_fara_tva', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('moneda_abonament', models.IntegerField(choices=[(1, 'RON'), (2, 'EUR'), (3, 'USD')])),
                ('observatii', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': "Aplicații INFO'98",
            },
        ),
        migrations.CreateModel(
            name='CategorieContract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorie_contract', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Categorii de contracte',
            },
        ),
        migrations.CreateModel(
            name='Clienti',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('societate', models.CharField(max_length=255)),
                ('cod_fiscal', models.IntegerField()),
                ('platitor_tva', models.BooleanField(default=None)),
                ('nr_registrul_comertului', models.CharField(max_length=255)),
                ('iban', models.CharField(max_length=255)),
                ('banca_cont', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Clienti',
            },
        ),
        migrations.CreateModel(
            name='PersoanaContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('telefon', models.IntegerField()),
                ('functie', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Persoane de contact',
            },
        ),
        migrations.CreateModel(
            name='Produse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produs', models.CharField(max_length=255)),
                ('serial_number', models.CharField(blank=True, max_length=255)),
                ('furnizor', models.CharField(max_length=255)),
                ('pret_furnizor_fara_tva', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('moneda_furnizor', models.IntegerField(choices=[(1, 'RON'), (2, 'EUR'), (3, 'USD')])),
                ('pret_vanzare_fara_tva', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('moneda_vanzare', models.IntegerField(choices=[(1, 'RON'), (2, 'EUR'), (3, 'USD')])),
                ('observatii', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Produse',
            },
        ),
        migrations.CreateModel(
            name='Reprezentant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('telefon', models.IntegerField()),
                ('functie', models.IntegerField(choices=[(1, 'Administrator'), (2, 'Director'), (3, 'Director General'), (4, 'Director Adjunct'), (5, 'Contabil Șef'), (6, 'Director Economic')])),
            ],
            options={
                'verbose_name_plural': 'Reprezentanti',
            },
        ),
        migrations.CreateModel(
            name='ServiciiInformatice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviciu', models.CharField(max_length=255)),
                ('contravaloare_serviciu_fara_tva', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('moneda_vanzare', models.IntegerField(choices=[(1, 'RON'), (2, 'EUR'), (3, 'USD')])),
                ('observatii', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Servicii',
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nr_registru', models.IntegerField(default=contr_clienti.models.increment_nr_reg, unique=True)),
                ('nr_contract', models.IntegerField(default=contr_clienti.models.increment_nr_contr)),
                ('data_contract', models.DateField(blank=True, null=True)),
                ('data_incepere_contract', models.DateField(blank=True, null=True)),
                ('data_sfarsit_contract', models.DateField(blank=True, null=True)),
                ('observatii', models.TextField(blank=True, max_length=255)),
                ('aplicatii', models.ManyToManyField(blank=True, to='contr_clienti.AplicatiiInfo98')),
                ('beneficiar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contr_clienti.Clienti')),
                ('produse', models.ManyToManyField(blank=True, to='contr_clienti.Produse')),
                ('servicii', models.ManyToManyField(blank=True, to='contr_clienti.ServiciiInformatice')),
                ('tip_contract', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contr_clienti.CategorieContract', verbose_name='Categorie contract')),
            ],
            options={
                'verbose_name_plural': 'Contracte',
                'unique_together': {('nr_contract', 'data_contract')},
            },
        ),
        migrations.AddField(
            model_name='clienti',
            name='persoana_contact',
            field=models.ManyToManyField(to='contr_clienti.PersoanaContact'),
        ),
        migrations.AddField(
            model_name='clienti',
            name='punct_de_lucru',
            field=models.ManyToManyField(to='contr_clienti.Adresa'),
        ),
        migrations.AddField(
            model_name='clienti',
            name='reprezentant',
            field=models.ManyToManyField(to='contr_clienti.Reprezentant'),
        ),
        migrations.AddField(
            model_name='clienti',
            name='sediul_social',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sediu', to='contr_clienti.Adresa'),
        ),
        migrations.CreateModel(
            name='ActAditional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nr_registru', models.IntegerField(default=contr_clienti.models.increment_nr_reg, unique=True)),
                ('nr_actaditional', models.IntegerField()),
                ('data_actaditional', models.DateField(blank=True, null=True)),
                ('data_incepere_actaditional', models.DateField(blank=True, null=True)),
                ('data_sfarsit_actaditional', models.DateField(blank=True, null=True)),
                ('observatii', models.TextField(blank=True, max_length=255)),
                ('aplicatii', models.ManyToManyField(blank=True, to='contr_clienti.AplicatiiInfo98')),
                ('contract', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contr_clienti.Contract')),
                ('produse', models.ManyToManyField(blank=True, to='contr_clienti.Produse')),
                ('servicii', models.ManyToManyField(blank=True, to='contr_clienti.ServiciiInformatice')),
            ],
            options={
                'verbose_name_plural': 'Acte Aditionale',
            },
        ),
    ]
