# -*- coding: utf-8 -*-


import subprocess


import os, tempfile

def mktmpfifos(filenames):
    tmpdir = tempfile.mkdtemp()
    filenames = [os.path.join(tmpdir, f) for f in filenames]
    for f in filenames:
        os.mkfifo(f)
    return filenames

def fgfs(filename_out):
    args = [
        "fgfs",
        "--altitude=10000",
        "--enable-hud",
        "--disable-hud-3d",
        "--disable-panel",
        "--timeofday=noon",
        "--fg-scenery=/dev/null",
        "--generic=file,out,10,{},playback".format(filename_out)
    ]
    print (" ".join(args))
    return subprocess.Popen(args)

def reader(filename_in):
    with open(filename_in, "r", buffering=0) as f:
        print "Opened file {}".format(filename_in)
        while True:
            data = f.readline()
            if len(data) == 0:
                break

            print repr(data)

        print "Closed file"


import protoxml


def main():
    outfilename, infilename = mktmpfifos(('out.pipe', 'in.pipe'))
    p = fgfs(outfilename)


    protocol = 'playback'
    protocol_file = '/usr/share/flightgear/data/Protocol/{}.xml'.format(protocol)

    outfile = open(outfilename, 'r')
    reader = protoxml.make_reader(protocol_file, outfile)

    try:
        for l in reader:
            print u"Heading: {:6.1f}° Pitch {:6.1f}°, Roll: {:6.1f}° (Speed {:6.1f}kt)".format(
                l["/orientation/heading-deg"],
                l["/orientation/pitch-deg"],
                l["/orientation/roll-deg"],
                l['/velocities/airspeed-kt']

            )
    except:
        p.kill()
        p.wait()
        raise

    p.kill()
    p.wait()


if __name__ == '__main__':
    main()
