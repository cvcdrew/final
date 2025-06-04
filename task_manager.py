{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMI93hTbufRpQdBRBXCXPfG",
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
        "<a href=\"https://colab.research.google.com/github/cvcdrew/final/blob/main/task_manager.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "txOtAOR2Z1aT"
      },
      "outputs": [],
      "source": [
        "def display_menu():\n",
        "    \"\"\"\n",
        "    Display menu options - use Week 3 formatting techniques only\n",
        "\n",
        "    >>> display_menu()  # doctest: +SKIP\n",
        "    1. Add task\n",
        "    2. List tasks\n",
        "    3. Remove task\n",
        "    4. Quit\n",
        "\n",
        "    >>> display_menu()  # doctest: +SKIP\n",
        "    1. Add task\n",
        "    2. List tasks\n",
        "    3. Remove task\n",
        "    4. Quit\n",
        "    \"\"\"\n",
        "    print(\"1. Add task\")\n",
        "    print(\"2. List tasks\")\n",
        "    print(\"3. Remove task\")\n",
        "    print(\"4. Quit\")\n",
        "\n",
        "def get_user_choice():\n",
        "    \"\"\"\n",
        "    Get and validate user choice - Week 6 input validation style\n",
        "\n",
        "    >>> # Manual test required, so skipping\n",
        "    >>> # get_user_choice()  # doctest: +SKIP\n",
        "    >>> # get_user_choice()  # doctest: +SKIP\n",
        "    \"\"\"\n",
        "    while True:\n",
        "        choice = input(\"Enter your choice (1-4): \").strip()\n",
        "        if choice in ['1', '2', '3', '4']:\n",
        "            return int(choice)\n",
        "        else:\n",
        "            print(\"Invalid choice. Please enter a number between 1 and 4.\")\n",
        "\n",
        "def main():\n",
        "    \"\"\"Main program loop - Week 5 loop patterns only\"\"\"\n",
        "    while True:\n",
        "        display_menu()\n",
        "        user_choice = get_user_choice()\n",
        "        if user_choice == 1:\n",
        "            print(\"Add task selected\")  # Placeholder\n",
        "        elif user_choice == 2:\n",
        "            print(\"List tasks selected\")  # Placeholder\n",
        "        elif user_choice == 3:\n",
        "            print(\"Remove task selected\")  # Placeholder\n",
        "        else:  # user_choice == 4\n",
        "            print(\"Goodbye!\")\n",
        "            break\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    main()\n"
      ]
    }
  ]
}