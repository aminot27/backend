from apps.warehouse.models.unit_model import Unit


class UnitRepository:

    @staticmethod
    def get_unit(unit_id):
        return Unit.objects.get_one(unit_id)

    @staticmethod
    def get_units(*values, **params):
        return Unit.objects.get_many(*values, **params)

    @staticmethod
    def create_unit(unit):
        return Unit.objects.create_one(**unit)

    @staticmethod
    def update_unit(unit_id, unit):
        return Unit.objects.update_one(obj_primary_key=unit_id, **unit)

    @staticmethod
    def log_delete_unit(unit_id):
        return Unit.objects.log_delete_one(primary_key=unit_id)

    @staticmethod
    def soft_delete_unit(unit_id):
        return Unit.objects.soft_delete_one(primary_key=unit_id)
