import argparse


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Process price... Anything else?")
    parser.add_argument('-p', '--price',
                        dest="price",
                        help="This defines the price for your computer.",
                        type=int,
                        default=1000)
    parser.add_argument('-w', '--windows',
                        dest="windows",
                        help="Use this flag if you need a windows operating system.",
                        action="store_true",
                        default=False)
    parser.add_argument('-r', '--ram-min',
                        dest="ram_gigs_minimum",
                        help="Use this flag to specify a minimum amount of ram.",
                        type=int,
                        default=4)
    parser.add_argument('-f', '--form-factor',
                        dest="fomr_factor",
                        help="Specify form factor according to the docs.",
                        type=int,
                        default=2)
    parser.add_argument('-s', '--ssd-required',
                        dest="ssd_required",
                        help="Use this flag to require an SSD",
                        action="store_true",
                        default=False)
    parser.add_argument('-g', '--graphics-card-manufacturer',
                        dest="graphics_card_manufacturer",
                        help="Use this to determine a graphics card manufacturer.",
                        type=int,
                        default=0)
    parser.add_argument('-c', '--cpu-type',
                        dest="cpu_type",
                        help="Use this to determine the CPU type.",
                        type=int,
                        default=13)

    args = parser.parse_args()
    print(args)
