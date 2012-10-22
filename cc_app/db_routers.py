class CampusDbRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'campusdb':
            return 'campusdb'
        return None
    def db_for_write(self, model, **hints):
        return None
    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'campusdb' or obj2._meta.app_label == 'campusdb':
            return True
        return None
    def allow_syncdb(self, db, model):
        if db == 'campusdb' or model._meta.app_label == 'campusdb':
            return False
        else:
            return None
