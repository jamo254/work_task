import pandas as pd

""" Фред Денис
 - Задача
""" 
data = {
    "data":
    [
        {
            "order_id": 11973,
            "warehouse_name": "Мордор",
            "highway_cost": -70,
            "products": [
                {
                    "product": "ломтик июльского неба",
                    "price": 450,
                    "quantity": 1
                },
                {
                    "product": "билет в Израиль",
                    "price": 1000,
                    "quantity": 3
                },
                {
                    "product": "статуэтка Ленина",
                    "price": 200,
                    "quantity": 3
                }
            ]
        },
        {
            "order_id": 62239,
            "warehouse_name": "хутор близ Диканьки",
            "highway_cost": -15,
            "products": [
                {
                    "product": "билет в Израиль",
                    "price": 1000,
                    "quantity": 1
                }
            ]
        },
        {
            "order_id": 85794,
            "warehouse_name": "отель Лето",
            "highway_cost": -50,
            "products": [
                {
                    "product": "зеленая пластинка",
                    "price": 10,
                    "quantity": 2
                }
            ]
        },
        {
            "order_id": 33684,
            "warehouse_name": "Мордор",
            "highway_cost": -30,
            "products": [
                {
                    "product": "билет в Израиль",
                    "price": 1000,
                    "quantity": 2
                },
                {
                    "product": "зеленая пластинка",
                    "price": 10,
                    "quantity": 1
                }
            ]
        },
        {
            "order_id": 25824,
            "warehouse_name": "отель Лето",
            "highway_cost": -75,
            "products": [
                {
                    "product": "автограф Стаса Барецкого",
                    "price": 600,
                    "quantity": 1
                },
                {
                    "product": "статуэтка Ленина",
                    "price": 200,
                    "quantity": 1
                },
                {
                    "product": "плюмбус",
                    "price": 250,
                    "quantity": 1
                }
            ]
        },
        {
            "order_id": 87044,
            "warehouse_name": "остров невезения",
            "highway_cost": -15,
            "products": [
                {
                    "product": "плюмбус",
                    "price": 250,
                    "quantity": 3
                }
            ]
        },
        {
            "order_id": 58598,
            "warehouse_name": "гиперборея",
            "highway_cost": -160,
            "products": [
                {
                    "product": "плюмбус",
                    "price": 250,
                    "quantity": 3
                },
                {
                    "product": "статуэтка Ленина",
                    "price": 200,
                    "quantity": 3
                },
                {
                    "product": "статуэтка Ленина",
                    "price": 200,
                    "quantity": 2
                }
            ]
        },
        {
            "order_id": 5430,
            "warehouse_name": "гиперборея",
            "highway_cost": -80,
            "products": [
                {
                    "product": "ломтик июльского неба",
                    "price": 450,
                    "quantity": 1
                },
                {
                    "product": "плюмбус",
                    "price": 250,
                    "quantity": 3
                }
            ]
        },
        {
            "order_id": 60502,
            "warehouse_name": "отель Лето",
            "highway_cost": -75,
            "products": [
                {
                    "product": "автограф Стаса Барецкого",
                    "price": 600,
                    "quantity": 3
                }
            ]
        },
        {
            "order_id": 96473,
            "warehouse_name": "Мордор",
            "highway_cost": -20,
            "products": [
                {
                    "product": "зеленая пластинка",
                    "price": 10,
                    "quantity": 2
                }
            ]
        },
        {
            "order_id": 64013,
            "warehouse_name": "хутор близ Диканьки",
            "highway_cost": -105,
            "products": [
                {
                    "product": "плюмбус",
                    "price": 250,
                    "quantity": 2
                },
                {
                    "product": "плюмбус",
                    "price": 250,
                    "quantity": 2
                },
                {
                    "product": "зеленая пластинка",
                    "price": 10,
                    "quantity": 3
                }
            ]
        },
        {
            "order_id": 59105,
            "warehouse_name": "отель Лето",
            "highway_cost": -25,
            "products": [
                {
                    "product": "статуэтка Ленина",
                    "price": 200,
                    "quantity": 1
                }
            ]
        },
        {
            "order_id": 85535,
            "warehouse_name": "отель Лето",
            "highway_cost": -25,
            "products": [
                {
                    "product": "статуэтка Ленина",
                    "price": 200,
                    "quantity": 1
                }
            ]
        },
        {
            "order_id": 24928,
            "warehouse_name": "хутор близ Диканьки",
            "highway_cost": -60,
            "products": [
                {
                    "product": "подписка на suppi-блог",
                    "price": 150,
                    "quantity": 2
                },
                {
                    "product": "статуэтка Ленина",
                    "price": 200,
                    "quantity": 1
                },
                {
                    "product": "статуэтка Ленина",
                    "price": 200,
                    "quantity": 1
                }
            ]
        },
        {
            "order_id": 2751,
            "warehouse_name": "гиперборея",
            "highway_cost": -80,
            "products": [
                {
                    "product": "зеленая пластинка",
                    "price": 10,
                    "quantity": 3
                },
                {
                    "product": "зеленая пластинка",
                    "price": 10,
                    "quantity": 1
                }
            ]
        },
        {
            "order_id": 35995,
            "warehouse_name": "гиперборея",
            "highway_cost": -20,
            "products": [
                {
                    "product": "ломтик июльского неба",
                    "price": 450,
                    "quantity": 1
                }
            ]
        },
        {
            "order_id": 80252,
            "warehouse_name": "остров невезения",
            "highway_cost": -35,
            "products": [
                {
                    "product": "статуэтка Ленина",
                    "price": 200,
                    "quantity": 3
                },
                {
                    "product": "статуэтка Ленина",
                    "price": 200,
                    "quantity": 2
                },
                {
                    "product": "ломтик июльского неба",
                    "price": 450,
                    "quantity": 2
                }
            ]
        },
        {
            "order_id": 27443,
            "warehouse_name": "Мордор",
            "highway_cost": -10,
            "products": [
                {
                    "product": "статуэтка Ленина",
                    "price": 200,
                    "quantity": 1
                }
            ]
        },
        {
            "order_id": 1391,
            "warehouse_name": "остров невезения",
            "highway_cost": -10,
            "products": [
                {
                    "product": "плюмбус",
                    "price": 250,
                    "quantity": 2
                }
            ]
        },
        {
            "order_id": 83474,
            "warehouse_name": "хутор близ Диканьки",
            "highway_cost": -75,
            "products": [
                {
                    "product": "плюмбус",
                    "price": 250,
                    "quantity": 2
                },
                {
                    "product": "ломтик июльского неба",
                    "price": 450,
                    "quantity": 3
                }
            ]
        },
        {
            "order_id": 84471,
            "warehouse_name": "хутор близ Диканьки",
            "highway_cost": -60,
            "products": [
                {
                    "product": "плюмбус",
                    "price": 250,
                    "quantity": 1
                },
                {
                    "product": "ломтик июльского неба",
                    "price": 450,
                    "quantity": 1
                },
                {
                    "product": "подписка на suppi-блог",
                    "price": 150,
                    "quantity": 2
                }
            ]
        },
        {
            "order_id": 96799,
            "warehouse_name": "остров невезения",
            "highway_cost": -10,
            "products": [
                {
                    "product": "ломтик июльского неба",
                    "price": 450,
                    "quantity": 2
                }
            ]
        },
        {
            "order_id": 99324,
            "warehouse_name": "остров невезения",
            "highway_cost": -10,
            "products": [
                {
                    "product": "автограф Стаса Барецкого",
                    "price": 600,
                    "quantity": 1
                },
                {
                    "product": "билет в Израиль",
                    "price": 1000,
                    "quantity": 1
                }
            ]
        },
        {
            "order_id": 85787,
            "warehouse_name": "хутор близ Диканьки",
            "highway_cost": -90,
            "products": [
                {
                    "product": "зеленая пластинка",
                    "price": 10,
                    "quantity": 3
                },
                {
                    "product": "зеленая пластинка",
                    "price": 10,
                    "quantity": 2
                },
                {
                    "product": "билет в Израиль",
                    "price": 1000,
                    "quantity": 1
                }
            ]
        },
        {
            "order_id": 28774,
            "warehouse_name": "отель Лето",
            "highway_cost": -175,
            "products": [
                {
                    "product": "билет в Израиль",
                    "price": 1000,
                    "quantity": 2
                },
                {
                    "product": "статуэтка Ленина",
                    "price": 200,
                    "quantity": 3
                },
                {
                    "product": "билет в Израиль",
                    "price": 1000,
                    "quantity": 2
                }
            ]
        },
        {
            "order_id": 68707,
            "warehouse_name": "отель Лето",
            "highway_cost": -50,
            "products": [
                {
                    "product": "плюмбус",
                    "price": 250,
                    "quantity": 2
                }
            ]
        },
        {
            "order_id": 99220,
            "warehouse_name": "хутор близ Диканьки",
            "highway_cost": -75,
            "products": [
                {
                    "product": "плюмбус",
                    "price": 250,
                    "quantity": 3
                },
                {
                    "product": "подписка на suppi-блог",
                    "price": 150,
                    "quantity": 1
                },
                {
                    "product": "плюмбус",
                    "price": 250,
                    "quantity": 1
                }
            ]
        },
        {
            "order_id": 59930,
            "warehouse_name": "остров невезения",
            "highway_cost": -20,
            "products": [
                {
                    "product": "зеленая пластинка",
                    "price": 10,
                    "quantity": 2
                },
                {
                    "product": "статуэтка Ленина",
                    "price": 200,
                    "quantity": 2
                }
            ]
        },
        {
            "order_id": 70074,
            "warehouse_name": "остров невезения",
            "highway_cost": -30,
            "products": [
                {
                    "product": "плюмбус",
                    "price": 250,
                    "quantity": 2
                },
                {
                    "product": "плюмбус",
                    "price": 250,
                    "quantity": 1
                },
                {
                    "product": "ломтик июльского неба",
                    "price": 450,
                    "quantity": 3
                }
            ]
        },
        {
            "order_id": 12715,
            "warehouse_name": "хутор близ Диканьки",
            "highway_cost": -45,
            "products": [
                {
                    "product": "автограф Стаса Барецкого",
                    "price": 600,
                    "quantity": 1
                },
                {
                    "product": "автограф Стаса Барецкого",
                    "price": 600,
                    "quantity": 2
                }
            ]
        },
        {
            "order_id": 63213,
            "warehouse_name": "Мордор",
            "highway_cost": -30,
            "products": [
                {
                    "product": "зеленая пластинка",
                    "price": 10,
                    "quantity": 3
                }
            ]
        },
        {
            "order_id": 32313,
            "warehouse_name": "хутор близ Диканьки",
            "highway_cost": -120,
            "products": [
                {
                    "product": "билет в Израиль",
                    "price": 1000,
                    "quantity": 3
                },
                {
                    "product": "плюмбус",
                    "price": 250,
                    "quantity": 2
                },
                {
                    "product": "зеленая пластинка",
                    "price": 10,
                    "quantity": 3
                }
            ]
        },
        {
            "order_id": 65113,
            "warehouse_name": "хутор близ Диканьки",
            "highway_cost": -30,
            "products": [
                {
                    "product": "плюмбус",
                    "price": 250,
                    "quantity": 2
                }
            ]
        },
        {
            "order_id": 56905,
            "warehouse_name": "Мордор",
            "highway_cost": -20,
            "products": [
                {
                    "product": "билет в Израиль",
                    "price": 1000,
                    "quantity": 2
                }
            ]
        },
        {
            "order_id": 14742,
            "warehouse_name": "хутор близ Диканьки",
            "highway_cost": -60,
            "products": [
                {
                    "product": "статуэтка Ленина",
                    "price": 200,
                    "quantity": 1
                },
                {
                    "product": "автограф Стаса Барецкого",
                    "price": 600,
                    "quantity": 1
                },
                {
                    "product": "плюмбус",
                    "price": 250,
                    "quantity": 2
                }
            ]
        },
        {
            "order_id": 16240,
            "warehouse_name": "Мордор",
            "highway_cost": -20,
            "products": [
                {
                    "product": "билет в Израиль",
                    "price": 1000,
                    "quantity": 2
                }
            ]
        },
        {
            "order_id": 79318,
            "warehouse_name": "Мордор",
            "highway_cost": -30,
            "products": [
                {
                    "product": "автограф Стаса Барецкого",
                    "price": 600,
                    "quantity": 1
                },
                {
                    "product": "статуэтка Ленина",
                    "price": 200,
                    "quantity": 2
                }
            ]
        },
        {
            "order_id": 20914,
            "warehouse_name": "гиперборея",
            "highway_cost": -40,
            "products": [
                {
                    "product": "билет в Израиль",
                    "price": 1000,
                    "quantity": 2
                }
            ]
        },
        {
            "order_id": 42314,
            "warehouse_name": "хутор близ Диканьки",
            "highway_cost": -45,
            "products": [
                {
                    "product": "статуэтка Ленина",
                    "price": 200,
                    "quantity": 1
                },
                {
                    "product": "статуэтка Ленина",
                    "price": 200,
                    "quantity": 2
                }
            ]
        },
        {
            "order_id": 68783,
            "warehouse_name": "остров невезения",
            "highway_cost": -15,
            "products": [
                {
                    "product": "статуэтка Ленина",
                    "price": 200,
                    "quantity": 3
                }
            ]
        },
        {
            "order_id": 47954,
            "warehouse_name": "гиперборея",
            "highway_cost": -60,
            "products": [
                {
                    "product": "билет в Израиль",
                    "price": 1000,
                    "quantity": 3
                }
            ]
        },
        {
            "order_id": 83618,
            "warehouse_name": "Мордор",
            "highway_cost": -30,
            "products": [
                {
                    "product": "зеленая пластинка",
                    "price": 10,
                    "quantity": 3
                }
            ]
        },
        {
            "order_id": 57775,
            "warehouse_name": "хутор близ Диканьки",
            "highway_cost": -30,
            "products": [
                {
                    "product": "статуэтка Ленина",
                    "price": 200,
                    "quantity": 2
                }
            ]
        },
        {
            "order_id": 66474,
            "warehouse_name": "гиперборея",
            "highway_cost": -140,
            "products": [
                {
                    "product": "плюмбус",
                    "price": 250,
                    "quantity": 2
                },
                {
                    "product": "автограф Стаса Барецкого",
                    "price": 600,
                    "quantity": 3
                },
                {
                    "product": "билет в Израиль",
                    "price": 1000,
                    "quantity": 2
                }
            ]
        },
        {
            "order_id": 72097,
            "warehouse_name": "остров невезения",
            "highway_cost": -30,
            "products": [
                {
                    "product": "ломтик июльского неба",
                    "price": 450,
                    "quantity": 5
                },
                {
                    "product": "зеленая пластинка",
                    "price": 10,
                    "quantity": 3
                }
            ]
        },
        {
            "order_id": 74454,
            "warehouse_name": "отель Лето",
            "highway_cost": -150,
            "products": [
                {
                    "product": "зеленая пластинка",
                    "price": 10,
                    "quantity": 1
                },
                {
                    "product": "автограф Стаса Барецкого",
                    "price": 600,
                    "quantity": 2
                },
                {
                    "product": "билет в Израиль",
                    "price": 1000,
                    "quantity": 3
                }
            ]
        },
        {
            "order_id": 14350,
            "warehouse_name": "гиперборея",
            "highway_cost": -120,
            "products": [
                {
                    "product": "автограф Стаса Барецкого",
                    "price": 600,
                    "quantity": 1
                },
                {
                    "product": "ломтик июльского неба",
                    "price": 450,
                    "quantity": 3
                },
                {
                    "product": "автограф Стаса Барецкого",
                    "price": 600,
                    "quantity": 2
                }
            ]
        },
        {
            "order_id": 4035,
            "warehouse_name": "хутор близ Диканьки",
            "highway_cost": -75,
            "products": [
                {
                    "product": "автограф Стаса Барецкого",
                    "price": 600,
                    "quantity": 2
                },
                {
                    "product": "билет в Израиль",
                    "price": 1000,
                    "quantity": 3
                }
            ]
        },
        {
            "order_id": 67495,
            "warehouse_name": "Мордор",
            "highway_cost": -70,
            "products": [
                {
                    "product": "подписка на suppi-блог",
                    "price": 150,
                    "quantity": 1
                },
                {
                    "product": "подписка на suppi-блог",
                    "price": 150,
                    "quantity": 3
                },
                {
                    "product": "подписка на suppi-блог",
                    "price": 150,
                    "quantity": 3
                }
            ]
        },
        {
            "order_id": 49616,
            "warehouse_name": "отель Лето",
            "highway_cost": -100,
            "products": [
                {
                    "product": "билет в Израиль",
                    "price": 1000,
                    "quantity": 3
                },
                {
                    "product": "зеленая пластинка",
                    "price": 10,
                    "quantity": 1
                }
            ]
        },
        {
            "order_id": 83887,
            "warehouse_name": "гиперборея",
            "highway_cost": -80,
            "products": [
                {
                    "product": "зеленая пластинка",
                    "price": 10,
                    "quantity": 1
                },
                {
                    "product": "статуэтка Ленина",
                    "price": 200,
                    "quantity": 2
                },
                {
                    "product": "билет в Израиль",
                    "price": 1000,
                    "quantity": 1
                }
            ]
        },
        {
            "order_id": 50030,
            "warehouse_name": "гиперборея",
            "highway_cost": -140,
            "products": [
                {
                    "product": "подписка на suppi-блог",
                    "price": 150,
                    "quantity": 3
                },
                {
                    "product": "билет в Израиль",
                    "price": 1000,
                    "quantity": 2
                },
                {
                    "product": "автограф Стаса Барецкого",
                    "price": 600,
                    "quantity": 2
                }
            ]
        },
        {
            "order_id": 2558,
            "warehouse_name": "хутор близ Диканьки",
            "highway_cost": -75,
            "products": [
                {
                    "product": "плюмбус",
                    "price": 250,
                    "quantity": 1
                },
                {
                    "product": "зеленая пластинка",
                    "price": 10,
                    "quantity": 3
                },
                {
                    "product": "подписка на suppi-блог",
                    "price": 150,
                    "quantity": 1
                }
            ]
        },
        {
            "order_id": 82378,
            "warehouse_name": "остров невезения",
            "highway_cost": -5,
            "products": [
                {
                    "product": "статуэтка Ленина",
                    "price": 200,
                    "quantity": 1
                }
            ]
        },
        {
            "order_id": 88503,
            "warehouse_name": "гиперборея",
            "highway_cost": -140,
            "products": [
                {
                    "product": "зеленая пластинка",
                    "price": 10,
                    "quantity": 2
                },
                {
                    "product": "билет в Израиль",
                    "price": 1000,
                    "quantity": 3
                },
                {
                    "product": "подписка на suppi-блог",
                    "price": 150,
                    "quantity": 2
                }
            ]
        },
        {
            "order_id": 17339,
            "warehouse_name": "гиперборея",
            "highway_cost": -60,
            "products": [
                {
                    "product": "автограф Стаса Барецкого",
                    "price": 600,
                    "quantity": 3
                }
            ]
        },
        {
            "order_id": 2108,
            "warehouse_name": "остров невезения",
            "highway_cost": -10,
            "products": [
                {
                    "product": "зеленая пластинка",
                    "price": 10,
                    "quantity": 1
                },
                {
                    "product": "статуэтка Ленина",
                    "price": 200,
                    "quantity": 1
                }
            ]
        },
        {
            "order_id": 48000,
            "warehouse_name": "остров невезения",
            "highway_cost": -30,
            "products": [
                {
                    "product": "плюмбус",
                    "price": 250,
                    "quantity": 1
                },
                {
                    "product": "плюмбус",
                    "price": 250,
                    "quantity": 3
                },
                {
                    "product": "статуэтка Ленина",
                    "price": 200,
                    "quantity": 2
                }
            ]
        },
        {
            "order_id": 2091,
            "warehouse_name": "отель Лето",
            "highway_cost": -100,
            "products": [
                {
                    "product": "ломтик июльского неба",
                    "price": 450,
                    "quantity": 2
                },
                {
                    "product": "плюмбус",
                    "price": 250,
                    "quantity": 2
                }
            ]
        },
        {
            "order_id": 35330,
            "warehouse_name": "отель Лето",
            "highway_cost": -125,
            "products": [
                {
                    "product": "билет в Израиль",
                    "price": 1000,
                    "quantity": 2
                },
                {
                    "product": "зеленая пластинка",
                    "price": 10,
                    "quantity": 3
                }
            ]
        },
        {
            "order_id": 89159,
            "warehouse_name": "гиперборея",
            "highway_cost": -40,
            "products": [
                {
                    "product": "подписка на suppi-блог",
                    "price": 150,
                    "quantity": 2
                }
            ]
        },
        {
            "order_id": 22103,
            "warehouse_name": "гиперборея",
            "highway_cost": -60,
            "products": [
                {
                    "product": "плюмбус",
                    "price": 250,
                    "quantity": 1
                },
                {
                    "product": "подписка на suppi-блог",
                    "price": 150,
                    "quantity": 1
                },
                {
                    "product": "билет в Израиль",
                    "price": 1000,
                    "quantity": 1
                }
            ]
        },
        {
            "order_id": 64670,
            "warehouse_name": "гиперборея",
            "highway_cost": -100,
            "products": [
                {
                    "product": "билет в Израиль",
                    "price": 1000,
                    "quantity": 2
                },
                {
                    "product": "ломтик июльского неба",
                    "price": 450,
                    "quantity": 3
                }
            ]
        },
        {
            "order_id": 52587,
            "warehouse_name": "Мордор",
            "highway_cost": -80,
            "products": [
                {
                    "product": "зеленая пластинка",
                    "price": 10,
                    "quantity": 2
                },
                {
                    "product": "плюмбус",
                    "price": 250,
                    "quantity": 3
                },
                {
                    "product": "автограф Стаса Барецкого",
                    "price": 600,
                    "quantity": 3
                }
            ]
        },
        {
            "order_id": 88114,
            "warehouse_name": "отель Лето",
            "highway_cost": -75,
            "products": [
                {
                    "product": "ломтик июльского неба",
                    "price": 450,
                    "quantity": 1
                },
                {
                    "product": "подписка на suppi-блог",
                    "price": 150,
                    "quantity": 1
                },
                {
                    "product": "плюмбус",
                    "price": 250,
                    "quantity": 1
                }
            ]
        },
        {
            "order_id": 72357,
            "warehouse_name": "гиперборея",
            "highway_cost": -100,
            "products": [
                {
                    "product": "подписка на suppi-блог",
                    "price": 150,
                    "quantity": 1
                },
                {
                    "product": "билет в Израиль",
                    "price": 1000,
                    "quantity": 2
                },
                {
                    "product": "билет в Израиль",
                    "price": 1000,
                    "quantity": 2
                }
            ]
        },
        {
            "order_id": 82545,
            "warehouse_name": "отель Лето",
            "highway_cost": -125,
            "products": [
                {
                    "product": "подписка на suppi-блог",
                    "price": 150,
                    "quantity": 2
                },
                {
                    "product": "плюмбус",
                    "price": 250,
                    "quantity": 3
                }
            ]
        },
        {
            "order_id": 59590,
            "warehouse_name": "отель Лето",
            "highway_cost": -75,
            "products": [
                {
                    "product": "билет в Израиль",
                    "price": 1000,
                    "quantity": 3
                }
            ]
        },
        {
            "order_id": 20814,
            "warehouse_name": "хутор близ Диканьки",
            "highway_cost": -45,
            "products": [
                {
                    "product": "статуэтка Ленина",
                    "price": 200,
                    "quantity": 2
                },
                {
                    "product": "автограф Стаса Барецкого",
                    "price": 600,
                    "quantity": 1
                }
            ]
        },
        {
            "order_id": 32918,
            "warehouse_name": "хутор близ Диканьки",
            "highway_cost": -105,
            "products": [
                {
                    "product": "статуэтка Ленина",
                    "price": 200,
                    "quantity": 1
                },
                {
                    "product": "автограф Стаса Барецкого",
                    "price": 600,
                    "quantity": 3
                },
                {
                    "product": "плюмбус",
                    "price": 250,
                    "quantity": 3
                }
            ]
        },
        {
            "order_id": 33899,
            "warehouse_name": "гиперборея",
            "highway_cost": -20,
            "products": [
                {
                    "product": "билет в Израиль",
                    "price": 1000,
                    "quantity": 1
                }
            ]
        },
        {
            "order_id": 72309,
            "warehouse_name": "остров невезения",
            "highway_cost": -5,
            "products": [
                {
                    "product": "билет в Израиль",
                    "price": 1000,
                    "quantity": 1
                }
            ]
        },
        {
            "order_id": 98423,
            "warehouse_name": "хутор близ Диканьки",
            "highway_cost": -30,
            "products": [
                {
                    "product": "автограф Стаса Барецкого",
                    "price": 600,
                    "quantity": 2
                }
            ]
        },
        {
            "order_id": 28543,
            "warehouse_name": "хутор близ Диканьки",
            "highway_cost": -75,
            "products": [
                {
                    "product": "статуэтка Ленина",
                    "price": 200,
                    "quantity": 3
                },
                {
                    "product": "статуэтка Ленина",
                    "price": 200,
                    "quantity": 2
                }
            ]
        },
        {
            "order_id": 64068,
            "warehouse_name": "Мордор",
            "highway_cost": -10,
            "products": [
                {
                    "product": "подписка на suppi-блог",
                    "price": 150,
                    "quantity": 1
                }
            ]
        },
        {
            "order_id": 75938,
            "warehouse_name": "гиперборея",
            "highway_cost": -80,
            "products": [
                {
                    "product": "зеленая пластинка",
                    "price": 10,
                    "quantity": 1
                },
                {
                    "product": "ломтик июльского неба",
                    "price": 450,
                    "quantity": 3
                }
            ]
        },
        {
            "order_id": 47230,
            "warehouse_name": "отель Лето",
            "highway_cost": -25,
            "products": [
                {
                    "product": "ломтик июльского неба",
                    "price": 450,
                    "quantity": 1
                }
            ]
        },
        {
            "order_id": 64268,
            "warehouse_name": "хутор близ Диканьки",
            "highway_cost": -75,
            "products": [
                {
                    "product": "автограф Стаса Барецкого",
                    "price": 600,
                    "quantity": 1
                },
                {
                    "product": "зеленая пластинка",
                    "price": 10,
                    "quantity": 1
                },
                {
                    "product": "подписка на suppi-блог",
                    "price": 150,
                    "quantity": 3
                }
            ]
        },
        {
            "order_id": 65559,
            "warehouse_name": "остров невезения",
            "highway_cost": -20,
            "products": [
                {
                    "product": "статуэтка Ленина",
                    "price": 200,
                    "quantity": 3
                },
                {
                    "product": "статуэтка Ленина",
                    "price": 200,
                    "quantity": 1
                }
            ]
        },
        {
            "order_id": 6535,
            "warehouse_name": "хутор близ Диканьки",
            "highway_cost": -105,
            "products": [
                {
                    "product": "автограф Стаса Барецкого",
                    "price": 600,
                    "quantity": 2
                },
                {
                    "product": "автограф Стаса Барецкого",
                    "price": 600,
                    "quantity": 2
                },
                {
                    "product": "зеленая пластинка",
                    "price": 10,
                    "quantity": 3
                }
            ]
        },
        {
            "order_id": 77850,
            "warehouse_name": "хутор близ Диканьки",
            "highway_cost": -60,
            "products": [
                {
                    "product": "билет в Израиль",
                    "price": 1000,
                    "quantity": 2
                },
                {
                    "product": "автограф Стаса Барецкого",
                    "price": 600,
                    "quantity": 2
                }
            ]
        },
        {
            "order_id": 76803,
            "warehouse_name": "отель Лето",
            "highway_cost": -25,
            "products": [
                {
                    "product": "зеленая пластинка",
                    "price": 10,
                    "quantity": 1
                }
            ]
        },
        {
            "order_id": 99246,
            "warehouse_name": "хутор близ Диканьки",
            "highway_cost": -45,
            "products": [
                {
                    "product": "автограф Стаса Барецкого",
                    "price": 600,
                    "quantity": 3
                }
            ]
        },
        {
            "order_id": 96721,
            "warehouse_name": "Мордор",
            "highway_cost": -20,
            "products": [
                {
                    "product": "ломтик июльского неба",
                    "price": 450,
                    "quantity": 2
                }
            ]
        },
        {
            "order_id": 88509,
            "warehouse_name": "гиперборея",
            "highway_cost": -60,
            "products": [
                {
                    "product": "автограф Стаса Барецкого",
                    "price": 600,
                    "quantity": 1
                },
                {
                    "product": "ломтик июльского неба",
                    "price": 450,
                    "quantity": 2
                }
            ]
        },
        {
            "order_id": 33780,
            "warehouse_name": "гиперборея",
            "highway_cost": -120,
            "products": [
                {
                    "product": "подписка на suppi-блог",
                    "price": 150,
                    "quantity": 2
                },
                {
                    "product": "статуэтка Ленина",
                    "price": 200,
                    "quantity": 2
                },
                {
                    "product": "зеленая пластинка",
                    "price": 10,
                    "quantity": 2
                }
            ]
        },
        {
            "order_id": 70216,
            "warehouse_name": "хутор близ Диканьки",
            "highway_cost": -90,
            "products": [
                {
                    "product": "плюмбус",
                    "price": 250,
                    "quantity": 2
                },
                {
                    "product": "статуэтка Ленина",
                    "price": 200,
                    "quantity": 2
                },
                {
                    "product": "статуэтка Ленина",
                    "price": 200,
                    "quantity": 2
                }
            ]
        },
        {
            "order_id": 26702,
            "warehouse_name": "Мордор",
            "highway_cost": -40,
            "products": [
                {
                    "product": "статуэтка Ленина",
                    "price": 200,
                    "quantity": 1
                },
                {
                    "product": "статуэтка Ленина",
                    "price": 200,
                    "quantity": 3
                }
            ]
        },
        {
            "order_id": 83889,
            "warehouse_name": "отель Лето",
            "highway_cost": -150,
            "products": [
                {
                    "product": "зеленая пластинка",
                    "price": 10,
                    "quantity": 2
                },
                {
                    "product": "автограф Стаса Барецкого",
                    "price": 600,
                    "quantity": 1
                },
                {
                    "product": "статуэтка Ленина",
                    "price": 200,
                    "quantity": 3
                }
            ]
        },
        {
            "order_id": 16012,
            "warehouse_name": "отель Лето",
            "highway_cost": -50,
            "products": [
                {
                    "product": "ломтик июльского неба",
                    "price": 450,
                    "quantity": 2
                }
            ]
        },
        {
            "order_id": 61521,
            "warehouse_name": "хутор близ Диканьки",
            "highway_cost": -45,
            "products": [
                {
                    "product": "ломтик июльского неба",
                    "price": 450,
                    "quantity": 3
                }
            ]
        },
        {
            "order_id": 15237,
            "warehouse_name": "хутор близ Диканьки",
            "highway_cost": -60,
            "products": [
                {
                    "product": "зеленая пластинка",
                    "price": 10,
                    "quantity": 1
                },
                {
                    "product": "плюмбус",
                    "price": 250,
                    "quantity": 1
                },
                {
                    "product": "зеленая пластинка",
                    "price": 10,
                    "quantity": 2
                }
            ]
        },
        {
            "order_id": 20645,
            "warehouse_name": "отель Лето",
            "highway_cost": -50,
            "products": [
                {
                    "product": "ломтик июльского неба",
                    "price": 450,
                    "quantity": 2
                }
            ]
        },
        {
            "order_id": 70849,
            "warehouse_name": "остров невезения",
            "highway_cost": -25,
            "products": [
                {
                    "product": "зеленая пластинка",
                    "price": 10,
                    "quantity": 1
                },
                {
                    "product": "плюмбус",
                    "price": 250,
                    "quantity": 2
                },
                {
                    "product": "зеленая пластинка",
                    "price": 10,
                    "quantity": 2
                }
            ]
        },
        {
            "order_id": 36764,
            "warehouse_name": "гиперборея",
            "highway_cost": -20,
            "products": [
                {
                    "product": "подписка на suppi-блог",
                    "price": 150,
                    "quantity": 1
                }
            ]
        },
        {
            "order_id": 28106,
            "warehouse_name": "хутор близ Диканьки",
            "highway_cost": -30,
            "products": [
                {
                    "product": "подписка на suppi-блог",
                    "price": 150,
                    "quantity": 1
                },
                {
                    "product": "статуэтка Ленина",
                    "price": 200,
                    "quantity": 1
                }
            ]
        },
        {
            "order_id": 98100,
            "warehouse_name": "остров невезения",
            "highway_cost": -10,
            "products": [
                {
                    "product": "автограф Стаса Барецкого",
                    "price": 600,
                    "quantity": 1
                },
                {
                    "product": "билет в Израиль",
                    "price": 1000,
                    "quantity": 1
                }
            ]
        },
        {
            "order_id": 79293,
            "warehouse_name": "отель Лето",
            "highway_cost": -75,
            "products": [
                {
                    "product": "статуэтка Ленина",
                    "price": 200,
                    "quantity": 1
                },
                {
                    "product": "автограф Стаса Барецкого",
                    "price": 600,
                    "quantity": 1
                },
                {
                    "product": "ломтик июльского неба",
                    "price": 450,
                    "quantity": 1
                }
            ]
        },
        {
            "order_id": 2930,
            "warehouse_name": "Мордор",
            "highway_cost": -30,
            "products": [
                {
                    "product": "плюмбус",
                    "price": 250,
                    "quantity": 2
                },
                {
                    "product": "плюмбус",
                    "price": 250,
                    "quantity": 1
                }
            ]
        },
        {
            "order_id": 124,
            "warehouse_name": "хутор близ Диканьки",
            "highway_cost": -45,
            "products": [
                {
                    "product": "плюмбус",
                    "price": 250,
                    "quantity": 3
                }
            ]
        }
    ]
}

