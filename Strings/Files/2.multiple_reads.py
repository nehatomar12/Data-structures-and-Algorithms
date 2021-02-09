# https://github.com/saiyancode/LogIt/blob/master/logit.py
# https://coderwall.com/p/sme8mg/chunking-large-text-files-with-multiple-python-processes-and-redis
import multiprocessing

from multiprocessing import Pool
print(multiprocessing.cpu_count())


class ReadFile:
    def __init__(self):

        self.results = []

    def chunks(self, l, n):
            for i in range(0, len(l), n):
                yield l[i:i + n]

    def parse_chunk(self,data):
        results = []
        for line in data:
            try:
                parsed = dict()
                parsed['ip'] = line[0]
                parsed['date'], parsed['time'] = self.__parse_date_time(line[3].lstrip('['))
                parsed['url'] = line[6]
                parsed['status'] = line[8]
                parsed['request_size'] = line[9]
                parsed['user_agent'] = ' '.join(line[11:])
                parsed['verify'] = str(self.verify(parsed['user_agent'],parsed['ip']))
                results.append(parsed)
            except Exception as e:
                print(e)
        return results


    def run_process(self):
        file = open("../data_set/input.txt").readlines()
        listify = [line.split() for line in file]
        #print(len(listify))
        data = self.chunks(listify, int(len(listify) / (multiprocessing.cpu_count() - 2)))

        p = Pool(processes=multiprocessing.cpu_count() - 4)
        results = [p.apply_async(self.parse_chunk, args=(list(x),)) for x in data]

        # wait for results
        results = [item.get() for item in results]
        self.results = sum(results, [])

r = ReadFile()
r.run_process()
print(r.results)
