"""
This problem was asked by Facebook.

Given an unordered list of flights taken by someone,
each represented as (origin, destination) pairs,
and a starting airport, compute the person's itinerary.
If no such itinerary exists, return null.
If there are multiple possible itineraries,
return the lexicographically smallest one.
All flights must be used in the itinerary.

For example, given the list of flights
[('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
and starting airport 'YUL',
you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')]
and starting airport 'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]
and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C']
even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary.
However, the first one is lexicographically smaller.
"""
import unittest
from typing import Dict, List, Optional, Tuple


def itinerary(flights: List[Tuple[str, str]],
              start: str) -> Optional[List[str]]:
    it = [start]
    while flights:
        next_f = None  # type: Optional[Tuple[int, str]]
        for i, f in enumerate(flights):
            # pylint: disable=E1136
            # this is done because pylint ignores control flow to
            # check if next_f is subscriptable in the next statement:
            if it[-1] == f[0] and (not next_f or f[1] < next_f[1]):
                next_f = (i, f[1])
        if not next_f:
            return None
        it.append(next_f[1])
        flights.pop(next_f[0])
    return it


class TestSolution(unittest.TestCase):
    def test_given1(self) -> None:
        self.assertEqual(
            itinerary(
                [
                    ('SFO', 'HKO'),
                    ('YYZ', 'SFO'),
                    ('YUL', 'YYZ'),
                    ('HKO', 'ORD')
                ], 'YUL'),
            ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'])

    def test_given2(self) -> None:
        self.assertEqual(
            itinerary([('SFO', 'COM'), ('COM', 'YYZ')], 'COM'),
            None)

    def test_given3(self) -> None:
        self.assertEqual(
            itinerary([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], 'A'),
            ['A', 'B', 'C', 'A', 'C'])

if __name__ == '__main__':
    unittest.main()
