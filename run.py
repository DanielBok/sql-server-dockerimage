import subprocess
import sys
import time


def build():
    tag = image_tag()
    execute("docker", "image", "build", "--tag", f"danielbok/sql-server:{tag}", ".")


def push():
    current = f"danielbok/sql-server:{image_tag()}"
    latest = "danielbok/sql-server:latest"
    execute("docker", "image", "tag", current, latest)
    execute("docker", "image", "push", current)
    execute("docker", "image", "push", latest)


def image_tag():
    with open("Dockerfile") as f:
        line = f.readline()

    return line.strip().split(":")[-1]


def execute(*commands: str):
    print(' '.join(commands))
    process = subprocess.Popen(commands, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    while True:
        output = process.stdout.readline().decode('utf-8')
        if process.poll() is not None:
            break
        if output:
            print(output)
        time.sleep(0.5)


if __name__ == "__main__":
    cmd = sys.argv[1].strip()
    if cmd == "build":
        build()
    elif cmd == "push":
        push()
    else:
        raise Exception(f"Unknown command: {cmd}")