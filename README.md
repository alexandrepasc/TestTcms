# TestTcms

python manage.py test <br>
python manage.py createsuperuser <br>
<br><br>
<h3>Create table</h3><br>
Model<br>

    from django.db import models

    class RunTest(models.Model):
    class Meta:
        managed = False
        db_table = 'integration_view'

    name = models.CharField(
        db_column='object_name',
        max_length=255,
        primary_key=True,
        verbose_name='Object Name',
    )
    some_value = models.CharField(
        db_column='some_object_value',
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Some Object Value',
    )

    # Depending on the situation it might be a good idea to redefine
    # some methods as a NOOP as a safety-net.
    # Note, that it's not completely safe this way, but might help with some
    # silly mistakes in user code

    def save(self, *args, **kwargs):
        """Preventing data modification."""
        pass

    def delete(self, *args, **kwargs):
        """Preventing data deletion."""
        pass

<br>
Create:<br>

    from django.db import connection
    from mgrtests.mtest.myModel import RunTest
    
    with connection.schema_editor() as schema_editor:
        schema_editor.create_model(RunTest)