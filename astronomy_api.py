from pathlib import Path
import pandas as pd
from datetime import datetime, timedelta
from astral import moon


def moon_phase_mapping(phase_value):
    if 0 <= phase_value < 3.69:
        return 'New Moon'
    elif 3.69 <= phase_value < 7.38:
        return 'Waxing Crescent'
    elif 7.38 <= phase_value < 11.07:
        return 'First Quarter'
    elif 11.07 <= phase_value < 14.76:
        return 'Waxing Gibbous'
    elif 14.76 <= phase_value < 18.45:
        return 'Full Moon'
    elif 18.45 <= phase_value < 22.14:
        return 'Waning Gibbous'
    elif 22.14 <= phase_value < 25.83:
        return 'Last Quarter'
    else:  # 25.83 <= phase_value < 29.53
        return 'Waning Crescent'


# start and end dates for a 5-year period
start_date = datetime(2019, 3, 6)
end_date = datetime(2024, 3, 5)

data = []

# Generates moon phase for each day
current_date = start_date
while current_date <= end_date:
    phase = moon.phase(current_date)
    phase_desc = moon_phase_mapping(phase)
    data.append([current_date.strftime('%Y-%m-%d'), phase_desc])
    current_date += timedelta(days=1)

df = pd.DataFrame(data, columns=['Date', 'Moon Phase'])
path_to_data_file = Path(__file__).parent / "data" / "moon_phases.csv"
df.to_csv(path_to_data_file, index=False)
print(df)
