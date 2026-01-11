class ChaiUtils:

    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]
    
raw = " Water , milk , ginger , honey "
clean = ChaiUtils.clean_ingredients(raw)
print(clean)

