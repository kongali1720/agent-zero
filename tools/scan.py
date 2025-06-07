import subprocess

def port_scan(ip):
    try:
        result = subprocess.check_output(['nmap', '-F', ip], stderr=subprocess.STDOUT, text=True)
        return result
    except Exception as e:
        return f"[x] Nmap Error: {e}"
