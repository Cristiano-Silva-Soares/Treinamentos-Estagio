# Generated by Django 4.0.3 on 2022-03-17 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'db_table': 'branch',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'city',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=64)),
                ('income', models.DecimalField(decimal_places=2, max_digits=16)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
            ],
            options={
                'db_table': 'customer',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=64)),
                ('city', models.ForeignKey(db_column='id_city', on_delete=django.db.models.deletion.DO_NOTHING, to='core.city')),
            ],
            options={
                'db_table': 'district',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=64)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=16)),
                ('admission_date', models.DateField()),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
            ],
            options={
                'db_table': 'employee',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MaritalStatus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'db_table': 'marital_status',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('cost_price', models.DecimalField(decimal_places=2, max_digits=16)),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=16)),
            ],
            options={
                'db_table': 'product',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProductGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('commission_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('gain_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'db_table': 'product_group',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('branch', models.ForeignKey(db_column='id_branch', on_delete=django.db.models.deletion.DO_NOTHING, to='core.branch')),
                ('customer', models.ForeignKey(db_column='id_customer', on_delete=django.db.models.deletion.DO_NOTHING, to='core.customer')),
                ('employee', models.ForeignKey(db_column='id_employee', on_delete=django.db.models.deletion.DO_NOTHING, to='core.employee')),
            ],
            options={
                'db_table': 'sale',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('abbreviation', models.CharField(max_length=2)),
            ],
            options={
                'db_table': 'state',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('legal_document', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'db_table': 'supplier',
                'managed': True,
            },
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='zone',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.CreateModel(
            name='SaleItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('quantity', models.DecimalField(decimal_places=3, max_digits=16)),
                ('product', models.ForeignKey(db_column='id_product', on_delete=django.db.models.deletion.DO_NOTHING, to='core.product')),
                ('sale', models.ForeignKey(db_column='id_sale', on_delete=django.db.models.deletion.DO_NOTHING, to='core.sale')),
            ],
            options={
                'db_table': 'sale_item',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='product',
            name='product_group',
            field=models.ForeignKey(db_column='id_product_group', on_delete=django.db.models.deletion.DO_NOTHING, to='core.productgroup'),
        ),
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(db_column='id_supplier', on_delete=django.db.models.deletion.DO_NOTHING, to='core.supplier'),
        ),
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(db_column='id_department', on_delete=django.db.models.deletion.DO_NOTHING, to='core.department'),
        ),
        migrations.AddField(
            model_name='employee',
            name='district',
            field=models.ForeignKey(db_column='id_district', on_delete=django.db.models.deletion.DO_NOTHING, to='core.district'),
        ),
        migrations.AddField(
            model_name='employee',
            name='marital_status',
            field=models.ForeignKey(db_column='id_marital_status', on_delete=django.db.models.deletion.DO_NOTHING, to='core.maritalstatus'),
        ),
        migrations.AddField(
            model_name='district',
            name='zone',
            field=models.ForeignKey(db_column='id_zone', on_delete=django.db.models.deletion.DO_NOTHING, to='core.zone'),
        ),
        migrations.AddField(
            model_name='customer',
            name='district',
            field=models.ForeignKey(db_column='id_district', on_delete=django.db.models.deletion.DO_NOTHING, to='core.district'),
        ),
        migrations.AddField(
            model_name='customer',
            name='marital_status',
            field=models.ForeignKey(db_column='id_marital_status', on_delete=django.db.models.deletion.DO_NOTHING, to='core.maritalstatus'),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(db_column='id_state', on_delete=django.db.models.deletion.DO_NOTHING, related_name='cities', to='core.state'),
        ),
        migrations.AddField(
            model_name='branch',
            name='district',
            field=models.ForeignKey(db_column='id_district', on_delete=django.db.models.deletion.DO_NOTHING, to='core.district'),
        ),
    ]