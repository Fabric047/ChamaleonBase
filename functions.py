import argparse
import stat
from datetime import datetime
from pathlib import Path
import sys
from rich import print


def main():
    parser = argparse.ArgumentParser(description='Herramienta que trata de reemplazar el comando "ls"')
    subparser = parser.add_subparsers(dest='command', help='Sub-comandos disponibles')

    # Comando show
    command_show = subparser.add_parser('show', help='Mostrar todos los archivos')
    command_show.add_argument('-d','--detailed', action='store_true', help='Ver archivos en detalle')
    command_show.add_argument('-S', '--size', type=str.lower,choices=['kb','mb','gb'],
                              help="Sin esta flag, el tamano de los archivos se mostrara en kb. Puedes escribir mb o gb (Ej. -S mb). Por default, el tamano de archivos se mostrara en kb, mb y gb.")
    command_show.add_argument('-s', '--sort', type=str,  default="name",help='Ordenar elementos por: name, size, date')
    command_show.add_argument('-r', '--reverse', action='store_true', help='Invertir orden (descendente)')
    command_show.add_argument('-L','--max-depth', type=int, default=2, help='Limitar la profundidad de recursión al escanear carpetas')
    command_show.add_argument('-l','--limit', type=int, help="Mostrar solo N cantidad de archivos (Ej. combinar con --sort size para ver el 'Top 10 archivos más grandes')")


    # Comando find
    command_find = subparser.add_parser('find', help='Encontrar un archivo rapidamente')
    command_find.add_argument('-n','--name', type=str, help="Buscar por nombre")
    command_find.add_argument('-s','--size', type=str, help="Buscar por tamano (en kb)")
    command_find.add_argument('-d','--date', type=str, help="Buscar por fecha de modificacion (year-month-day)")
    command_find.add_argument('-e','--extension', type=str, help="Buscar por extension (Ej. txt, mp3, mp4, csv, etc)")

    args = parser.parse_args()

    if args.command == 'show':
        # function_show(args)
        pass
    elif args.command == 'find':
        # function_find(args)
        pass
    else:
        parser.print_help()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nSaliendo del programa...")
        sys.exit(0)