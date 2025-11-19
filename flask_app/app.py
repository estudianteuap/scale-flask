from flask import Flask
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    # Muestra el ID del contenedor para verificar el balanceo de carga
    #container_id = os.uname()[1]
    current_date = datetime.now().strftime("%Y-%m-%d")

    return f"Hello, World! Cristhiam Montes {current_date}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)