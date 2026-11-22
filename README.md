# 🦎 ChamaleonBase

**ChamaleonBase** es una herramienta de línea de comandos (CLI) rápida y sencilla desarrollada en Python para convertir datos entre diferentes sistemas de numeración y codificaciones de texto utilizando `bytes` como representación intermedia.

## ✨ Características

* **Conversión bidireccional** entre 5 formatos distintos:
  * **Decimal (`dec`)**
  * **Hexadecimal (`hex`)** (soporta prefijo `0x` y espacios)
  * **Binario (`bin`)** (soporta prefijo `0b` y espacios)
  * **ASCII (`ascii`)**
  * **Base64 (`base64`)**
* **Arquitectura limpia:** Desacopla la decodificación y codificación mediante tablas de despacho, facilitando agregar nuevos formatos en el futuro.
* **Salida enriquecida:** Utiliza la librería `rich` para una mejor presentación en terminal.
* **Validación de argumentos:** Previene combinaciones inválidas de entrada/salida y captura errores de formato de manera amigable.

---

## 📋 Requisitos

* **Python 3.9+** (requerido por el uso del método `.removeprefix()`).
* Librería **[Rich](https://github.com/Textualize/rich)** para la salida en consola.

---

## 🚀 Instalación

1. Clona o descarga este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/Fabric047/ChamaleonBase.git
   cd ChamaleonBase
   ```

2. Instala la dependencia necesaria:
   ```bash
   pip install rich
   ```

---

## 💻 Uso

La sintaxis general requiere especificar **un formato de origen** y **un formato de destino**:

```bash
python chamaleon_base.py --<origen> <VALOR> --to-<destino>
```
*(Nota: Reemplaza `chamaleon_base.py` por el nombre real de tu archivo).*

### Opciones disponibles

| Formato | Flag de Origen (Entrada) | Flag de Destino (Salida) |
| :--- | :--- | :--- |
| **Decimal** | `--dec <VALOR>` | `--to-dec` |
| **Hexadecimal** | `--hex <VALOR>` | `--to-hex` |
| **Binario** | `--bin <VALOR>` | `--to-bin` |
| **ASCII** | `--ascii <VALOR>` | `--to-ascii` |
| **Base64** | `--base64 <VALOR>` | `--to-base64` |

### Ejemplos prácticos

**1. Convertir texto ASCII a Hexadecimal:**
```bash
python chamaleon_base.py --ascii "Hola" --to-hex
# Salida: 486f6c61
```

**2. Convertir Hexadecimal (con prefijo y espacios) a Base64:**
```bash
python chamaleon_base.py --hex "0x48 6f 6c 61" --to-base64
# Salida: SG9sYQ==
```

**3. Convertir Binario a Decimal:**
```bash
python chamaleon_base.py --bin "0b11111111" --to-dec
# Salida: 255
```

**4. Convertir Base64 a ASCII:**
```bash
python chamaleon_base.py --base64 "SG9sYSBNdW5kbw==" --to-ascii
# Salida: Hola Mundo
```

**5. Ver la ayuda del programa:**
```bash
python chamaleon_base.py --help
```

---

## 🛠️ Cómo funciona internamente

El flujo de conversión sigue un patrón de **hub central en `bytes`** en orden *Big-Endian*:

```text
[Entrada] ──(Decoder)──▶ [bytes] ──(Encoder)──▶ [Salida]
```

Esto evita tener que programar $N \times (N-1)$ funciones de conversión directa, reduciendo la complejidad a solo $N$ decodificadores y $N$ codificadores.

---

## 📄 Licencia

Este proyecto es de uso libre. Siéntete libre de modificarlo y adaptarlo a tus necesidades.