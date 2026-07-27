from app.db.database import get_db
from fastapi import Depends
from sqlalchemy import select
from app.core.security import get_current_user
from app.db.models import Permission, RolePermission
def required_permission(permissions:list):
    print ("reached")
    def checker(user=Depends(get_current_user), db=Depends(get_db)):
        role_id = user.role_id
        for permission in permissions:
                stmt = select(RolePermission).where(RolePermission.role_id == role_id, RolePermission.permission_id == select(Permission.id).where(Permission.name == permission).scalar_subquery())
                result = db.execute(stmt).scalar()
                if result:
                    return True
        
        raise PermissionError(f"Role with id {role_id} does not have permission {permission}")  
    return checker