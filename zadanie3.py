zakupy = {"jajka": "sztuki",
          "ziemniaki": "kg",
          "pomarańcze": "sztuki",
          "mąka": "opakowania"}
sztuki = {klucz: wartosc for klucz, wartosc in zakupy.items() if wartosc == "sztuki"}
print(sztuki)