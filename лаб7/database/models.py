from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Confederacy(models.Model):
    confederacy_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'confederacy'


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


class Sponsor(models.Model):
    sponsor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'sponsor'

class Club(models.Model):
    club_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    rating = models.IntegerField(blank=True, null=True)
    confederacy = models.ForeignKey(Confederacy, models.DO_NOTHING, blank=True, null=True)
    sponsor = models.ForeignKey(Sponsor, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'club'

class Match(models.Model):
    match_id = models.AutoField(primary_key=True)
    playdata = models.DateTimeField(blank=True, null=True)
    count1 = models.IntegerField()
    club_id1 = models.ForeignKey(Club, models.DO_NOTHING, related_name = 'club_id1', db_column='club_id1', blank=True, null=True)
    count2 = models.IntegerField()
    club_id2 = models.ForeignKey(Club, models.DO_NOTHING, related_name = 'club_id2', db_column='club_id2', blank=True, null=True)
    sold = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'match'

class Coach(models.Model):
    coach_id = models.AutoField(primary_key=True)
    club = models.ForeignKey(Club, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'coach'


class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    club = models.ForeignKey(Club, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    efficiency = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player'