# Question 1 - tariff cost of delivery for each warehouse
df = pd.DataFrame(data["data"])
df["tariff_cost"] = df["highway_cost"] / \
    df["products"].apply(lambda x: sum([p["quantity"] for p in x]))

print(df)

# Question 2 -
# Найти суммарное количество , суммарный доход ,
# суммарный расход и суммарную прибыль для каждого товара (представить как таблицу со столбцами
# 'product', 'quantity', 'income', 'expenses', 'profit')

# aggregated data
aggregated_df = pd.DataFrame(
    columns=['product', 'quantity', 'income', 'expenses', 'profit'])

# Iterate over each row in the original DataFrame and calculate the required values:
for index, row in df.iterrows():
    order_id = row['order_id']
    warehouse_name = row['warehouse_name']
    products = row['products']

    for product in products:
        product_name = product['product']
        price = product['price']
        quantity = product['quantity']

        income = price * quantity
        expenses = row['highway_cost']
        profit = income - expenses

        aggregated_df = aggregated_df.append({
            'product': product_name,
            'quantity': quantity,
            'income': income,
            'expenses': expenses,
            'profit': profit
        }, ignore_index=True)
# Grouping DataFrame 'product' and calculate the sum of 'quantity', 'income', 'expenses', and 'profit':
aggregated_df = aggregated_df.groupby('product').sum().reset_index()
print(aggregated_df)  # results


