from mrjob.job import MRJob

class MRSimpleJob(MRJob):

    def mapper(self, _, line):
        yield 'lines', 1
        yield 'words', len(line.split())
        yield 'chars', len(line)

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    MRSimpleJob.run()