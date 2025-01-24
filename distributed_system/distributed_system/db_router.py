class DatabaseRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'users':
            return 'users'
        elif model._meta.app_label == 'products':
            return 'products'
        elif model._meta.app_label == 'orders':
            return 'orders'
        return 'default'

    def db_for_write(self, model, **hints):
        return self.db_for_read(model, **hints)
    
    def allow_relation(self, obj1, obj2, **hints):
        return True