"""
Gilman Mail — Cliente de envio de correos
==========================================
Uso (con la contrasena como argumento):
    python scripts/send.py ahora <password> <to> <subject> <body>
    python scripts/send.py programar <password> <to> <subject> <body> <YYYY-MM-DDTHH:MM>
    python scripts/send.py listar <password>
    python scripts/send.py eliminar <password> <schedule_id>

Uso alternativo (contrasena en la variable de entorno GILMAN_PASSWORD;
el argumento password se omite y los demas argumentos se desplazan):
    python scripts/send.py ahora <to> <subject> <body>
    python scripts/send.py programar <to> <subject> <body> <YYYY-MM-DDTHH:MM>
    python scripts/send.py listar
    python scripts/send.py eliminar <schedule_id>

Requiere: pip install requests
"""

import os
import sys
import requests
from datetime import datetime

BASE = "https://admin-correo.gilman.pro"
FROM = "admin@gilman.pro"

session = requests.Session()
session.verify = False


def login(password: str):
    r = session.post(f"{BASE}/login", data={"username": "admin@gilman.pro", "password": password})
    if r.status_code != 200:
        raise RuntimeError(f"Login fallido: {r.status_code}")


def send_now(to: str, subject: str, body: str, password: str, from_email: str = FROM) -> bool:
    login(password)
    r = session.post(f"{BASE}/transactional/send-test", data={
        "from_email": from_email, "to_email": to, "subject": subject, "body": body,
    })
    return r.status_code == 303


def schedule(to: str, subject: str, body: str, when: str, password: str, from_email: str = FROM) -> bool:
    login(password)
    r = session.post(f"{BASE}/marketing/schedule", data={
        "from_email": from_email, "to": to, "subject": subject, "body": body, "scheduled_at": when,
    })
    return r.status_code == 303


def list_schedules(password: str) -> list:
    login(password)
    r = session.get(f"{BASE}/marketing")
    schedules = []
    for line in r.text.split("\n"):
        if "schedule_id" in line and "value=" in line:
            import re
            sid = re.search(r'value="(\w+)"', line)
            if sid:
                schedules.append(sid.group(1))
    return schedules


def delete_schedule(schedule_id: str, password: str) -> bool:
    login(password)
    r = session.post(f"{BASE}/marketing/schedule/delete", data={"schedule_id": schedule_id})
    return r.status_code == 303


if __name__ == "__main__":
    # Si GILMAN_PASSWORD esta definida, el password posicional es opcional
    # y los demas argumentos se desplazan un puesto a la izquierda.
    env_password = os.environ.get("GILMAN_PASSWORD")
    if len(sys.argv) < (2 if env_password else 3):
        print("Uso: python send.py <ahora|programar|listar|eliminar> [password] [args...]")
        print("     (o define GILMAN_PASSWORD en el entorno y omite el password)")
        sys.exit(1)

    cmd = sys.argv[1]
    if env_password:
        password, args = env_password, sys.argv[2:]
    else:
        password, args = sys.argv[2], sys.argv[3:]

    if cmd == "ahora":
        to, subject, body = args[0], args[1], args[2]
        ok = send_now(to, subject, body, password)
        print("Enviado" if ok else "Error")

    elif cmd == "programar":
        to, subject, body, when = args[0], args[1], args[2], args[3]
        ok = schedule(to, subject, body, when, password)
        print("Programado" if ok else "Error")

    elif cmd == "listar":
        scheds = list_schedules(password)
        print(f"{len(scheds)} programaciones: {scheds}")

    elif cmd == "eliminar":
        ok = delete_schedule(args[0], password)
        print("Eliminado" if ok else "Error")

    else:
        print(f"Comando desconocido: {cmd}")
