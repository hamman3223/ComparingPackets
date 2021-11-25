import click
from subprocess import Popen,PIPE

      
class Script():
    def __init__(self, **kwargs) -> None:
        self.second_packet = kwargs['second_packet']
        self.first_packet = kwargs['first_packet']
        self.path_file = kwargs['path_file']
        self.second_path_file = kwargs['second_path_file']

    def run(self):
        if self.second_path_file==None:
            self.second_path_file = self.path_file
        self.create_first_file()
        self.create_second_file()
        self.compare_files()
        return self.k

    def create_first_file(self):
        proccess = Popen(f"editcap -r {self.path_file} - {self.first_packet} | tshark -r - -V > /tmp/first_packet.txt", stdin=PIPE, shell=True)
    def create_second_file(self):
        proccess = Popen(f"editcap -r {self.second_path_file} - {self.second_packet} | tshark -r - -V > /tmp/second_packet.txt", stdin=PIPE, shell=True)
    def compare_files(self):
        self.proccess = Popen(["diff", "-y", "--left-column", "/tmp/first_packet.txt", "/tmp/second_packet.txt"], stdout=PIPE, stderr=PIPE)
        self.stdout, self.stderr = self.proccess.communicate()
        self.k = self.stdout

@click.command()
@click.option('-1', '--first-packet', help='first packet')
@click.option('-2', '--second-packet', help='second packet')
@click.option('-pf', '--path_file', help='Second path to packet in pcapng format')
@click.option('-spf', '--second_path_file', help='Second path to packet in pcapng format')
def comparing(second_packet, path_file, first_packet, second_path_file):
    flags = {
        'first_packet': first_packet,
        'second_packet': second_packet,
        'path_file': path_file,
        'second_path_file': second_path_file
    }
    k = []
    starting_point = Script(**flags)
    k = starting_point.run()
    print(str(k, 'utf-8'))

comparing()
