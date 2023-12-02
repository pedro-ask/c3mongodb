import sys
import subprocess

def refresh_application():
    python = sys.executable
    subprocess.run([python] + sys.argv)