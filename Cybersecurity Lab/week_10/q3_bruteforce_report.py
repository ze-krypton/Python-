# Q3 - Brute Force Attack Report (Theory Only - No Code)

"""
BRUTE FORCE ATTACK REPORT
==========================

Objective:
To evaluate the security of the login mechanism against brute-force attacks.

Findings:
- The login page allowed multiple consecutive failed attempts without restriction.
- No account lockout or delay mechanism was observed.
- Error messages clearly indicated invalid credentials.
- No CAPTCHA or additional verification was triggered.

Risk Level: HIGH

Mitigation Strategies:
- Implement account lockout after limited failed login attempts.
- Add CAPTCHA or multi-factor authentication (MFA).
- Introduce rate limiting to slow down repeated login requests.
- Use generic error messages (e.g., "Invalid username or password").
- Monitor and log suspicious login activity.
- Encourage strong password policies.

Conclusion:
The login system lacks adequate protection against brute-force attacks.
Implementing the recommended controls will significantly improve security.
"""
