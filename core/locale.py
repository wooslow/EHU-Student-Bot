import json
import os


class I18N:
    def __init__(self):
        self.locales = {}
        self._load_locales()

    def _load_locales(self):
        """
        The _load_locales function is a helper function that loads all the locales from the core/localization folder.
        It returns a dictionary of locales, where each locale is another dictionary containing all the strings for that locale.

        :return: The locales dictionary
        """
        for locale_filename in os.listdir("core/localization"):
            if locale_filename.endswith(".json"):
                locale = locale_filename.replace(".json", "")
                with open(f"core/localization/{locale_filename}", encoding="UTF-8") as locale_file:
                    self.locales[locale] = json.load(locale_file)

        return self.locales

    def __getitem__(self, language: str) -> dict[str, str]:
        return self.locales[language]