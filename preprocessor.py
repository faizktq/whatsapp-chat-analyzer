import re
import pandas as pd

def preprocess(data: str) -> pd.DataFrame:
    """
    Parses WhatsApp chat text into a structured DataFrame.
    Handles standard 12-hour (AM/PM) and 24-hour formats automatically.
    """
    # Pattern to identify the start of a message (Dates)
    # This pattern matches: "12/12/12, 10:10 - " or "12/12/12, 10:10 AM - "
    pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}(?:\s?[APap][Mm])?\s-\s'

    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)

    df = pd.DataFrame({'user_message': messages, 'message_date': dates})

    # CLEANING: Remove the trailing " - " from dates to parse them correctly
    df['message_date'] = df['message_date'].str.strip(' - ')

    # PROFESSIONAL FIX: Use 'mixed' format to let Pandas handle different locales automatically
    # dayfirst=True ensures 10/05 is treated as May 10th or Oct 5th correctly based on context
    df['date'] = pd.to_datetime(df['message_date'], format='mixed', dayfirst=True)

    users = []
    messages = []
    for message in df['user_message']:
        # Split user and message: "User: Hello" -> ["User", "Hello"]
        entry = re.split(r'([\w\W]+?):\s', message)
        if entry[1:]:  # User name exists
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('group_notification')
            messages.append(entry[0])

    df['user'] = users
    df['message'] = messages
    df.drop(columns=['user_message', 'message_date'], inplace=True)

    # Extract date attributes for analysis
    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    # Create period for heatmap (e.g., "13-14" for 1 PM)
    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period

    return df