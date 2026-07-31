
# Secure Coding Review Report

## Submitted By

M MOHAMED ANAS

---

# Objective

To identify security vulnerabilities in an application and provide secure coding recommendations.

---

# Application Reviewed

Python Login Authentication System

---

# Vulnerabilities

## 1. Plain Text Password Storage

Risk:
If the source code is leaked, all passwords become visible.

Severity:
High

Recommendation:
Store passwords using hashing algorithms.

---

## 2. No Password Encryption

Risk:
Attackers can easily steal credentials.

Severity:
High

Recommendation:
Use SHA-256, bcrypt or Argon2.

---

## 3. No Input Validation

Risk:
Unexpected inputs may affect application behavior.

Severity:
Medium

Recommendation:
Validate all user inputs.

---

## 4. No Logging

Risk:
Failed login attempts cannot be monitored.

Severity:
Medium

Recommendation:
Maintain authentication logs.

---

## 5. No Account Lockout

Risk:
Allows brute-force attacks.

Severity:
High

Recommendation:
Lock the account after multiple failed attempts.

---

# Security Best Practices

- Use strong passwords.
- Enable Multi-Factor Authentication.
- Never store passwords in plain text.
- Validate user input.
- Use HTTPS.
- Perform regular security audits.

---

# Conclusion

The insecure login system contains several security weaknesses. The secure version follows better authentication practices and significantly improves application security.
