import pandas as pd


class WbCardService:
    def xlsx_file_handler(self, article_file):
        xl = pd.ExcelFile(article_file)
        df1 = xl.parse(xl.sheet_names[0])
        return df1[df1.columns[0]].values.tolist()

    def data_prep(self, validated_data: dict):
        result_data = list()
        article = validated_data.get('article', None)
        if article:
            result_data.append(article)
        article_file = validated_data.get('article_file', None)

        if article_file:
            result_data += self.xlsx_file_handler(article_file)

        return result_data
