This project is about analyzing mcdonalds menu items yea its simple

Data :

RangeIndex: 260 entries, 0 to 259
Data columns (total 24 columns):
 #   Column                         Non-Null Count  Dtype
---  ------                         --------------  -----
 0   Category                       260 non-null    object
 1   Item                           260 non-null    object
 2   Serving Size                   260 non-null    object
 3   Calories                       260 non-null    int64
 4   Calories from Fat              260 non-null    int64
 5   Total Fat                      260 non-null    float64
 6   Total Fat (% Daily Value)      260 non-null    int64
 7   Saturated Fat                  260 non-null    float64
 8   Saturated Fat (% Daily Value)  260 non-null    int64
 9   Trans Fat                      260 non-null    float64
 10  Cholesterol                    260 non-null    int64
 11  Cholesterol (% Daily Value)    260 non-null    int64
 12  Sodium                         260 non-null    int64
 13  Sodium (% Daily Value)         260 non-null    int64
 14  Carbohydrates                  260 non-null    int64
 15  Carbohydrates (% Daily Value)  260 non-null    int64
 16  Dietary Fiber                  260 non-null    int64
 17  Dietary Fiber (% Daily Value)  260 non-null    int64
 18  Sugars                         260 non-null    int64
 19  Protein                        260 non-null    int64
 20  Vitamin A (% Daily Value)      260 non-null    int64
 21  Vitamin C (% Daily Value)      260 non-null    int64
 22  Calcium (% Daily Value)        260 non-null    int64
 23  Iron (% Daily Value)           260 non-null    int64
dtypes: float64(3), int64(18), object(3)
memory usage: 48.9+ KB
None
                                         Item  fat_calorie_ratio
28              Big Breakfast (Large Biscuit)           0.587500
11            Sausage Biscuit (Large Biscuit)           0.583333
27            Big Breakfast (Regular Biscuit)           0.581081
13   Sausage Biscuit with Egg (Large Biscuit)           0.578947
78                Chicken McNuggets (4 piece)           0.578947
..                                        ...                ...
139                          Iced Tea (Large)                NaN
140                          Iced Tea (Child)                NaN
145                            Coffee (Small)                NaN
146                           Coffee (Medium)                NaN
147                            Coffee (Large)                NaN

[260 rows x 2 columns]
                                                  Item  Sugars
253               McFlurry with M&M’s Candies (Medium)     128
246                           Strawberry Shake (Large)     123
249                            Chocolate Shake (Large)     120
251                             Shamrock Shake (Large)     115
258  McFlurry with Reese's Peanut Butter Cups (Medium)     103
..                                                 ...     ...
78                         Chicken McNuggets (4 piece)       0
125                             Diet Dr Pepper (Child)       0
97                                 Medium French Fries       0
38                                          Hash Brown       0
96                                  Small French Fries       0

[260 rows x 2 columns]
                                               Item  protein_density
86   Premium Bacon Ranch Salad with Grilled Chicken         0.131818
163                            Nonfat Latte (Small)         0.100000
165                            Nonfat Latte (Large)         0.094118
89     Premium Southwest Salad with Grilled Chicken         0.093103
164                           Nonfat Latte (Medium)         0.092308
..                                              ...              ...
139                                Iced Tea (Large)              NaN
140                                Iced Tea (Child)              NaN
145                                  Coffee (Small)              NaN
146                                 Coffee (Medium)              NaN
147                                  Coffee (Large)              NaN

[260 rows x 2 columns]
               Category                                               Item     Serving Size  ...  fat_calorie_ratio  protein_density  Unhealthy_score
