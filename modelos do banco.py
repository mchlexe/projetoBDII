# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AppUsuario(models.Model):
    id = models.BigAutoField(primary_key=True)
    cod = models.IntegerField()
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'app_usuario'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Estados(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    codigo = models.CharField(max_length=2, blank=True, null=True)
    nome = models.CharField(max_length=50, blank=True, null=True)
    sigla_uf = models.CharField(max_length=2, blank=True, null=True)
    nm_regiao = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estados'


class Imediatas(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    cd_rgi = models.CharField(max_length=6, blank=True, null=True)
    nm_rgi = models.CharField(max_length=100, blank=True, null=True)
    sigla_uf = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'imediatas'


class Intermediarias(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    cd_rgint = models.CharField(max_length=4, blank=True, null=True)
    nm_rgint = models.CharField(max_length=100, blank=True, null=True)
    sigla_uf = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intermediarias'


class Layer(models.Model):
    topology = models.OneToOneField('Topology', models.DO_NOTHING, primary_key=True)
    layer_id = models.IntegerField()
    schema_name = models.CharField(max_length=-1)
    table_name = models.CharField(max_length=-1)
    feature_column = models.CharField(max_length=-1)
    feature_type = models.IntegerField()
    level = models.IntegerField()
    child_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'layer'
        unique_together = (('topology', 'layer_id'), ('schema_name', 'table_name', 'feature_column'),)


class Mesorregioes(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    codigo = models.CharField(max_length=4, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    sigla_uf = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mesorregioes'


class Microrregioes(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    codigo = models.CharField(max_length=5, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    sigla_uf = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'microrregioes'


class Municipios(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    codigo = models.CharField(max_length=7, blank=True, null=True)
    nome = models.CharField(max_length=60, blank=True, null=True)
    sigla_uf = models.CharField(max_length=2, blank=True, null=True)
    area_km2 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'municipios'


class Populacao(models.Model):
    cod_municipio = models.IntegerField()
    ano = models.IntegerField()
    populacao = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'populacao'


class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True, null=True)
    auth_srid = models.IntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True, null=True)
    proj4text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spatial_ref_sys'


class Topology(models.Model):
    name = models.CharField(unique=True, max_length=-1)
    srid = models.IntegerField()
    precision = models.FloatField()
    hasz = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'topology'
