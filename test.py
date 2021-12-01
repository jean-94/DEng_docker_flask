import unittest
import requests
import time
from statistics import mean
 
class TestApp(unittest.TestCase):
    def test_outputs(self):
        list = [42,0]
        link = 'http://localhost:4000/mean?values='
        first = True
        for value in list:
            if first:
                link += str(value)
                first = False
            else:
                link += ',' + str(value)
        self.assertEqual(float(str(requests.get(link).text).split('=')[-1].strip()), mean(list))

    def test_mean(self):
        link ='http://localhost:4000/'
        self.assertEqual(float(str(requests.get(link).text).split('=')[-1].strip()), 200)

    def test_load(self):
        time_process = []
        check = False
        for i in range(1000):
            values = [42,0]
            time_start = time.process_time()
            requests.get(f'http://localhost:4000/mean?values={values}')
            time_end = time.process_time()
            time_process.append(time_end - time_start)
        if mean(time_process) <= 0.1:
            check = True
        self.assertEqual(check, True)


if (__name__ == '__main__'):
    unittest.main()