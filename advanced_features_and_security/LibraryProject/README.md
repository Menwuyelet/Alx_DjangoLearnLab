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

# Security measures

## Security Settings to Configure

- set DEBUG = FALSE
- set SECURE_BROWSER_XSS_FILTER = TRUE to enable Enable XSS filter in browsers
- set X_FRAME_OPTIONS = 'DENY'
- set SECURE_CONTENT_TYPE_NOSNIFF = TRUE to Prevent browsers from interpreting files as a different MIME type
- CSRF_COOKIE_SECURE = True to Ensure cookies are sent over HTTPS only.
- SESSION_COOKIE_SECURE = True to Ensure cookies are sent over HTTPS only.

## Forms
- All forms include `{% csrf_token %}` to protect against CSRF attacks.

## Data Access
- Uses Django ORM to prevent SQL injection.
- User inputs are validated and sanitized using Django forms.

## Content Security Policy (CSP)
- used CSP manually 

# Security Review Report

## HTTPS Support
- **SECURE_SSL_REDIRECT:** All non-HTTPS requests are redirected to HTTPS.
- **HSTS:** Enforced for 1 year, includes subdomains, and allows preloading.

## Secure Cookies
- **SESSION_COOKIE_SECURE:** Ensures session cookies are only sent over HTTPS.
- **CSRF_COOKIE_SECURE:** Ensures CSRF cookies are only sent over HTTPS.

## Secure Headers
- **X_FRAME_OPTIONS:** Prevents clickjacking.
- **SECURE_CONTENT_TYPE_NOSNIFF:** Prevents MIME sniffing.
- **SECURE_BROWSER_XSS_FILTER:** Enables XSS filtering.