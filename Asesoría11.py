{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Asesoría11.ipynb",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/kevinrdf/CLASES/blob/main/Asesor%C3%ADa11.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "zTq2LfbTQak3"
      },
      "source": [
        "# Diccionarios"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "4BBoiRzUQzsQ"
      },
      "source": [
        "Diseñee un programa que al comienzo carge la tabla de precios de productos de un quiosco en un diccionario y, luego, que SIEMPRE le pregunte al usuario 3 opciones:\n",
        "1. Si desea añadir un nuevo item al diccionario\n",
        "2. Que le brinde el costo de un producto.\n",
        "3. Que imprima todos los productos y precios del quiosco.\n",
        "\n",
        "- Cuando añade un nuevo item al diccionario tiene que preguntar al usuario el nombre y costo del producto.\n",
        "- Cuando le brinda el costo del producto a un usuario, el usuario tiene que ingresar el nombre del producto; si no se encuentra el producto debe indicar que no cuentan con el producto en el quiosco. \n",
        "- Si ingresa una opción debe indicarlo.\n",
        "\n",
        "| Producto | Precio |\n",
        "| -------- | ------ |\n",
        "| Queque | 1.5 |\n",
        "| Empanada | 3.5 |\n",
        "| Gaseosa | 2.0 |\n",
        "\n",
        "\n",
        "```\n",
        "Bienvenidos al Quiosco !\n",
        "Eliga una opcion :\n",
        "1. Ingresar un nuevo item .\n",
        "2. Averiguar el costo de un item .\n",
        "3. Imprimir todos los items con su precio .\n",
        "```"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "X6pzFh_eQSQy"
      },
      "source": [
        "# Variables globales\n",
        "bienvenida = \"\\n\\n¡Bienvenidos al Quiosco!\"\n",
        "opciones = \"Eliga una opcion :\\n 1. Ingresar un nuevo item.\\n 2. Averiguar el costo de un item.\\n 3. Imprimir todos los items con su precio.\\nIngrese -1 para terminar el programa\"\n",
        "error = '\\nOpción inválida'\n",
        "\n",
        "# Estructura del diccionario: producto: precio\n",
        "items = {'Queque': 1.5, 'Empanada': 3.5, 'Gaseosa': 2}\n",
        "\n",
        "\n",
        "# Funciones\n",
        "def ingresar_opcion():\n",
        "  print(bienvenida)\n",
        "  print(opciones)\n",
        "  op = int(input('\\nIngrese la opción deseada: '))\n",
        "  return op\n",
        "\n",
        "\n",
        "def ingresar_item():\n",
        "  # Ingresar datos\n",
        "  nombre = input('Ingrese el nombre del producto: ')\n",
        "  precio = float(input('Ingrese el precio del producto: '))\n",
        "  # Añadir al diccionario\n",
        "  items[nombre] = precio\n",
        "\n",
        "\n",
        "def averiguar_costo():\n",
        "  # Ingresar datos\n",
        "  nombre = input('Ingrese el nombre del producto: ')\n",
        "  # Verificar si existe e imprimir el precio\n",
        "  if nombre in items:\n",
        "    print(nombre, ': ', items[nombre])\n",
        "  else:\n",
        "    print('\\nProducto no encontrado.')\n",
        "\n",
        "\n",
        "def imprimir_items():\n",
        "  for item in items:\n",
        "    print(item, ': ', items[item])\n",
        "\n",
        "\n",
        "\n",
        "# Programa\n",
        "opcion = 0\n",
        "while opcion != -1:\n",
        "  opcion = ingresar_opcion()\n",
        "  if opcion == 1:\n",
        "    # Ingresar un item\n",
        "    ingresar_item()\n",
        "  elif opcion == 2:\n",
        "    # Averiguar el costo\n",
        "    averiguar_costo()\n",
        "  elif opcion == 3:\n",
        "    # Imprimir todos los items y sus costos\n",
        "    imprimir_items()\n",
        "  else:\n",
        "    print(error)\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "V1Q7jcugQT-g"
      },
      "source": [
        "# Otras dudas"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "62WIdBq9OkMl",
        "outputId": "cb4f3aa3-e143-41eb-e630-0d4a79f57d8f"
      },
      "source": [
        "a = [[1, 2], [2, 3]]\n",
        "b = a\n",
        "print(b)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[1, 2], [2, 3]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8fNBSQZIPdmM",
        "outputId": "85af3d01-5b69-48f6-ab25-85354ad99817"
      },
      "source": [
        "letra = input('Ingrese una letra: ')\n",
        "# Para utilizar mayúsculas\n",
        "letra = letra.upper()\n",
        "# Número de columna en base al ascii de 'A'\n",
        "val = ord(letra) - 65\n",
        "print(val)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Ingrese una letra: D\n",
            "3\n"
          ]
        }
      ]
    }
  ]
}