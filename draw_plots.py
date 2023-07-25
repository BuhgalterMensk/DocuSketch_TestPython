import pandas as pd
import matplotlib.pyplot as plt

class Drawing_plots:
    def draw_plots(self, name_json):
        #Загружаем данные из файла в Dataframe
        df = pd.read_json(name_json)
        #Создаем список из путей для картинок
        paths = []
        #Делаем график для каждого столбца
        for t in df:
            # Столбец "name" содержит названия комнат, поэтому для него не строим визуализацию
            if t != 'name':
                #Даем имя графику
                plt.title(t)
                #Строим график
                plt.plot(df[t])
                filename = t + '.png'
                path = 'plots/'+ filename
                #Сохраняем график
                plt.savefig(path)
                paths.append(path)
        return paths

dp = Drawing_plots()
dp.draw_plots('deviation.json')