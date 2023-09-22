import datetime
from time import sleep

import pandas as pd

print("Hello world from Docker!!!")

while True:
    df = pd.DataFrame(
        data={
            "timestamp": [datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(days=7)],
            "col2": [3, 4],
        }
    )

    print(df)
    sleep(2)


# docker build -t quiz_image .
# docker run --rm -it --name quiz_cont  quiz_image
# python", "src/manage.py", "runserver", "0:8008

# local machine 8010 -> container machine 8000

# docker run --rm -it -p 8008:8010 -v D:\Hillel\quizez_2023\quizez_2023\src:/quiz/src --name quiz_cont
# quiz_image ./commands/start_server_dev.sh
