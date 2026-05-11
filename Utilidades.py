import re
import random
import string
from datetime import datetime

# --- FUNCIONES DE VALIDACIÓN ---

def validar_email(email):
    """Verifica el formato de un correo electrónico[cite: 29]."""
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(patron, email))

def validar_carne(carne):
    """Valida el formato de carné estudiantil (ej. 2026-001)[cite: 36]."""
    return bool(re.match(r'^\d{4}-\d{3}$', carne))

def validar_fecha(fecha_str):
    """Valida una fecha en formato DD/MM/AAAA[cite: 39]."""
    try:
        datetime.strptime(fecha_str, '%d/%m/%Y')
        return True
    except ValueError:
        return False

def formatear_dpi(dpi_raw):
    """Convierte un DPI de 13 dígitos a formato legible[cite: 41]."""
    if len(dpi_raw) != 13: return "DPI Inválido"
    return f"{dpi_raw[:4]} {dpi_raw[4:9]} {dpi_raw[9:]}"

# --- FUNCIONES MATEMÁTICAS ---

def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal[cite: 30].
    Fórmula: $$IMC = \frac{peso}{altura^2}$$
    """
    if altura <= 0: return 0
    return round(peso / (altura ** 2), 2)

def quetzales_a_dolares(monto, tasa=7.85):
    """Convierte moneda local a dólares[cite: 31]."""
    return round(monto / tasa, 2)

def es_primo(n):
    """Verifica si un número es primo[cite: 33]."""
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def calcular_factorial(n):
    """Calcula el factorial de un número entero[cite: 34]."""
    if n < 0: return None
    return 1 if n == 0 else n * calcular_factorial(n - 1)

def calcular_descuento(precio, porcentaje):
    """Calcula el precio final con descuento aplicado[cite: 37]."""
    return precio - (precio * (porcentaje / 100))

def calcular_promedio(lista):
    """Calcula el promedio de un arreglo de números[cite: 39]."""
    return sum(lista) / len(lista) if lista else 0

def mayor_menor(lista):
    """Encuentra el valor más alto y más bajo de un arreglo[cite: 40]."""
    if not lista: return None, None
    return max(lista), min(lista)

# --- FUNCIONES DE TEXTO Y UTILIDADES ---

def contar_vocales(texto):
    """Cuenta las vocales en una cadena[cite: 32]."""
    return sum(1 for c in texto.lower() if c in "aeiouáéíóú")

def invertir_cadena(texto):
    """Invierte el orden de los caracteres[cite: 38]."""
    return texto[::-1]

def generar_password(longitud=12):
    """Genera una contraseña aleatoria de longitud N[cite: 39]."""
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longitud))

def celsius_a_fahrenheit(c):
    """Convierte grados Celsius a Fahrenheit[cite: 35]."""
    return (c * 9/5) + 32

# --- PRUEBAS DE EJECUCIÓN ---
if __name__ == "__main__":
    print(f"Test IMC: {calcular_imc(75, 1.80)}") 
    print(f"Test Primo: {es_primo(17)}")
    print(f"Test DPI: {formatear_dpi('2000123450101')}")