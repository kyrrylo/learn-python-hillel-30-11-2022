original_seconds = 48 * 3600 + 3665
# 2 days 1 hour, 1 minute, 5 seconds
# количество секунд, минут, часов и дней
# рабочее решение
days = original_seconds // (3600 * 24)
original_seconds -= days * (3600 * 24)
hours = original_seconds // 3600
original_seconds -= hours * 3600
minutes = original_seconds // 60
seconds = original_seconds - minutes * 60
"""
# альтернативное решение
minutes, seconds = divmod(original_seconds, 60)
hours, minutes = divmod(minutes, 60)
days, hours = divmod(hours, 24)
"""
# f - format форматируемая строка
print(f"{days} days {hours} hours {minutes} minutes {seconds} seconds")
