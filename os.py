import os

def get_facts():

    u = os.uname()
    info = {
        "SYSNAME": u.sysname,
        "KERNEL": u.release,
        "ARCH": u.machine,
        "RELEASE_OS": u.version,
        "HOSTNAME": u.nodename,
}

    with open("system.env", "w") as f:
        for k, v in info.items():
            f.write(f"{k}={v}\n")

if __name__ == "__main__":
    get_facts()