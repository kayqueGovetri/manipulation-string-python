class ExtractorArgumentsUrl:
    def __init__(self, url):
        if self.string_is_valid(url) and url.startswith("https://bytebank.com"):
            self.url = url.lower()
        else:
            raise LookupError("Invalid url!")

    @staticmethod
    def string_is_valid(url):
        if url:
            return True
        else:
            return False

    def extract_arguments(self, source_currency, destination_currency):

        source_currency_search = source_currency.lower()
        destination_currency_search = destination_currency.lower()

        initial_target_currency_index = self.finds_initial_index(destination_currency_search)
        final_target_currency_index = self.url.find("&valor=")

        final_origin_currency_index = self.url.find("&")
        initial_origin_currency_index = self.finds_initial_index(source_currency_search)

        origin_currency = self.url[initial_origin_currency_index:final_origin_currency_index]
        if origin_currency == "moedadestino":
            self.exchange_currency_origin()
            final_origin_currency_index = self.url.find("&")
            initial_origin_currency_index = self.finds_initial_index(source_currency_search)

            origin_currency = self.url[initial_origin_currency_index:final_origin_currency_index]
        target_currency = self.url[initial_target_currency_index:final_target_currency_index]

        return origin_currency, target_currency

    def finds_initial_index(self, currency):
        return self.url.find(currency) + len(currency)

    def exchange_currency_origin(self):
        self.url = self.url.replace("moedadestino", "real", 1)

    def extract_value(self):
        search_value = "valor="
        index_initial_value = self.finds_initial_index(currency=search_value)
        value = self.url[index_initial_value:]
        return value
