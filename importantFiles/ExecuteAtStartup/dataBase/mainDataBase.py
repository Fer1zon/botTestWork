from .createTable import createAdminTable, createUserTable
from .updateFields import updateFields 








def mainDataBaseFunction():
    createUserTable()
    createAdminTable()
    updateFields()