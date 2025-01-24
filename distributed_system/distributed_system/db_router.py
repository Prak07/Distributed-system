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
        # Allow relations if both models are in the simulation app
        if obj1._meta.app_label in ['users', 'products', 'orders'] and obj2._meta.app_label in ['users', 'products', 'orders']:
            return True
        return False