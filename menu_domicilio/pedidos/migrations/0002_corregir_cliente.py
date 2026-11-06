from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('pedidos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='dreccion',
            new_name='direccion',
        ),
        migrations.AddField(
            model_name='cliente',
            name='usuario',
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='cliente',
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
