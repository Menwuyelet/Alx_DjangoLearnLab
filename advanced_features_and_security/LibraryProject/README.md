# Permissions and Groups Setup

## Custom Permissions

- **Book Model Permissions**:
  - `can_view`: Permission to view books
  - `can_create`: Permission to create books
  - `can_edit`: Permission to edit books
  - `can_delete`: Permission to delete books

## Groups and Permissions

- **Editors**:
  - Can `can_edit`
  - Can `can_create`

- **Viewers**:
  - Can `can_view`

- **Admins**:
  - Can `can_view`
  - Can `can_create`
  - Can `can_edit`
  - Can `can_delete`

## Views

- `view_book`: Requires `can_view`
- `edit_book`: Requires `can_edit`
- `create_book`: Requires `can_create`
- `delete_book`: Requires `can_delete`