import logging

logger = logging.getLogger("uvicorn.error")


def send_reset_email(to_email: str, reset_link: str) -> None:
    # DEV ONLY: prints the link in the terminal.
    # In production, plug in SMTP / SendGrid / AWS SES here.
    logger.info("Password reset link for %s -> %s", to_email, reset_link)


"""1. Import logging
Imports Python's built-in logging module, which lets the application record messages, warnings, and errors.
2. Create a logger
Creates a logger named uvicorn.error, which is associated with Uvicorn's logging configuration.
This allows the application to write messages to the terminal or configured log destination.
3. Define the function
The function accepts two values:
- to_email: The email address of the user requesting a password reset.
- reset_link: The link the user can open to reset their password.
The -> None annotation means the function is not intended to return a value.
4. Record the reset link
The function writes an informational log message containing the user's email address and password reset link.
The %s placeholders are replaced by the supplied values when the log message is formatted.
For example, the terminal might show a message like:
Password reset link for user@example.com -> https://example.com/reset?token=abc123
This lets a developer test the password-reset workflow without configuring an email service.
5. Why does the comment say DEV ONLY?
In development, printing the link in the terminal is convenient. In production, the application should send the link through an actual email service, such as SMTP, SendGrid, or Amazon SES.
Important security point: A password reset link contains a sensitive token. Logging it can allow anyone with access to the logs to reset the user's password. Production logs should never expose reset tokens or complete reset links.
In simple terms, this function is currently a placeholder for a real email-sending service."""


"""
Yes, it can work by changing only this file, provided your existing project already generates the reset link and calls send_reset_email() correctly.

You would need to:

Replace the logging with SMTP email-sending logic.

Configure SMTP credentials, preferably through environment variables.

Ensure the existing dependencies and configuration support it."""
