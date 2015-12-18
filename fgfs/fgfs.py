# -*- coding: utf-8 -*-
import protoxml
import subprocess
from common import mktmpfifos


class FlightGear(object):
    def __init__(self, initial_altitude=10000, receive_protocol="playback", send_protocol=None, receive_hz=10):
        self.initial_altitude = 1000
        self.receive_protocol = receive_protocol
        self.receive_protocol_file = '/usr/share/flightgear/data/Protocol/{}.xml'.format(receive_protocol)
        self.receive_file = None
        self.receive_hz = receive_hz
        self.send_protocol = send_protocol
        self.send_protocol_file = '/usr/share/flightgear/data/Protocol/{}.xml'.format(send_protocol)
        self.receive_file = None
        self.process = None

    def start(self):
        self.receive_file, self.send_file = mktmpfifos(('out.pipe', 'in.pipe'))
        args = [
            "fgfs",
            "--altitude=10000",
            "--enable-hud",
            "--disable-hud-3d",
            "--disable-panel",
            "--timeofday=noon",
            "--fg-scenery=/dev/null",
            "--generic=file,out,{},{},playback".format(self.receive_hz, self.receive_file)
        ]
        print (" ".join(args))

        self.process = subprocess.Popen(args)

    def stop(self):
        if self.process is not None:
            self.process.kill()
            self.process.wait()

    @property
    def receiver(self):
        with open(self.receive_file, 'r') as f:
            reader = protoxml.make_reader(self.receive_protocol_file, f)
            for d in reader:
                yield d


    def send(self, params):
        raise NotImplementedError()