# Question 3 -
# Составить табличку со столбцами 'order_id' (id заказа) и 'order_profit' (прибыль полученная с заказа).
# А также вывести среднюю прибыль заказов

# Creating table with columns 'order_id' and 'order_profit'

profit_df = pd.DataFrame(columns=['order_id', 'order_profit'])

# Iterater each row in original DataFrame
for index, row in df.iterrows():
    order_id = row['order_id']
    products = row['products']
    highway_cost = row['highway_cost']
    order_profit = sum([(p['price'] * p['quantity']) -
                       highway_cost for p in products])

    profit_df = profit_df.append({
        'order_id': order_id,
        'order_profit': order_profit
    }, ignore_index=True)

# Calculate the average order profit:
average_profit = profit_df['order_profit'].mean()
# order profit DataFrame and average profit:
print(profit_df)
print("Average Profit: ", average_profit)

# Question 4 -

""" Составить табличку типа 'warehouse_name', 'product', 'quantity', 'profit', 'percent_profit_product_of_warehouse'
 (процент прибыли продукта заказанного из определенного склада к прибыли этого склада)

 creating a table with columns 'warehouse_name', 'product', 'quantity', 'profit',
 and 'percent_profit_product_of_warehouse' 
"""
profit_percent_df = pd.DataFrame(columns=[
                                 'warehouse_name', 'product', 'quantity', 'profit', 'percent_profit_product_of_warehouse'])

