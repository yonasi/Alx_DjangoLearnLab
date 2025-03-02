
1. Custom Permissions:
   - defined in bookshelf/models.py within the Book model's Meta class.
   - Permissions types: can_view, can_create, can_edit, can_delete.

2. Groups:
   - Created via Django's admin interface
   - Groups: Editors, Viewers, Admins.

3. Permission Assignments:
   - Editors: Assigned can_create and can_edit permissions.
   - Viewers: Assigned can_view permission.
   - Admins: Assigned all permissions (can_view, can_create, can_edit, can_delete).

4. View Protection:
   - Views in bookshelf/views.py are protected using the @permission_required decorator.

5. Testing:
   - Create test users through the admin interface.
   - Assign users to the created groups.
   - Log in as each user and test access to different parts of the application to verify permission enforcement.
