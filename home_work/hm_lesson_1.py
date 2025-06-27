"""This app is designed to help you practice formatting python code.

This program should not start, and if it suddenly starts and works,
then some kind of magic has happened.
Basically, because this is not a whole program, but only a piece of it.

"""

import argparse

from datetime import datetime


FILENAME = 'file.txt'

# Find logs according to the given parameters.
# By default it prints the first 300 symbols
ParSer = argparse.ArgumentParser


class EntriesCount:

    """Doc.string for class EntriesCount."""

    def find_entries(self,
                     log_entries: dict,
                     text: str,
                     unwanted: str,
                     date: str) -> dict:

        """Doc.string for def find_entries."""

        if date:
            if date.startswith('..'):
                date = str(datetime.strptime(date[3:], '%Y-%m-%d %H:%M:%S.%f'))
                log_entries = dict(
                    (key, value) for key,
                    value in log_entries.items() if key <= date)

            elif date.endswith('..'):
                date = str(datetime.strptime(date[:-3],
                                             '%Y-%m-%d %H:%M:%S.%f'))
                log_entries = dict(
                    (key, value) for key,
                    value in log_entries.items() if key >= date)
            elif '/' in date:
                date_1 = datetime.strptime(date[:date.find('/')],
                                           '%Y-%m-%d %H:%M:%S.%f')
                date_2 = datetime.strptime(date[date.find('/') + 1:],
                                           '%Y-%m-%d %H:%M:%S.%f')
                log_entries = dict(
                    (key, value) for key,
                    value in log_entries.items() if date_1 <= key <= date_2)
        else:
            date = str(datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f'))
            log_entries = dict(
                (key, value) for key,
                value in log_entries.items() if key == date)

        if text:
            log_entries = dict(
                (key, value) for key,
                value in log_entries.items() if text.lower() in value.lower())

        if unwanted:
            if ',' in unwanted:
                unwanted = str(unwanted.split(','))
            else:
                unwanted = str([unwanted])
            for unw in unwanted:
                log_entries = dict(
                    (key, value) for key,
                    value in log_entries.items()
                    if unw.strip().lower() not in value.lower())
        return log_entries

    def parse_entries(self, logs: list) -> dict:

        """Doc.string for def parse_entries"""

        date = None
        entries = {}
        for log in logs:
            for line in log:
                possible_date = line[:23]
                try:
                    date = datetime.strptime(possible_date,
                                             '%Y-%m-%d %H:%M:%S.%f')
                    entries[date] = line
                except ValueError:
                    if date:
                        entries[date] += line
                    continue
        return entries
