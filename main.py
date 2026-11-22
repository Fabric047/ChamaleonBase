import sys
from rich import print

BASES = ("dec", "hex", "bin", "ascii", "base64")


# ---------- Decoders: texto de la base -> bytes ----------
def dec_a_bytes(valor: str) -> bytes:
    num = int(valor)
    longitud = max(1, (num.bit_length() + 7) // 8)
    return num.to_bytes(longitud, byteorder="big")

def hex_a_bytes(valor: str) -> bytes:
    clean_str = valor.removeprefix("0x").replace(" ", "")
    if len(clean_str) % 2 != 0:
        clean_str = "0" + clean_str
    return bytes.fromhex(clean_str)

def bin_a_bytes(valor: str) -> bytes:
    clean_str = valor.removeprefix("0b").replace(" ", "")
    longitud = max(1, (len(clean_str) + 7) // 8)
    return int(clean_str, 2).to_bytes(longitud, byteorder="big")

def ascii_a_bytes(valor: str) -> bytes:
    return valor.encode("ascii")

def base64_a_bytes(valor: str) -> bytes:
    import base64
    return base64.b64decode(valor)

# ---------- Encoders: bytes -> texto de la base ----------
def bytes_a_dec(datos: bytes) -> str:
    string = str(int.from_bytes(datos, byteorder="big"))
    return string

def bytes_a_hex(datos: bytes) -> str:
    string = datos.hex()
    return string

def bytes_a_bin(datos: bytes) -> str:
    string = "".join(f"{byte:08b}" for byte in datos)
    return string

def bytes_a_ascii(datos: bytes) -> str:
    string = datos.decode("ascii")
    return string

def bytes_a_base64(datos: bytes) -> str:
    import base64
    string = base64.b64encode(datos).decode("ascii")
    return string


# ---------- Tablas de despacho ----------
DECODERS = {
    "dec": dec_a_bytes,
    "hex": hex_a_bytes,
    "bin": bin_a_bytes,
    "ascii": ascii_a_bytes,
    "base64": base64_a_bytes,
}

ENCODERS = {
    "dec": bytes_a_dec,
    "hex": bytes_a_hex,
    "bin": bytes_a_bin,
    "ascii": bytes_a_ascii,
    "base64": bytes_a_base64,
}


def convertir(valor: str, origen: str, destino: str) -> str:
    return ENCODERS[destino](DECODERS[origen](valor))


def main():
    import argparse

    parser = argparse.ArgumentParser(prog="ChamaleonBase")

    grupo_origen = parser.add_mutually_exclusive_group(required=True)
    grupo_destino = parser.add_mutually_exclusive_group(required=True)

    for base in BASES:
        grupo_origen.add_argument(f"--{base}", metavar="VALOR")
        grupo_destino.add_argument(f"--to-{base}", dest=f"to_{base}", action="store_true")

    args = parser.parse_args()

    origen = next(b for b in BASES if getattr(args, b) is not None)
    destino = next(b for b in BASES if getattr(args, f"to_{b}"))

    try:
        print(convertir(getattr(args, origen), origen, destino))
    except ValueError as e:
        parser.error(f"valor inválido para {origen}: {e}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nSaliendo del programa...")
        sys.exit(0)