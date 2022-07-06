import pandas as pd
import numpy as np

class Meals:
    def __init__(self):
        self.train = pd.read_csv('data/train.csv')
        self.test = pd.read_csv('data/test.csv')
        self.df = pd.concat([self.train, self.test], axis=0).reset_index(drop=True)

    def refine(self):
        df = self.df.copy()

        #Wide Form -> Long Form 변환
        meal_df = self.__transform_to_long(df)
        
        #메뉴 불필요항 제거
        meal_df = self.__remove_no_need_item_in_menu(meal_df)

        #메뉴 One-Hot-Encoding
        meal_df = pd.merge(meal_df, self.__menu_one_hot_encoding(meal_df), on=['일자', '시간대'])
        
        #요일 One-Hot-Encoding
        meal_df = pd.concat([meal_df.drop(columns=['요일']), pd.get_dummies(meal_df["요일"])[['월', '화', '수', '목', '금']]], axis=1)


        return meal_df
        
        


    def __transform_to_long(self, df):
        target_df = df.drop(columns=["조식메뉴"])
        
        target_df['일자'] = pd.to_datetime(target_df["일자"])
        #코로나발발이후 열 추가
        target_df["코로나발발이후"] = False
        target_df.loc[target_df["일자"] >= '2019-12-31',  "코로나발발이후"] = True
        #중식, 석식 행 구분을 위해 컬럼 분리
        columns = target_df.columns.tolist()
        
        
        #lunch, dinner별로 필요한 열 편집
        mealtime = {"lunch":"중식", "dinner":"석식"}
        meal_dfs = []
        timeslot = 0
        for eng, kor in mealtime.items():
            cols = self.__get_cols_by_timeslot(columns, [f'{kor}메뉴', f'{kor}계'])
            temp_df = target_df[cols].rename(columns={f'{kor}메뉴':'메뉴', f'{kor}계' : '식수'})
            temp_df["시간대"] = timeslot
            timeslot += 1
            meal_dfs.append(temp_df)

        return pd.concat(meal_dfs, axis=0).sort_values(by=['일자', '시간대'])


    def  __get_cols_by_timeslot(self, columns, targets):
        cols = columns.copy()
        to_removes = []
        for col in cols:
            if (col not in targets) and (("중식" in col) | ("석식" in col)) :
                to_removes.append(col) 
        
        for _ in to_removes:
            cols.remove(_)
        return cols

        
    def __remove_no_need_item_in_menu(self, df):
        temp_df = df.copy()
        temp_df['메뉴'] = temp_df['메뉴'].str.replace("  +",  " ", regex=True).str.replace("\(.*?\)\s?", "", regex=True)
        return temp_df


    def __menu_one_hot_encoding(self, df):
        menu_df = df.copy()
        menus = menu_df['메뉴'].replace("  +",  " ", regex=True).str.replace("(\(|\<).*?(\)|\>)\s?", "", regex=True)
        
        spanned_menus = menus.str.strip().str.split(' ', expand=True)
        
        splited_menues = {x : f'메뉴_{x}' for x in range(8)}
        t_df = pd.concat([menu_df[['일자', '시간대']], spanned_menus], axis=1).rename(columns=splited_menues)

        melted_df = t_df.melt(id_vars=['일자', '시간대'], value_vars=splited_menues.values())
        melted_df = melted_df.sort_values(by=['일자', '시간대']).set_index(['일자', '시간대'])
        melted_df = melted_df.drop('variable', axis=1).drop(melted_df['value'] == "", axis=0)
        melted_df[melted_df["value"].isnull()] = "None"
        melted_df["value"] = melted_df["value"].str.replace('*', "", regex=False)

        final_df = pd.get_dummies(melted_df).groupby(by=['일자', '시간대']).sum()
        final_df = final_df.drop(columns=['value_None', 'value_']).reset_index()


        return final_df






if __name__ == '__main__':
    print(Meals().refine())
    