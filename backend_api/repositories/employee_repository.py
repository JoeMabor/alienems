from domain.usecases.repositories.employee_repository import EmployeeRepoPort
from domain.entities.employee import EmployeeEntity
from backend_api.models import Employee
from backend_api.models import WorkTime
from .helpers import DataConverter


class EmployeeRepoPortImp(EmployeeRepoPort):
    """
    Implementation of Employee repository in Django.
    """

    def retrieve_all(self):
        """
        Concrete implementation of abstract retrieve_all function in EmployeeRepo port
        :return:
        """
        employee_objs = Employee.objects.all()
        employee_models = []
        for employee in employee_objs:
            employee_models.append(DataConverter.to_employee_entity(employee))
        return employee_models

    def retrieve_by_id(self, employee_pk):
        """
        Concrete implementation of abstract retrieve_by_id function in EmployeeRepo port
        :param employee_pk:
        :return:
        """
        try:
            employee_obj = Employee.objects.get(pk=employee_pk)
            return DataConverter.to_employee_entity(employee_obj)
        except Employee.DoesNotExist:
            raise Employee.DoesNotExist

    def save(self, employee_entity: EmployeeEntity):
        """
        Concrete implementation of abstract save function in EmployeeRepot port
        :param employee_entity:
        :return:
        """
        employee_model = DataConverter.from_employee_entity(employee_entity)
        employee_model.save()
        employee_model.refresh_from_db()
        return DataConverter.to_employee_entity(employee_model)

    def employee_exists(self, employee_pk):
        """
        Implementation of abstract employee_exists function in EmployeeRepo port
        :param employee_pk:
        :return:
        """
        try:
            employee = Employee.objects.get(pk=employee_pk)
            return DataConverter.to_employee_entity(employee)
        except Employee.DoesNotExist:
            return None

    def delete(self, employee_pk: int):
        try:
            employee = Employee.objects.get(pk=employee_pk)
            employee.delete()
            employee_entity = DataConverter.to_employee_entity(employee)
            return employee_entity
        except Employee.DoesNotExist:
            raise Employee.DoesNotExist


