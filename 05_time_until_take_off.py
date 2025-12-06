import math

from datetime import datetime, timezone


def time_until_take_off(from_time: str, take_off_time: str) -> int:
    def _parse_time(elf_time: str) -> datetime:
        cleaned_date = (
            elf_time.replace("*", "-")
            .replace("@", " ")
            .replace("|", ":")
            .replace(" NP", "")
        )
        format_datetime = datetime.strptime(cleaned_date, "%Y-%m-%d %H:%M:%S")
        format_datetime = format_datetime.replace(tzinfo=timezone.utc)
        return format_datetime

    format_from_time = _parse_time(from_time)
    format_take_off_time = _parse_time(take_off_time)

    difference_time = format_take_off_time - format_from_time
    difference_seconds = difference_time.total_seconds()
    print(math.floor(difference_seconds))

    return math.floor(difference_seconds)


if __name__ == "__main__":
    takeoff = "2025*12*25@00|00|00 NP"

    time_until_take_off("2025*12*24@23|59|30 NP", takeoff)
    # 30

    time_until_take_off("2025*12*25@00|00|00 NP", takeoff)
    # 0

    time_until_take_off("2025*12*25@00|00|12 NP", takeoff)
    # -12
