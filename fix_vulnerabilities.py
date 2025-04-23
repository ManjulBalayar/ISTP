#!/usr/bin/env python
"""
Script to automatically fix vulnerabilities in dependencies.
Generates an updated requirements file with recommended fixed versions.
"""

import subprocess
import json
import os
import sys
from packaging import version

def get_vulnerability_data():
    """Run safety check and return parsed vulnerability data"""
    print("Scanning for vulnerabilities...")
    result = subprocess.run(
        ['safety', 'check', '--json', '-r', 'requirements.txt'],
        capture_output=True,
        text=True
    )
    
    if result.stdout.strip():
        try:
            return json.loads(result.stdout)
        except json.JSONDecodeError:
            print("Error: Could not parse safety output")
            print(result.stdout)
            return []
    
    return []

def get_latest_version(package):
    """Get the latest version of a package from PyPI"""
    try:
        result = subprocess.run(
            ['pip', 'index', 'versions', package],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            lines = result.stdout.strip().split('\n')
            for line in lines:
                if "Available versions:" in line:
                    versions_str = line.split("Available versions:")[1].strip()
                    versions = [v.strip().strip(',') for v in versions_str.split()]
                    
                    # Filter out pre-release versions
                    stable_versions = [v for v in versions if not ('a' in v or 'b' in v or 'rc' in v)]
                    
                    if stable_versions:
                        return stable_versions[0]  # Return the latest stable version
        
        # Fallback to pip search if the above method fails
        result = subprocess.run(
            ['pip', 'search', package],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            for line in result.stdout.strip().split('\n'):
                if line.startswith(package + ' '):
                    parts = line.split()
                    if len(parts) >= 2:
                        return parts[1].strip('()')
    
    except Exception as e:
        print(f"Error getting latest version for {package}: {str(e)}")
    
    return None

def parse_requirements(file_path='requirements.txt'):
    """Parse requirements.txt into a dictionary of package: version"""
    requirements = {}
    
    if not os.path.exists(file_path):
        return requirements
    
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                # Handle various formats like package==1.0.0, package>=1.0.0, etc.
                if '==' in line:
                    package, ver = line.split('==', 1)
                    requirements[package.strip()] = ver.strip()
                elif '>=' in line:
                    package, ver = line.split('>=', 1)
                    requirements[package.strip()] = '>=' + ver.strip()
                elif '>' in line:
                    package, ver = line.split('>', 1)
                    requirements[package.strip()] = '>' + ver.strip()
                elif '<=' in line:
                    package, ver = line.split('<=', 1)
                    requirements[package.strip()] = '<=' + ver.strip()
                elif '<' in line:
                    package, ver = line.split('<', 1)
                    requirements[package.strip()] = '<' + ver.strip()
                elif '~=' in line:
                    package, ver = line.split('~=', 1)
                    requirements[package.strip()] = '~=' + ver.strip()
                else:
                    # Just the package name without version
                    requirements[line.strip()] = None
    
    return requirements

def generate_fixed_requirements(vulnerabilities):
    """Generate updated requirements with fixed versions"""
    current_requirements = parse_requirements()
    fixed_requirements = current_requirements.copy()
    
    fixed_packages = set()
    
    for vuln in vulnerabilities:
        package = vuln['package_name']
        fixed_packages.add(package)
        
        # Try to get the latest version
        latest_version = get_latest_version(package)
        
        if latest_version:
            fixed_requirements[package] = '==' + latest_version
            print(f"Fixing {package}: {current_requirements.get(package)} -> {latest_version}")
        else:
            print(f"Warning: Couldn't determine latest version for {package}")
    
    # Generate new requirements.txt content
    content = []
    for package, version_spec in fixed_requirements.items():
        if version_spec:
            content.append(f"{package}{version_spec}")
        else:
            content.append(package)
    
    # Write to fixed_requirements.txt
    with open('fixed_requirements.txt', 'w') as f:
        f.write('\n'.join(content))
    
    return fixed_packages

def main():
    # Install safety if not already installed
    try:
        import safety
    except ImportError:
        print("Installing safety...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'safety', 'packaging'])
    
    # Get vulnerability data
    vulnerabilities = get_vulnerability_data()
    
    if not vulnerabilities:
        print("No vulnerabilities found!")
        return 0
    
    print(f"Found {len(vulnerabilities)} vulnerabilities.")
    
    # Generate fixed requirements
    fixed_packages = generate_fixed_requirements(vulnerabilities)
    
    print("\nRecommendations:")
    print(f"1. Review the generated fixed_requirements.txt file")
    print(f"2. Test your application with the updated dependencies before deploying")
    print(f"3. After testing, replace your requirements.txt with fixed_requirements.txt")
    print("\nFixed packages:")
    for package in fixed_packages:
        print(f"- {package}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 