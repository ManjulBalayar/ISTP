#!/usr/bin/env python
"""
Security check script to run before deployment.
Checks for dependency vulnerabilities using Safety.
"""

import os
import sys
import subprocess
import json
from datetime import datetime

def run_safety_check():
    print("Running Safety check on dependencies...")
    try:
        # Run safety check and get JSON output
        result = subprocess.run(
            ['safety', 'check', '--json', '-r', 'requirements.txt'], 
            capture_output=True, 
            text=True
        )
        
        if result.returncode != 0:
            # Parse JSON output to get vulnerability details
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
        
        print("No security vulnerabilities found!")
        return True
    
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
        if result.returncode != 0:
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
        
        print("No code security issues found!")
        return True
    
    except Exception as e:
        print(f"Error running code security check: {str(e)}")
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
        print("Security issues found. Please fix before deployment.")
        sys.exit(1)
    
    print("All security checks passed!")
    sys.exit(0) 