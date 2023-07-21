from datetime import date, datetime, timedelta

semester_dates = {
    'start_date': date(2023, 4, 20),
    'end_date': date(2023, 6, 20),
}


# Calculate the number of schedules
def count_schedules_within_semester(start_date, end_date):
    schedule_count = 0
    current_date = start_date

    while current_date <= end_date:
        if current_date.weekday() in [2, 3, 4]:
            start_time = datetime.combine(current_date, datetime.strptime('09:00', '%H:%M').time())
            end_time = datetime.combine(current_date, datetime.strptime('10:45', '%H:%M').time())

            if start_date <= start_time.date() <= end_date and start_date <= end_time.date() <= end_date:
                schedule_count += 1

        current_date += timedelta(days=1)

    return schedule_count
