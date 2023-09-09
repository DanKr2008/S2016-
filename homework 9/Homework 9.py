import requests

class ParseHTML:
    def __init__(self, url: str):
        self.Counter: int = 0
        self.Url = url
        self.Result: dict = {}

    def ParseDollar(self, separator1: str, separator2: str, prefix: str):
        response = requests.get(self.Url)
        response_text = response.text

        start_idx = response_text.find(separator1)
        end_idx = response_text.find(separator2, start_idx)

        while start_idx != -1 and end_idx != -1:
            substring = response_text[start_idx:end_idx]

            if prefix in substring:
                value = substring.split(prefix)[1].strip()
                if value.startswith('>') and value.endswith('</'):
                    value = value[1:-2]
                    self.Result[self.Counter] = value
                    self.Counter += 1

            start_idx = response_text.find(separator1, end_idx)
            end_idx = response_text.find(separator2, start_idx)


url = "https://bank.gov.ua/"
parser = ParseHTML(url)
separator1 = '<div class="collection-item indicator with-dir">'
separator2 = '</div>'
prefix = 'Офіційний курс до дол. США'
parser.ParseDollar(separator1, separator2, prefix)


usd_rate = None
for key, value in parser.Result.items():
    usd_rate = float(value.replace(',', '.'))
    break

if usd_rate is not None:
    print("Курс долара США:", usd_rate)
else:
    print("Курс долара США не знайдено")