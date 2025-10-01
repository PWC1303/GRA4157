def time_to_seconds(time_str):

    try:
        if len(time_str) <7:
            print( "timestring is to short") 
        end_hours_ind = len(time_str)-6
        hh = time_str[0:end_hours_ind]
        mm = time_str[end_hours_ind+1:end_hours_ind+3]
        ss = time_str[end_hours_ind+4:end_hours_ind+6]
        hours_in_sec = int(hh)*3600
        mins_in_sec = int(mm)*60
        ss_in_sec = int(ss)

        if not 0<=int(mm)<60 or not (0<=int(ss)<60):
            raise ValueError("Minutes and seconds must be between 0 and 59")

        total_seconds = hours_in_sec+mins_in_sec+ss_in_sec
    except ValueError as e:
        raise ValueError(f"Invalid time string '{time_str}': {e}")
    return(total_seconds)