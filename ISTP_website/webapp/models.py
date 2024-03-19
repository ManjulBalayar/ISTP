# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Qol(models.Model):
    commid = models.FloatField(db_column='CommID', blank=True, primary_key=True)  # Field name made lowercase.
    fipspl = models.IntegerField(db_column='FIPSPL', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    cat = models.TextField(db_column='CAT', blank=True, null=True)  # Field name made lowercase.
    qoljobs_vg = models.FloatField(db_column='QOLjobs_vg', blank=True, null=True)  # Field name made lowercase.
    qoljobs_g = models.FloatField(db_column='QOLjobs_g', blank=True, null=True)  # Field name made lowercase.
    qoljobs_f = models.FloatField(db_column='QOLjobs_f', blank=True, null=True)  # Field name made lowercase.
    qoljobs_p = models.FloatField(db_column='QOLjobs_p', blank=True, null=True)  # Field name made lowercase.
    qoljobs_dnk = models.FloatField(db_column='QOLjobs_dnk', blank=True, null=True)  # Field name made lowercase.
    qoljobs_na = models.FloatField(db_column='QOLjobs_na', blank=True, null=True)  # Field name made lowercase.
    qolmedical_vg = models.CharField(db_column='QOLmedical_vg', max_length=255, blank=True, null=True)  # Field name made lowercase.
    qolmedical_g = models.CharField(db_column='QOLmedical_g', max_length=255, blank=True, null=True)  # Field name made lowercase.
    qolmedical_f = models.CharField(db_column='QOLmedical_f', max_length=255, blank=True, null=True)  # Field name made lowercase.
    qolmedical_p = models.CharField(db_column='QOLmedical_p', max_length=255, blank=True, null=True)  # Field name made lowercase.
    qolmedical_dnk = models.CharField(db_column='QOLmedical_dnk', max_length=255, blank=True, null=True)  # Field name made lowercase.
    qolmedical_na = models.CharField(db_column='QOLmedical_na', max_length=255, blank=True, null=True)  # Field name made lowercase.
    qolk12_vg = models.FloatField(db_column='QOLk12_vg', blank=True, null=True)  # Field name made lowercase.
    qolk12_g = models.FloatField(db_column='QOLk12_g', blank=True, null=True)  # Field name made lowercase.
    qolk12_f = models.FloatField(db_column='QOLk12_f', blank=True, null=True)  # Field name made lowercase.
    qolk12_p = models.FloatField(db_column='QOLk12_p', blank=True, null=True)  # Field name made lowercase.
    qolk12_dnk = models.FloatField(db_column='QOLk12_dnk', blank=True, null=True)  # Field name made lowercase.
    qolk12_na = models.FloatField(db_column='QOLk12_na', blank=True, null=True)  # Field name made lowercase.
    qolhousing_vg = models.FloatField(db_column='QOLhousing_vg', blank=True, null=True)  # Field name made lowercase.
    qolhousing_g = models.FloatField(db_column='QOLhousing_g', blank=True, null=True)  # Field name made lowercase.
    qolhousing_f = models.FloatField(db_column='QOLhousing_f', blank=True, null=True)  # Field name made lowercase.
    qolhousing_p = models.FloatField(db_column='QOLhousing_p', blank=True, null=True)  # Field name made lowercase.
    qolhousing_dnk = models.FloatField(db_column='QOLhousing_dnk', blank=True, null=True)  # Field name made lowercase.
    qolhousing_na = models.FloatField(db_column='QOLhousing_na', blank=True, null=True)  # Field name made lowercase.
    qolshop_vg = models.FloatField(db_column='QOLshop_vg', blank=True, null=True)  # Field name made lowercase.
    qolshop_g = models.FloatField(db_column='QOLshop_g', blank=True, null=True)  # Field name made lowercase.
    qolshop_f = models.FloatField(db_column='QOLshop_f', blank=True, null=True)  # Field name made lowercase.
    qolshop_p = models.FloatField(db_column='QOLshop_p', blank=True, null=True)  # Field name made lowercase.
    qolshop_dnk = models.FloatField(db_column='QOLshop_dnk', blank=True, null=True)  # Field name made lowercase.
    qolshop_na = models.FloatField(db_column='QOLshop_na', blank=True, null=True)  # Field name made lowercase.
    qolchildcare_vg = models.FloatField(db_column='QOLchildcare_vg', blank=True, null=True)  # Field name made lowercase.
    qolchildcare_g = models.FloatField(db_column='QOLchildcare_g', blank=True, null=True)  # Field name made lowercase.
    qolchildcare_f = models.FloatField(db_column='QOLchildcare_f', blank=True, null=True)  # Field name made lowercase.
    qolchildcare_p = models.FloatField(db_column='QOLchildcare_p', blank=True, null=True)  # Field name made lowercase.
    qolchildcare_dnk = models.FloatField(db_column='QOLchildcare_dnk', blank=True, null=True)  # Field name made lowercase.
    qolchildcare_na = models.FloatField(db_column='QOLchildcare_na', blank=True, null=True)  # Field name made lowercase.
    qolseniorcare_vg = models.FloatField(db_column='QOLseniorcare_vg', blank=True, null=True)  # Field name made lowercase.
    qolseniorcare_g = models.FloatField(db_column='QOLseniorcare_g', blank=True, null=True)  # Field name made lowercase.
    qolseniorcare_f = models.FloatField(db_column='QOLseniorcare_f', blank=True, null=True)  # Field name made lowercase.
    qolseniorcare_p = models.FloatField(db_column='QOLseniorcare_p', blank=True, null=True)  # Field name made lowercase.
    qolseniorcare_dnk = models.FloatField(db_column='QOLseniorcare_dnk', blank=True, null=True)  # Field name made lowercase.
    qolseniorcare_na = models.FloatField(db_column='QOLseniorcare_na', blank=True, null=True)  # Field name made lowercase.
    qolyouth_vg = models.FloatField(db_column='QOLyouth_vg', blank=True, null=True)  # Field name made lowercase.
    qolyouth_g = models.FloatField(db_column='QOLyouth_g', blank=True, null=True)  # Field name made lowercase.
    qolyouth_f = models.FloatField(db_column='QOLyouth_f', blank=True, null=True)  # Field name made lowercase.
    qolyouth_p = models.FloatField(db_column='QOLyouth_p', blank=True, null=True)  # Field name made lowercase.
    qolyouth_dnk = models.FloatField(db_column='QOLyouth_dnk', blank=True, null=True)  # Field name made lowercase.
    qolyouth_na = models.FloatField(db_column='QOLyouth_na', blank=True, null=True)  # Field name made lowercase.
    qolcommsrvall_vg = models.FloatField(db_column='QOLcommsrvall_vg', blank=True, null=True)  # Field name made lowercase.
    qolcommsrvall_g = models.FloatField(db_column='QOLcommsrvall_g', blank=True, null=True)  # Field name made lowercase.
    qolcommsrvall_f = models.FloatField(db_column='QOLcommsrvall_f', blank=True, null=True)  # Field name made lowercase.
    qolcommsrvall_p = models.FloatField(db_column='QOLcommsrvall_p', blank=True, null=True)  # Field name made lowercase.
    qolcommsrvall_dnk = models.FloatField(db_column='QOLcommsrvall_dnk', blank=True, null=True)  # Field name made lowercase.
    qolcommsrvall_na = models.FloatField(db_column='QOLcommsrvall_na', blank=True, null=True)  # Field name made lowercase.
    qolrecrentr_vg = models.FloatField(db_column='QOLrecrentr_vg', blank=True, null=True)  # Field name made lowercase.
    qolrecrentr_g = models.FloatField(db_column='QOLrecrentr_g', blank=True, null=True)  # Field name made lowercase.
    qolrecrentr_f = models.FloatField(db_column='QOLrecrentr_f', blank=True, null=True)  # Field name made lowercase.
    qolrecrentr_p = models.FloatField(db_column='QOLrecrentr_p', blank=True, null=True)  # Field name made lowercase.
    qolrecrentr_dnk = models.FloatField(db_column='QOLrecrentr_dnk', blank=True, null=True)  # Field name made lowercase.
    qolrecrentr_na = models.FloatField(db_column='QOLrecrentr_na', blank=True, null=True)  # Field name made lowercase.
    qolpolice_vg = models.FloatField(db_column='QOLpolice_vg', blank=True, null=True)  # Field name made lowercase.
    qolpolice_g = models.FloatField(db_column='QOLpolice_g', blank=True, null=True)  # Field name made lowercase.
    qolpolice_f = models.FloatField(db_column='QOLpolice_f', blank=True, null=True)  # Field name made lowercase.
    qolpolice_p = models.FloatField(db_column='QOLpolice_p', blank=True, null=True)  # Field name made lowercase.
    qolpolice_dnk = models.FloatField(db_column='QOLpolice_dnk', blank=True, null=True)  # Field name made lowercase.
    qolpolice_na = models.FloatField(db_column='QOLpolice_na', blank=True, null=True)  # Field name made lowercase.
    qolfire_vg = models.FloatField(db_column='QOLfire_vg', blank=True, null=True)  # Field name made lowercase.
    qolfire_g = models.FloatField(db_column='QOLfire_g', blank=True, null=True)  # Field name made lowercase.
    qolfire_f = models.FloatField(db_column='QOLfire_f', blank=True, null=True)  # Field name made lowercase.
    qolfire_p = models.FloatField(db_column='QOLfire_p', blank=True, null=True)  # Field name made lowercase.
    qolfire_dnk = models.FloatField(db_column='QOLfire_dnk', blank=True, null=True)  # Field name made lowercase.
    qolfire_na = models.FloatField(db_column='QOLfire_na', blank=True, null=True)  # Field name made lowercase.
    qolems_vg = models.FloatField(db_column='QOLems_vg', blank=True, null=True)  # Field name made lowercase.
    qolems_g = models.FloatField(db_column='QOLems_g', blank=True, null=True)  # Field name made lowercase.
    qolems_f = models.FloatField(db_column='QOLems_f', blank=True, null=True)  # Field name made lowercase.
    qolems_p = models.FloatField(db_column='QOLems_p', blank=True, null=True)  # Field name made lowercase.
    qolems_dnk = models.FloatField(db_column='QOLems_dnk', blank=True, null=True)  # Field name made lowercase.
    qolems_na = models.FloatField(db_column='QOLems_na', blank=True, null=True)  # Field name made lowercase.
    qolstreets_vg = models.FloatField(db_column='QOLstreets_vg', blank=True, null=True)  # Field name made lowercase.
    qolstreets_g = models.FloatField(db_column='QOLstreets_g', blank=True, null=True)  # Field name made lowercase.
    qolstreets_f = models.FloatField(db_column='QOLstreets_f', blank=True, null=True)  # Field name made lowercase.
    qolstreets_p = models.FloatField(db_column='QOLstreets_p', blank=True, null=True)  # Field name made lowercase.
    qolstreets_dnk = models.FloatField(db_column='QOLstreets_dnk', blank=True, null=True)  # Field name made lowercase.
    qolstreets_na = models.FloatField(db_column='QOLstreets_na', blank=True, null=True)  # Field name made lowercase.
    qolparks_vg = models.FloatField(db_column='QOLparks_vg', blank=True, null=True)  # Field name made lowercase.
    qolparks_g = models.FloatField(db_column='QOLparks_g', blank=True, null=True)  # Field name made lowercase.
    qolparks_f = models.FloatField(db_column='QOLparks_f', blank=True, null=True)  # Field name made lowercase.
    qolparks_p = models.FloatField(db_column='QOLparks_p', blank=True, null=True)  # Field name made lowercase.
    qolparks_dnk = models.FloatField(db_column='QOLparks_dnk', blank=True, null=True)  # Field name made lowercase.
    qolparks_na = models.FloatField(db_column='QOLparks_na', blank=True, null=True)  # Field name made lowercase.
    qolgarbage_vg = models.FloatField(db_column='QOLgarbage_vg', blank=True, null=True)  # Field name made lowercase.
    qolgarbage_g = models.FloatField(db_column='QOLgarbage_g', blank=True, null=True)  # Field name made lowercase.
    qolgarbage_f = models.FloatField(db_column='QOLgarbage_f', blank=True, null=True)  # Field name made lowercase.
    qolgarbage_p = models.FloatField(db_column='QOLgarbage_p', blank=True, null=True)  # Field name made lowercase.
    qolgarbage_dnk = models.FloatField(db_column='QOLgarbage_dnk', blank=True, null=True)  # Field name made lowercase.
    qolgarbage_na = models.FloatField(db_column='QOLgarbage_na', blank=True, null=True)  # Field name made lowercase.
    qolwater_vg = models.FloatField(db_column='QOLwater_vg', blank=True, null=True)  # Field name made lowercase.
    qolwater_g = models.FloatField(db_column='QOLwater_g', blank=True, null=True)  # Field name made lowercase.
    qolwater_f = models.FloatField(db_column='QOLwater_f', blank=True, null=True)  # Field name made lowercase.
    qolwater_p = models.FloatField(db_column='QOLwater_p', blank=True, null=True)  # Field name made lowercase.
    qolwater_dnk = models.FloatField(db_column='QOLwater_dnk', blank=True, null=True)  # Field name made lowercase.
    qolwater_na = models.FloatField(db_column='QOLwater_na', blank=True, null=True)  # Field name made lowercase.
    qolgovtsrvall_vg = models.FloatField(db_column='QOLgovtsrvall_vg', blank=True, null=True)  # Field name made lowercase.
    qolgovtsrvall_g = models.FloatField(db_column='QOLgovtsrvall_g', blank=True, null=True)  # Field name made lowercase.
    qolgovtsrvall_f = models.FloatField(db_column='QOLgovtsrvall_f', blank=True, null=True)  # Field name made lowercase.
    qolgovtsrvall_p = models.FloatField(db_column='QOLgovtsrvall_p', blank=True, null=True)  # Field name made lowercase.
    qolgovtsrvall_dnk = models.FloatField(db_column='QOLgovtsrvall_dnk', blank=True, null=True)  # Field name made lowercase.
    qolgovtsrvall_na = models.FloatField(db_column='QOLgovtsrvall_na', blank=True, null=True)  # Field name made lowercase.
    pass

    class Meta:
        db_table = 'qol'

class Qol1994(models.Model):
    commid = models.FloatField(db_column='CommID', blank=True, primary_key=True)  # Field name made lowercase.
    fipspl = models.IntegerField(db_column='FIPSPL', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    cat = models.TextField(db_column='CAT', blank=True, null=True)  # Field name made lowercase.
    qoljobs_vg = models.FloatField(db_column='QOLjobs_vg', blank=True, null=True)  # Field name made lowercase.
    qoljobs_g = models.FloatField(db_column='QOLjobs_g', blank=True, null=True)  # Field name made lowercase.
    qoljobs_f = models.FloatField(db_column='QOLjobs_f', blank=True, null=True)  # Field name made lowercase.
    qoljobs_p = models.FloatField(db_column='QOLjobs_p', blank=True, null=True)  # Field name made lowercase.
    qoljobs_dnk = models.FloatField(db_column='QOLjobs_dnk', blank=True, null=True)  # Field name made lowercase.
    qoljobs_na = models.FloatField(db_column='QOLjobs_na', blank=True, null=True)  # Field name made lowercase.
    qolmedical_vg = models.CharField(db_column='QOLmedical_vg', max_length=255, blank=True, null=True)  # Field name made lowercase.
    qolmedical_g = models.CharField(db_column='QOLmedical_g', max_length=255, blank=True, null=True)  # Field name made lowercase.
    qolmedical_f = models.CharField(db_column='QOLmedical_f', max_length=255, blank=True, null=True)  # Field name made lowercase.
    qolmedical_p = models.CharField(db_column='QOLmedical_p', max_length=255, blank=True, null=True)  # Field name made lowercase.
    qolmedical_dnk = models.CharField(db_column='QOLmedical_dnk', max_length=255, blank=True, null=True)  # Field name made lowercase.
    qolmedical_na = models.CharField(db_column='QOLmedical_na', max_length=255, blank=True, null=True)  # Field name made lowercase.
    qolk12_vg = models.FloatField(db_column='QOLk12_vg', blank=True, null=True)  # Field name made lowercase.
    qolk12_g = models.FloatField(db_column='QOLk12_g', blank=True, null=True)  # Field name made lowercase.
    qolk12_f = models.FloatField(db_column='QOLk12_f', blank=True, null=True)  # Field name made lowercase.
    qolk12_p = models.FloatField(db_column='QOLk12_p', blank=True, null=True)  # Field name made lowercase.
    qolk12_dnk = models.FloatField(db_column='QOLk12_dnk', blank=True, null=True)  # Field name made lowercase.
    qolk12_na = models.FloatField(db_column='QOLk12_na', blank=True, null=True)  # Field name made lowercase.
    qolhousing_vg = models.FloatField(db_column='QOLhousing_vg', blank=True, null=True)  # Field name made lowercase.
    qolhousing_g = models.FloatField(db_column='QOLhousing_g', blank=True, null=True)  # Field name made lowercase.
    qolhousing_f = models.FloatField(db_column='QOLhousing_f', blank=True, null=True)  # Field name made lowercase.
    qolhousing_p = models.FloatField(db_column='QOLhousing_p', blank=True, null=True)  # Field name made lowercase.
    qolhousing_dnk = models.FloatField(db_column='QOLhousing_dnk', blank=True, null=True)  # Field name made lowercase.
    qolhousing_na = models.FloatField(db_column='QOLhousing_na', blank=True, null=True)  # Field name made lowercase.
    qolshop_vg = models.FloatField(db_column='QOLshop_vg', blank=True, null=True)  # Field name made lowercase.
    qolshop_g = models.FloatField(db_column='QOLshop_g', blank=True, null=True)  # Field name made lowercase.
    qolshop_f = models.FloatField(db_column='QOLshop_f', blank=True, null=True)  # Field name made lowercase.
    qolshop_p = models.FloatField(db_column='QOLshop_p', blank=True, null=True)  # Field name made lowercase.
    qolshop_dnk = models.FloatField(db_column='QOLshop_dnk', blank=True, null=True)  # Field name made lowercase.
    qolshop_na = models.FloatField(db_column='QOLshop_na', blank=True, null=True)  # Field name made lowercase.
    qolchildcare_vg = models.FloatField(db_column='QOLchildcare_vg', blank=True, null=True)  # Field name made lowercase.
    qolchildcare_g = models.FloatField(db_column='QOLchildcare_g', blank=True, null=True)  # Field name made lowercase.
    qolchildcare_f = models.FloatField(db_column='QOLchildcare_f', blank=True, null=True)  # Field name made lowercase.
    qolchildcare_p = models.FloatField(db_column='QOLchildcare_p', blank=True, null=True)  # Field name made lowercase.
    qolchildcare_dnk = models.FloatField(db_column='QOLchildcare_dnk', blank=True, null=True)  # Field name made lowercase.
    qolchildcare_na = models.FloatField(db_column='QOLchildcare_na', blank=True, null=True)  # Field name made lowercase.
    qolseniorcare_vg = models.FloatField(db_column='QOLseniorcare_vg', blank=True, null=True)  # Field name made lowercase.
    qolseniorcare_g = models.FloatField(db_column='QOLseniorcare_g', blank=True, null=True)  # Field name made lowercase.
    qolseniorcare_f = models.FloatField(db_column='QOLseniorcare_f', blank=True, null=True)  # Field name made lowercase.
    qolseniorcare_p = models.FloatField(db_column='QOLseniorcare_p', blank=True, null=True)  # Field name made lowercase.
    qolseniorcare_dnk = models.FloatField(db_column='QOLseniorcare_dnk', blank=True, null=True)  # Field name made lowercase.
    qolseniorcare_na = models.FloatField(db_column='QOLseniorcare_na', blank=True, null=True)  # Field name made lowercase.
    qolyouth_vg = models.FloatField(db_column='QOLyouth_vg', blank=True, null=True)  # Field name made lowercase.
    qolyouth_g = models.FloatField(db_column='QOLyouth_g', blank=True, null=True)  # Field name made lowercase.
    qolyouth_f = models.FloatField(db_column='QOLyouth_f', blank=True, null=True)  # Field name made lowercase.
    qolyouth_p = models.FloatField(db_column='QOLyouth_p', blank=True, null=True)  # Field name made lowercase.
    qolyouth_dnk = models.FloatField(db_column='QOLyouth_dnk', blank=True, null=True)  # Field name made lowercase.
    qolyouth_na = models.FloatField(db_column='QOLyouth_na', blank=True, null=True)  # Field name made lowercase.
    qolcommsrvall_vg = models.FloatField(db_column='QOLcommsrvall_vg', blank=True, null=True)  # Field name made lowercase.
    qolcommsrvall_g = models.FloatField(db_column='QOLcommsrvall_g', blank=True, null=True)  # Field name made lowercase.
    qolcommsrvall_f = models.FloatField(db_column='QOLcommsrvall_f', blank=True, null=True)  # Field name made lowercase.
    qolcommsrvall_p = models.FloatField(db_column='QOLcommsrvall_p', blank=True, null=True)  # Field name made lowercase.
    qolcommsrvall_dnk = models.FloatField(db_column='QOLcommsrvall_dnk', blank=True, null=True)  # Field name made lowercase.
    qolcommsrvall_na = models.FloatField(db_column='QOLcommsrvall_na', blank=True, null=True)  # Field name made lowercase.
    qolrecrentr_vg = models.FloatField(db_column='QOLrecrentr_vg', blank=True, null=True)  # Field name made lowercase.
    qolrecrentr_g = models.FloatField(db_column='QOLrecrentr_g', blank=True, null=True)  # Field name made lowercase.
    qolrecrentr_f = models.FloatField(db_column='QOLrecrentr_f', blank=True, null=True)  # Field name made lowercase.
    qolrecrentr_p = models.FloatField(db_column='QOLrecrentr_p', blank=True, null=True)  # Field name made lowercase.
    qolrecrentr_dnk = models.FloatField(db_column='QOLrecrentr_dnk', blank=True, null=True)  # Field name made lowercase.
    qolrecrentr_na = models.FloatField(db_column='QOLrecrentr_na', blank=True, null=True)  # Field name made lowercase.
    qolpolice_vg = models.FloatField(db_column='QOLpolice_vg', blank=True, null=True)  # Field name made lowercase.
    qolpolice_g = models.FloatField(db_column='QOLpolice_g', blank=True, null=True)  # Field name made lowercase.
    qolpolice_f = models.FloatField(db_column='QOLpolice_f', blank=True, null=True)  # Field name made lowercase.
    qolpolice_p = models.FloatField(db_column='QOLpolice_p', blank=True, null=True)  # Field name made lowercase.
    qolpolice_dnk = models.FloatField(db_column='QOLpolice_dnk', blank=True, null=True)  # Field name made lowercase.
    qolpolice_na = models.FloatField(db_column='QOLpolice_na', blank=True, null=True)  # Field name made lowercase.
    qolfire_vg = models.FloatField(db_column='QOLfire_vg', blank=True, null=True)  # Field name made lowercase.
    qolfire_g = models.FloatField(db_column='QOLfire_g', blank=True, null=True)  # Field name made lowercase.
    qolfire_f = models.FloatField(db_column='QOLfire_f', blank=True, null=True)  # Field name made lowercase.
    qolfire_p = models.FloatField(db_column='QOLfire_p', blank=True, null=True)  # Field name made lowercase.
    qolfire_dnk = models.FloatField(db_column='QOLfire_dnk', blank=True, null=True)  # Field name made lowercase.
    qolfire_na = models.FloatField(db_column='QOLfire_na', blank=True, null=True)  # Field name made lowercase.
    qolems_vg = models.FloatField(db_column='QOLems_vg', blank=True, null=True)  # Field name made lowercase.
    qolems_g = models.FloatField(db_column='QOLems_g', blank=True, null=True)  # Field name made lowercase.
    qolems_f = models.FloatField(db_column='QOLems_f', blank=True, null=True)  # Field name made lowercase.
    qolems_p = models.FloatField(db_column='QOLems_p', blank=True, null=True)  # Field name made lowercase.
    qolems_dnk = models.FloatField(db_column='QOLems_dnk', blank=True, null=True)  # Field name made lowercase.
    qolems_na = models.FloatField(db_column='QOLems_na', blank=True, null=True)  # Field name made lowercase.
    qolstreets_vg = models.FloatField(db_column='QOLstreets_vg', blank=True, null=True)  # Field name made lowercase.
    qolstreets_g = models.FloatField(db_column='QOLstreets_g', blank=True, null=True)  # Field name made lowercase.
    qolstreets_f = models.FloatField(db_column='QOLstreets_f', blank=True, null=True)  # Field name made lowercase.
    qolstreets_p = models.FloatField(db_column='QOLstreets_p', blank=True, null=True)  # Field name made lowercase.
    qolstreets_dnk = models.FloatField(db_column='QOLstreets_dnk', blank=True, null=True)  # Field name made lowercase.
    qolstreets_na = models.FloatField(db_column='QOLstreets_na', blank=True, null=True)  # Field name made lowercase.
    qolparks_vg = models.FloatField(db_column='QOLparks_vg', blank=True, null=True)  # Field name made lowercase.
    qolparks_g = models.FloatField(db_column='QOLparks_g', blank=True, null=True)  # Field name made lowercase.
    qolparks_f = models.FloatField(db_column='QOLparks_f', blank=True, null=True)  # Field name made lowercase.
    qolparks_p = models.FloatField(db_column='QOLparks_p', blank=True, null=True)  # Field name made lowercase.
    qolparks_dnk = models.FloatField(db_column='QOLparks_dnk', blank=True, null=True)  # Field name made lowercase.
    qolparks_na = models.FloatField(db_column='QOLparks_na', blank=True, null=True)  # Field name made lowercase.
    qolgarbage_vg = models.FloatField(db_column='QOLgarbage_vg', blank=True, null=True)  # Field name made lowercase.
    qolgarbage_g = models.FloatField(db_column='QOLgarbage_g', blank=True, null=True)  # Field name made lowercase.
    qolgarbage_f = models.FloatField(db_column='QOLgarbage_f', blank=True, null=True)  # Field name made lowercase.
    qolgarbage_p = models.FloatField(db_column='QOLgarbage_p', blank=True, null=True)  # Field name made lowercase.
    qolgarbage_dnk = models.FloatField(db_column='QOLgarbage_dnk', blank=True, null=True)  # Field name made lowercase.
    qolgarbage_na = models.FloatField(db_column='QOLgarbage_na', blank=True, null=True)  # Field name made lowercase.
    qolwater_vg = models.FloatField(db_column='QOLwater_vg', blank=True, null=True)  # Field name made lowercase.
    qolwater_g = models.FloatField(db_column='QOLwater_g', blank=True, null=True)  # Field name made lowercase.
    qolwater_f = models.FloatField(db_column='QOLwater_f', blank=True, null=True)  # Field name made lowercase.
    qolwater_p = models.FloatField(db_column='QOLwater_p', blank=True, null=True)  # Field name made lowercase.
    qolwater_dnk = models.FloatField(db_column='QOLwater_dnk', blank=True, null=True)  # Field name made lowercase.
    qolwater_na = models.FloatField(db_column='QOLwater_na', blank=True, null=True)  # Field name made lowercase.
    qolgovtsrvall_vg = models.FloatField(db_column='QOLgovtsrvall_vg', blank=True, null=True)  # Field name made lowercase.
    qolgovtsrvall_g = models.FloatField(db_column='QOLgovtsrvall_g', blank=True, null=True)  # Field name made lowercase.
    qolgovtsrvall_f = models.FloatField(db_column='QOLgovtsrvall_f', blank=True, null=True)  # Field name made lowercase.
    qolgovtsrvall_p = models.FloatField(db_column='QOLgovtsrvall_p', blank=True, null=True)  # Field name made lowercase.
    qolgovtsrvall_dnk = models.FloatField(db_column='QOLgovtsrvall_dnk', blank=True, null=True)  # Field name made lowercase.
    qolgovtsrvall_na = models.FloatField(db_column='QOLgovtsrvall_na', blank=True, null=True)  # Field name made lowercase.
    pass

    class Meta:
        db_table = 'qol1994'

class Qol2004(models.Model):
    commid = models.FloatField(db_column='CommID', blank=True, primary_key=True)  # Field name made lowercase.
    fipspl = models.IntegerField(db_column='FIPSPL', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    cat = models.TextField(db_column='CAT', blank=True, null=True)  # Field name made lowercase.
    qoljobs_vg = models.FloatField(db_column='QOLjobs_vg', blank=True, null=True)  # Field name made lowercase.
    qoljobs_g = models.FloatField(db_column='QOLjobs_g', blank=True, null=True)  # Field name made lowercase.
    qoljobs_f = models.FloatField(db_column='QOLjobs_f', blank=True, null=True)  # Field name made lowercase.
    qoljobs_p = models.FloatField(db_column='QOLjobs_p', blank=True, null=True)  # Field name made lowercase.
    qoljobs_dnk = models.FloatField(db_column='QOLjobs_dnk', blank=True, null=True)  # Field name made lowercase.
    qoljobs_na = models.FloatField(db_column='QOLjobs_na', blank=True, null=True)  # Field name made lowercase.
    qolmedical_vg = models.CharField(db_column='QOLmedical_vg', max_length=255, blank=True, null=True)  # Field name made lowercase.
    qolmedical_g = models.CharField(db_column='QOLmedical_g', max_length=255, blank=True, null=True)  # Field name made lowercase.
    qolmedical_f = models.CharField(db_column='QOLmedical_f', max_length=255, blank=True, null=True)  # Field name made lowercase.
    qolmedical_p = models.CharField(db_column='QOLmedical_p', max_length=255, blank=True, null=True)  # Field name made lowercase.
    qolmedical_dnk = models.CharField(db_column='QOLmedical_dnk', max_length=255, blank=True, null=True)  # Field name made lowercase.
    qolmedical_na = models.CharField(db_column='QOLmedical_na', max_length=255, blank=True, null=True)  # Field name made lowercase.
    qolk12_vg = models.FloatField(db_column='QOLk12_vg', blank=True, null=True)  # Field name made lowercase.
    qolk12_g = models.FloatField(db_column='QOLk12_g', blank=True, null=True)  # Field name made lowercase.
    qolk12_f = models.FloatField(db_column='QOLk12_f', blank=True, null=True)  # Field name made lowercase.
    qolk12_p = models.FloatField(db_column='QOLk12_p', blank=True, null=True)  # Field name made lowercase.
    qolk12_dnk = models.FloatField(db_column='QOLk12_dnk', blank=True, null=True)  # Field name made lowercase.
    qolk12_na = models.FloatField(db_column='QOLk12_na', blank=True, null=True)  # Field name made lowercase.
    qolhousing_vg = models.FloatField(db_column='QOLhousing_vg', blank=True, null=True)  # Field name made lowercase.
    qolhousing_g = models.FloatField(db_column='QOLhousing_g', blank=True, null=True)  # Field name made lowercase.
    qolhousing_f = models.FloatField(db_column='QOLhousing_f', blank=True, null=True)  # Field name made lowercase.
    qolhousing_p = models.FloatField(db_column='QOLhousing_p', blank=True, null=True)  # Field name made lowercase.
    qolhousing_dnk = models.FloatField(db_column='QOLhousing_dnk', blank=True, null=True)  # Field name made lowercase.
    qolhousing_na = models.FloatField(db_column='QOLhousing_na', blank=True, null=True)  # Field name made lowercase.
    qolshop_vg = models.FloatField(db_column='QOLshop_vg', blank=True, null=True)  # Field name made lowercase.
    qolshop_g = models.FloatField(db_column='QOLshop_g', blank=True, null=True)  # Field name made lowercase.
    qolshop_f = models.FloatField(db_column='QOLshop_f', blank=True, null=True)  # Field name made lowercase.
    qolshop_p = models.FloatField(db_column='QOLshop_p', blank=True, null=True)  # Field name made lowercase.
    qolshop_dnk = models.FloatField(db_column='QOLshop_dnk', blank=True, null=True)  # Field name made lowercase.
    qolshop_na = models.FloatField(db_column='QOLshop_na', blank=True, null=True)  # Field name made lowercase.
    qolchildcare_vg = models.FloatField(db_column='QOLchildcare_vg', blank=True, null=True)  # Field name made lowercase.
    qolchildcare_g = models.FloatField(db_column='QOLchildcare_g', blank=True, null=True)  # Field name made lowercase.
    qolchildcare_f = models.FloatField(db_column='QOLchildcare_f', blank=True, null=True)  # Field name made lowercase.
    qolchildcare_p = models.FloatField(db_column='QOLchildcare_p', blank=True, null=True)  # Field name made lowercase.
    qolchildcare_dnk = models.FloatField(db_column='QOLchildcare_dnk', blank=True, null=True)  # Field name made lowercase.
    qolchildcare_na = models.FloatField(db_column='QOLchildcare_na', blank=True, null=True)  # Field name made lowercase.
    qolseniorcare_vg = models.FloatField(db_column='QOLseniorcare_vg', blank=True, null=True)  # Field name made lowercase.
    qolseniorcare_g = models.FloatField(db_column='QOLseniorcare_g', blank=True, null=True)  # Field name made lowercase.
    qolseniorcare_f = models.FloatField(db_column='QOLseniorcare_f', blank=True, null=True)  # Field name made lowercase.
    qolseniorcare_p = models.FloatField(db_column='QOLseniorcare_p', blank=True, null=True)  # Field name made lowercase.
    qolseniorcare_dnk = models.FloatField(db_column='QOLseniorcare_dnk', blank=True, null=True)  # Field name made lowercase.
    qolseniorcare_na = models.FloatField(db_column='QOLseniorcare_na', blank=True, null=True)  # Field name made lowercase.
    qolyouth_vg = models.FloatField(db_column='QOLyouth_vg', blank=True, null=True)  # Field name made lowercase.
    qolyouth_g = models.FloatField(db_column='QOLyouth_g', blank=True, null=True)  # Field name made lowercase.
    qolyouth_f = models.FloatField(db_column='QOLyouth_f', blank=True, null=True)  # Field name made lowercase.
    qolyouth_p = models.FloatField(db_column='QOLyouth_p', blank=True, null=True)  # Field name made lowercase.
    qolyouth_dnk = models.FloatField(db_column='QOLyouth_dnk', blank=True, null=True)  # Field name made lowercase.
    qolyouth_na = models.FloatField(db_column='QOLyouth_na', blank=True, null=True)  # Field name made lowercase.
    qolcommsrvall_vg = models.FloatField(db_column='QOLcommsrvall_vg', blank=True, null=True)  # Field name made lowercase.
    qolcommsrvall_g = models.FloatField(db_column='QOLcommsrvall_g', blank=True, null=True)  # Field name made lowercase.
    qolcommsrvall_f = models.FloatField(db_column='QOLcommsrvall_f', blank=True, null=True)  # Field name made lowercase.
    qolcommsrvall_p = models.FloatField(db_column='QOLcommsrvall_p', blank=True, null=True)  # Field name made lowercase.
    qolcommsrvall_dnk = models.FloatField(db_column='QOLcommsrvall_dnk', blank=True, null=True)  # Field name made lowercase.
    qolcommsrvall_na = models.FloatField(db_column='QOLcommsrvall_na', blank=True, null=True)  # Field name made lowercase.
    qolrecrentr_vg = models.FloatField(db_column='QOLrecrentr_vg', blank=True, null=True)  # Field name made lowercase.
    qolrecrentr_g = models.FloatField(db_column='QOLrecrentr_g', blank=True, null=True)  # Field name made lowercase.
    qolrecrentr_f = models.FloatField(db_column='QOLrecrentr_f', blank=True, null=True)  # Field name made lowercase.
    qolrecrentr_p = models.FloatField(db_column='QOLrecrentr_p', blank=True, null=True)  # Field name made lowercase.
    qolrecrentr_dnk = models.FloatField(db_column='QOLrecrentr_dnk', blank=True, null=True)  # Field name made lowercase.
    qolrecrentr_na = models.FloatField(db_column='QOLrecrentr_na', blank=True, null=True)  # Field name made lowercase.
    qolpolice_vg = models.FloatField(db_column='QOLpolice_vg', blank=True, null=True)  # Field name made lowercase.
    qolpolice_g = models.FloatField(db_column='QOLpolice_g', blank=True, null=True)  # Field name made lowercase.
    qolpolice_f = models.FloatField(db_column='QOLpolice_f', blank=True, null=True)  # Field name made lowercase.
    qolpolice_p = models.FloatField(db_column='QOLpolice_p', blank=True, null=True)  # Field name made lowercase.
    qolpolice_dnk = models.FloatField(db_column='QOLpolice_dnk', blank=True, null=True)  # Field name made lowercase.
    qolpolice_na = models.FloatField(db_column='QOLpolice_na', blank=True, null=True)  # Field name made lowercase.
    qolfire_vg = models.FloatField(db_column='QOLfire_vg', blank=True, null=True)  # Field name made lowercase.
    qolfire_g = models.FloatField(db_column='QOLfire_g', blank=True, null=True)  # Field name made lowercase.
    qolfire_f = models.FloatField(db_column='QOLfire_f', blank=True, null=True)  # Field name made lowercase.
    qolfire_p = models.FloatField(db_column='QOLfire_p', blank=True, null=True)  # Field name made lowercase.
    qolfire_dnk = models.FloatField(db_column='QOLfire_dnk', blank=True, null=True)  # Field name made lowercase.
    qolfire_na = models.FloatField(db_column='QOLfire_na', blank=True, null=True)  # Field name made lowercase.
    qolems_vg = models.FloatField(db_column='QOLems_vg', blank=True, null=True)  # Field name made lowercase.
    qolems_g = models.FloatField(db_column='QOLems_g', blank=True, null=True)  # Field name made lowercase.
    qolems_f = models.FloatField(db_column='QOLems_f', blank=True, null=True)  # Field name made lowercase.
    qolems_p = models.FloatField(db_column='QOLems_p', blank=True, null=True)  # Field name made lowercase.
    qolems_dnk = models.FloatField(db_column='QOLems_dnk', blank=True, null=True)  # Field name made lowercase.
    qolems_na = models.FloatField(db_column='QOLems_na', blank=True, null=True)  # Field name made lowercase.
    qolstreets_vg = models.FloatField(db_column='QOLstreets_vg', blank=True, null=True)  # Field name made lowercase.
    qolstreets_g = models.FloatField(db_column='QOLstreets_g', blank=True, null=True)  # Field name made lowercase.
    qolstreets_f = models.FloatField(db_column='QOLstreets_f', blank=True, null=True)  # Field name made lowercase.
    qolstreets_p = models.FloatField(db_column='QOLstreets_p', blank=True, null=True)  # Field name made lowercase.
    qolstreets_dnk = models.FloatField(db_column='QOLstreets_dnk', blank=True, null=True)  # Field name made lowercase.
    qolstreets_na = models.FloatField(db_column='QOLstreets_na', blank=True, null=True)  # Field name made lowercase.
    qolparks_vg = models.FloatField(db_column='QOLparks_vg', blank=True, null=True)  # Field name made lowercase.
    qolparks_g = models.FloatField(db_column='QOLparks_g', blank=True, null=True)  # Field name made lowercase.
    qolparks_f = models.FloatField(db_column='QOLparks_f', blank=True, null=True)  # Field name made lowercase.
    qolparks_p = models.FloatField(db_column='QOLparks_p', blank=True, null=True)  # Field name made lowercase.
    qolparks_dnk = models.FloatField(db_column='QOLparks_dnk', blank=True, null=True)  # Field name made lowercase.
    qolparks_na = models.FloatField(db_column='QOLparks_na', blank=True, null=True)  # Field name made lowercase.
    qolgarbage_vg = models.FloatField(db_column='QOLgarbage_vg', blank=True, null=True)  # Field name made lowercase.
    qolgarbage_g = models.FloatField(db_column='QOLgarbage_g', blank=True, null=True)  # Field name made lowercase.
    qolgarbage_f = models.FloatField(db_column='QOLgarbage_f', blank=True, null=True)  # Field name made lowercase.
    qolgarbage_p = models.FloatField(db_column='QOLgarbage_p', blank=True, null=True)  # Field name made lowercase.
    qolgarbage_dnk = models.FloatField(db_column='QOLgarbage_dnk', blank=True, null=True)  # Field name made lowercase.
    qolgarbage_na = models.FloatField(db_column='QOLgarbage_na', blank=True, null=True)  # Field name made lowercase.
    qolwater_vg = models.FloatField(db_column='QOLwater_vg', blank=True, null=True)  # Field name made lowercase.
    qolwater_g = models.FloatField(db_column='QOLwater_g', blank=True, null=True)  # Field name made lowercase.
    qolwater_f = models.FloatField(db_column='QOLwater_f', blank=True, null=True)  # Field name made lowercase.
    qolwater_p = models.FloatField(db_column='QOLwater_p', blank=True, null=True)  # Field name made lowercase.
    qolwater_dnk = models.FloatField(db_column='QOLwater_dnk', blank=True, null=True)  # Field name made lowercase.
    qolwater_na = models.FloatField(db_column='QOLwater_na', blank=True, null=True)  # Field name made lowercase.
    qolgovtsrvall_vg = models.FloatField(db_column='QOLgovtsrvall_vg', blank=True, null=True)  # Field name made lowercase.
    qolgovtsrvall_g = models.FloatField(db_column='QOLgovtsrvall_g', blank=True, null=True)  # Field name made lowercase.
    qolgovtsrvall_f = models.FloatField(db_column='QOLgovtsrvall_f', blank=True, null=True)  # Field name made lowercase.
    qolgovtsrvall_p = models.FloatField(db_column='QOLgovtsrvall_p', blank=True, null=True)  # Field name made lowercase.
    qolgovtsrvall_dnk = models.FloatField(db_column='QOLgovtsrvall_dnk', blank=True, null=True)  # Field name made lowercase.
    qolgovtsrvall_na = models.FloatField(db_column='QOLgovtsrvall_na', blank=True, null=True)  # Field name made lowercase.
    pass

    class Meta:
        db_table = 'qol2004'