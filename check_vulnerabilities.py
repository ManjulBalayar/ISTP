#!/usr/bin/env python
"""
Script to check for vulnerabilities in our dependencies.
"""

import subprocess
import sys
import json
import os

def check_dependencies():
    print("Checking for vulnerabilities in dependencies...")
    
    # Create a directory for vulnerability reports if it doesn't exist
    if not os.path.exists('security_reports'):
        os.makedirs('security_reports')
    
    # Run pip-audit to check for vulnerabilities
    result = subprocess.run(
        [sys.executable, '-m', 'pip_audit', '--requirement', 'requirements.txt', '--format', 'json'],
        capture_output=True,
        text=True
    )
    
    # Check if pip-audit found any vulnerabilities
    try:
        audit_data = json.loads(result.stdout)
        
        # Newer versions of pip-audit have a different output format
        if "dependencies" in audit_data:
            dependencies = audit_data["dependencies"]
            vulnerable_deps = []
            
            for dep in dependencies:
                if "vulns" in dep and dep["vulns"]:
                    vulnerable_deps.append({
                        "name": dep["name"],
                        "installed_version": dep["version"],
                        "vulnerabilities": dep["vulns"]
                    })
        else:
            # Handle older format or potential changes in structure
            vulnerable_deps = []
            for pkg_name, pkg_data in audit_data.items():
                if pkg_data.get("vulns"):
                    vulnerable_deps.append({
                        "name": pkg_name,
                        "installed_version": pkg_data.get("version", "unknown"),
                        "vulnerabilities": pkg_data["vulns"]
                    })
        
        if vulnerable_deps:
            print(f"Found {len(vulnerable_deps)} vulnerable dependencies!")
            
            # Write a detailed report
            with open('security_reports/dependency_vulnerabilities.json', 'w') as f:
                json.dump(vulnerable_deps, f, indent=2)
            
            # Print a summary
            print("\nVulnerable Dependencies:")
            for dep in vulnerable_deps:
                print(f"  - {dep['name']} {dep['installed_version']}")
                for vuln in dep['vulnerabilities']:
                    print(f"    - {vuln.get('id', 'Unknown')}: {vuln.get('description', 'No description')}")
                    print(f"      Fixed in: {vuln.get('fix_versions', ['Unknown'])}")
            
            print("\nRecommendations:")
            print("1. Update dependencies to their fixed versions")
            print("2. See the detailed report in security_reports/dependency_vulnerabilities.json")
            return False
        else:
            print("No vulnerabilities found in your dependencies!")
            return True
    
    except json.JSONDecodeError:
        print("Error parsing pip-audit output. Check if pip-audit is installed.")
        print(f"Output: {result.stdout}")
        return False

if __name__ == "__main__":
    # Ensure required tools are installed
    try:
        import pip_audit
    except ImportError:
        print("Installing pip-audit...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'pip-audit'])
    
    # Run the check
    secure = check_dependencies()
    
    if not secure:
        sys.exit(1)
    
    print("All dependencies are secure!")
    sys.exit(0) 