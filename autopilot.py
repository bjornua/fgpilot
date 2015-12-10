# -*- coding: utf-8 -*-

import fgfs



def main():
    fg = fgfs.FlightGear()
    fg.start()

    try:
        for d in fg.receiver:
            print u"Heading: {:6.1f}° Pitch {:6.1f}°, Roll: {:6.1f}° (Speed {:6.1f}kt)".format(
                d["/orientation/heading-deg"],
                d["/orientation/pitch-deg"],
                d["/orientation/roll-deg"],
                d['/velocities/airspeed-kt']

            )
    except:
        fg.stop()
        raise


if __name__ == '__main__':
    main()
