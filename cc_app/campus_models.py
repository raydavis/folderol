from django.db import models, connection, connections, transaction

class CampusDbManager(models.Manager):
    def get_person_attributes(self, person_id):
        sql = ('select pi.ldap_uid, pi.ug_grad_flag, pi.first_name, pi.last_name, pi.person_name, pi.email_address, pi.affiliations,'
        ' sm.major_name, sm.major_title, sm.college_abbr, sm.major_name2, sm.major_title2, sm.college_abbr2,'
        ' sm.major_name3, sm.major_title3, sm.college_abbr3, sm.major_name4, sm.major_title4, sm.college_abbr4'
        ' from bspace_person_info_vw pi'
        ' left join bspace_student_major_vw sm on pi.ldap_uid = sm.ldap_uid'
        ' where pi.ldap_uid = %s')
        cursor = connections['campusdb'].cursor()
        cursor.execute(sql, [person_id])
        desc = cursor.description
        row = cursor.fetchone()
        attrs = dict(zip([col[0] for col in desc], row))
        return attrs

class CampusPersonAttributes(models.Model):
    ldap_uid = models.BigIntegerField(primary_key=True)
    person_name = models.CharField(max_length=400)
    class Meta:
        app_label = 'campusdb'
        db_table = 'bspace_person_info_vw'
        managed = False
    def __unicode__(self):
        return str(vars(self))
    objects = CampusDbManager()
