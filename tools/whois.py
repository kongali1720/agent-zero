import subprocess

def lookup(domain):
    try:
        output = subprocess.check_output(['whois', domain], stderr=subprocess.STDOUT, text=True)
        return output
    except Exception as e:
        return f"[x] WHOIS Error: {e}"