# Iterate over each row
for index, row in df.iterrows():
    warehouse_name = row['warehouse_name']
    products = row['products']
    highway_cost = row['highway_cost']
    total_warehouse_profit = sum(
        [(p['price'] * p['quantity']) - highway_cost for p in products])

    for product in products:
        product_name = product['product']
        quantity = product['quantity']
        product_profit = (product['price'] * quantity) - highway_cost
        percent_profit_product_of_warehouse = (
            product_profit / total_warehouse_profit) * 100

        profit_percent_df = profit_percent_df.append({
            'warehouse_name': warehouse_name,
            'product': product_name,
            'quantity': quantity,
            'profit': product_profit,
            'percent_profit_product_of_warehouse': percent_profit_product_of_warehouse
        }, ignore_index=True)

# Results
print("Profit percent", profit_percent_df)

#Question 5- 
""" Взять предыдущую табличку и отсортировать 'percent_profit_product_of_warehouse' по убыванию, после посчитать накопленный процент. 
  Накопленный процент - это новый столбец в этой табличке, который должен называться
 'accumulated_percent_profit_product_of_warehouse'. По своей сути это постоянно растущая сумма отсортированного по убыванию столбца 'percent_profit_product_of_warehouse'.
"""

# Sorting the DataFrame by 'percent_profit_product_of_warehouse' column in descending order
sorted_df = profit_percent_df.sort_values(by='percent_profit_product_of_warehouse', ascending=False)
#accumulated percentage:
sorted_df['accumulated_percent_profit_product_of_warehouse'] = sorted_df['percent_profit_product_of_warehouse'].cumsum()

print(sorted_df)


#Question 6 -
"""
Присвоить A, B, C - категории на основании значения накопленного процента('accumulated_percent_profit_product_of_warehouse'). 
Если значение накопленного процента меньше или равно 70, то категория A.
Если от 70 до 90 (включая 90), то категория Б. 
Остальное - категория C. Новый столбец обозначить в таблице как 'category'
"""

#Creating a new column 'category' in the DataFrame:
sorted_df['category'] = ''

# Assign categories A, B, and C based on the value of the accumulated percentage:

sorted_df.loc[sorted_df['accumulated_percent_profit_product_of_warehouse'] <= 70, 'category'] = 'A'
sorted_df.loc[(sorted_df['accumulated_percent_profit_product_of_warehouse'] > 70) & (sorted_df['accumulated_percent_profit_product_of_warehouse'] <= 90), 'category'] = 'B'
sorted_df.loc[sorted_df['accumulated_percent_profit_product_of_warehouse'] > 90, 'category'] = 'C'
print(sorted_df)
