import docker
client = docker.from_env()

import requests


def start(id):
    container = client.containers.get(id)
    container.start()
    output = container.exec_run("lspcie", tty=True, user="server", workdir="/home/server")
    out1 = output.output.decode('utf-8').replace("\n", "<br>")
    out2 = out1.replace("\r", "")
    return f"{out2}<br>EXITED({output.exit_code})"

def restart(id):
    container = client.containers.get(id)
    container.stop()
    return start(id)

def stop(id):
    container = client.containers.get(id)
    container.stop()
    return f"Container {container.short_id} stopped<br><br>EXITED(0)"

def kill(id):
    container = client.containers.get(id)
    container.kill()
    return f"Container {container.short_id} killed<br><br>EXITED(0)"