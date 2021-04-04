from ExtractorArgumentsUrl import ExtractorArgumentsUrl

url = "https://bytebank.com/cambio?moedaorigem=real&moedadestino=dolar&valor=100"
args = ExtractorArgumentsUrl(url)

origin_currency, target_currency = args.extract_arguments(source_currency="moedaorigem=",
                                                          destination_currency="moedadestino=")
print(origin_currency, target_currency)
