# Cookies

A cookie is a small piece of state that a server asks a user agent, commonly a browser, to store and send with later matching requests.

## Cookie Exchange

1. The server sends a `Set-Cookie` response header.
2. The browser stores the cookie subject to its attributes and policies.
3. On a later eligible request, the browser sends it in the `Cookie` request header.

Cookies commonly support session identifiers and user preferences. A cookie may contain a session identifier while the associated session data remains on the server.

## Cookie Attributes

| Attribute | Purpose |
|---|---|
| Expires / Max-Age | Sets persistence or lifetime |
| Domain | Controls eligible destination domains |
| Path | Restricts eligible request paths |
| Secure | Sends the cookie only over secure connections |
| HttpOnly | Prevents access through ordinary JavaScript APIs |
| SameSite | Restricts some cross-site cookie sending |

## Security Considerations

- Use HTTPS and the Secure attribute for sensitive cookies.
- Prefer HttpOnly for session identifiers that JavaScript does not need to access.
- Choose SameSite deliberately; it is not a complete replacement for CSRF protection.
- Avoid storing passwords or sensitive personal data directly in cookies.

## Key Takeaway

Cookies provide browser-managed state across requests. Their scope, lifetime and security attributes determine when they are stored and sent.