82       Chicken & Fish                       Chicken McNuggets (40 piece)  22.8 oz (646 g)  ...           0.563830         0.046277              333
32            Breakfast        Big Breakfast with Hotcakes (Large Biscuit)  15.3 oz (434 g)  ...           0.469565         0.031304              204
31            Breakfast      Big Breakfast with Hotcakes (Regular Biscuit)  14.8 oz (420 g)  ...           0.467890         0.033028              194
34            Breakfast  Big Breakfast with Hotcakes and Egg Whites (La...  15.4 oz (437 g)  ...           0.428571         0.033333              190
253  Smoothies & Shakes               McFlurry with M&M’s Candies (Medium)  16.2 oz (460 g)  ...           0.311828         0.021505              189
..                  ...                                                ...              ...  ...                ...              ...              ...
147        Coffee & Tea                                     Coffee (Large)     16 fl oz cup  ...                NaN              NaN                
0
137        Coffee & Tea                                   Iced Tea (Small)     16 fl oz cup  ...                NaN              NaN                
0
138        Coffee & Tea                                  Iced Tea (Medium)     21 fl oz cup  ...                NaN              NaN                
0
145        Coffee & Tea                                     Coffee (Small)     12 fl oz cup  ...                NaN              NaN                
0
136           Beverages                                Dasani Water Bottle       16.9 fl oz  ...                NaN              NaN                
0

[260 rows x 27 columns]
                                                  Item  Iron (% Daily Value)
31       Big Breakfast with Hotcakes (Regular Biscuit)                    40
32         Big Breakfast with Hotcakes (Large Biscuit)                    40
47                  Double Quarter Pounder with Cheese                    35
45           Quarter Pounder with Bacon Habanero Ranch                    30
33   Big Breakfast with Hotcakes and Egg Whites (Re...                    30
..                                                 ...                   ...
198                        Regular Iced Coffee (Large)                     0
197                       Regular Iced Coffee (Medium)                     0
196                        Regular Iced Coffee (Small)                     0
203                      Hazelnut Iced Coffee (Medium)                     0
210  Iced Coffee with Sugar Free French Vanilla Syr...                     0

[260 rows x 2 columns]
      Category                                          Item     Serving Size  ...  protein_density  Unhealthy_score  Vitamins
135  Beverages              Minute Maid Orange Juice (Large)     22 fl oz cup  ...         0.014286               58       240
84      Salads   Premium Bacon Ranch Salad (without Chicken)   7.9 oz (223 g)  ...         0.064286               28       200
89      Salads  Premium Southwest Salad with Grilled Chicken  11.8 oz (335 g)  ...         0.093103               51       200
88      Salads   Premium Southwest Salad with Crispy Chicken  12.3 oz (348 g)  ...         0.051111               80       200
87      Salads     Premium Southwest Salad (without Chicken)   8.1 oz (230 g)  ...         0.042857               19       185
..         ...                                           ...              ...  ...              ...              ...       ...
122  Beverages                        Diet Dr Pepper (Small)     16 fl oz cup  ...              NaN                3         0
123  Beverages                       Diet Dr Pepper (Medium)     21 fl oz cup  ...              NaN                4         0
124  Beverages                        Diet Dr Pepper (Large)     30 fl oz cup  ...              NaN                6         0
36   Breakfast                          Hotcakes and Sausage   6.8 oz (192 g)  ...         0.028846               90         0
35   Breakfast                                      Hotcakes   5.3 oz (151 g)  ...         0.022857               51         0

[260 rows x 28 columns]
                                               Item        Category  health_score
89     Premium Southwest Salad with Grilled Chicken          Salads           206
87        Premium Southwest Salad (without Chicken)          Salads           198
135                Minute Maid Orange Juice (Large)       Beverages           194
84      Premium Bacon Ranch Salad (without Chicken)          Salads           179
88      Premium Southwest Salad with Crispy Chicken          Salads           164
101                                    Apple Slices  Snacks & Sides           159
134               Minute Maid Orange Juice (Medium)       Beverages           131
41        Fruit & Maple Oatmeal without Brown Sugar       Breakfast           124
86   Premium Bacon Ranch Salad with Grilled Chicken          Salads           123
40                            Fruit & Maple Oatmeal       Breakfast           110
