#!/usr/bin/env python
"""
Security check script to run before deployment.
Checks for dependency vulnerabilities using Safety.
"""

import os
import sys
import subprocess
import json
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def run_safety_check():
    print("Running Safety check on dependencies...")
    try:
        # Run safety check and get JSON output
        result = subprocess.run(
            ['safety', 'check', '--json', '-r', 'requirements.txt'], 
            capture_output=True, 
            text=True
        )
        
        # Parse JSON output if there's any output
        if result.stdout.strip():
            try:
                vulnerabilities = json.loads(result.stdout)
                
                # Create report
                report = f"Security Scan Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                report += f"Found {len(vulnerabilities)} vulnerabilities:\n\n"
                
                for vuln in vulnerabilities:
                    report += f"Package: {vuln['package_name']}\n"
                    report += f"Installed version: {vuln['installed_version']}\n"
                    report += f"Vulnerable versions: {vuln['vulnerable_spec']}\n"
                    report += f"Description: {vuln['advisory']}\n"
                    report += f"CVE: {vuln.get('cve', 'N/A')}\n"
                    report += f"More info: {vuln.get('more_info_url', 'N/A')}\n"
                    report += "-" * 50 + "\n"
                
                # Save report to file
                with open('security_report.txt', 'w') as f:
                    f.write(report)
                    
                print(f"Found {len(vulnerabilities)} vulnerabilities. See security_report.txt for details.")
                return False
            except json.JSONDecodeError:
                # Safety might not always return valid JSON
                print("Warning: Could not parse safety output as JSON.")
                print("Output:", result.stdout)
                # Don't fail the build for parsing errors
                return True
        
        # If returncode is 0, no vulnerabilities were found
        if result.returncode == 0:
            print("No security vulnerabilities found!")
            return True
        else:
            print(f"Safety check failed with exit code {result.returncode}")
            print("Output:", result.stdout)
            print("Error:", result.stderr)
            return False
    
    except Exception as e:
        print(f"Error running security check: {str(e)}")
        return False

def check_code_security():
    print("Running Bandit for code security analysis...")
    try:
        # Run bandit on project directory, excluding virtualenv
        result = subprocess.run(
            ['bandit', '-r', '.', '-x', './virt,./JupyterStuff', '-f', 'json'], 
            capture_output=True, 
            text=True
        )
        
        # Parse results
        try:
            if result.stdout.strip():
                output = json.loads(result.stdout)
                results = output.get('results', [])
                
                if results:
                    # Create report
                    report = f"Code Security Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                    report += f"Found {len(results)} security issues:\n\n"
                    
                    for issue in results:
                        report += f"File: {issue['filename']}\n"
                        report += f"Line: {issue['line_number']}\n"
                        report += f"Issue: {issue['issue_text']}\n"
                        report += f"Severity: {issue['issue_severity']}\n"
                        report += f"Confidence: {issue['issue_confidence']}\n"
                        report += f"Code: {issue['code']}\n"
                        report += "-" * 50 + "\n"
                    
                    # Save report to file
                    with open('code_security_report.txt', 'w') as f:
                        f.write(report)
                        
                    print(f"Found {len(results)} code security issues. See code_security_report.txt for details.")
                    return False
        except json.JSONDecodeError:
            print("Warning: Could not parse Bandit output as JSON")
            print("Output:", result.stdout)
            print("Error:", result.stderr)
            # Don't fail the build for parsing errors
            return True
        
        print("No code security issues found!")
        return True
    
    except Exception as e:
        print(f"Error running code security check: {str(e)}")
        return False

def send_security_alert(subject, message, recipients=None):
    """
    Send security alert email to specified recipients.
    
    Args:
        subject (str): Email subject
        message (str): Email body content
        recipients (list): List of email addresses to send to
    
    Returns:
        bool: Whether email was sent successfully
    """
    if not recipients:
        # Default recipients if none provided
        recipients = ["security@example.com"]
        
    # Get email configuration from environment variables
    smtp_server = os.environ.get("SECURITY_SMTP_SERVER", "smtp.gmail.com")
    smtp_port = int(os.environ.get("SECURITY_SMTP_PORT", "587"))
    smtp_username = os.environ.get("SECURITY_SMTP_USERNAME", "")
    smtp_password = os.environ.get("SECURITY_SMTP_PASSWORD", "")
    sender_email = os.environ.get("SECURITY_SENDER_EMAIL", smtp_username)
    
    # If credentials not configured, just print warning and return
    if not smtp_username or not smtp_password:
        print("Email notification skipped: SMTP credentials not configured")
        print("Set SECURITY_SMTP_USERNAME and SECURITY_SMTP_PASSWORD environment variables")
        return False
    
    # Create email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ", ".join(recipients)
    msg['Subject'] = subject
    
    # Add message body
    msg.attach(MIMEText(message, 'plain'))
    
    try:
        # Connect to SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        
        # Send email
        server.send_message(msg)
        server.quit()
        
        print(f"Security alert email sent to {', '.join(recipients)}")
        return True
    except Exception as e:
        print(f"Failed to send security alert email: {str(e)}")
        return False

if __name__ == "__main__":
    # Install security tools if not present
    try:
        import safety
        import bandit
    except ImportError:
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'safety', 'bandit'])
    
    deps_secure = run_safety_check()
    code_secure = check_code_security()
    
    if not deps_secure or not code_secure:
        # Create notification message
        subject = "SECURITY ALERT: Issues found in application"
        message = f"Security scan performed on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        
        if not deps_secure:
            message += "DEPENDENCY VULNERABILITIES FOUND\n"
            message += "Please check security_report.txt for details.\n\n"
        
        if not code_secure:
            message += "CODE SECURITY ISSUES FOUND\n"
            message += "Please check code_security_report.txt for details.\n\n"
        
        message += "Fix these issues before proceeding with deployment."
        
        # Get recipients from environment variable (comma-separated list)
        recipients_str = os.environ.get("SECURITY_ALERT_RECIPIENTS", "")
        recipients = [email.strip() for email in recipients_str.split(",")] if recipients_str else None
        
        # Send alert email
        send_security_alert(subject, message, recipients)
        
        print("Security issues found. Please fix before deployment.")
        sys.exit(1)
    
    print("All security checks passed!")
    sys.exit(0) 