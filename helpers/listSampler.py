import argparse

from random import shuffle


def cli(argv=None):
    """ _summary_

    Args:
        argv (optional):

    Returns: Arguments passed through the command-line interface (CLI).
    """

    parser = argparse.ArgumentParser(prog="sampler",
                                     description="From a list of file names,"
                                                 " split into a supervised and unsupervised list of files.")

    parser.add_argument("--input", type=str, nargs=1,
                        help="Path to the file containing the list of file names.")

    parser.add_argument("--output_dir", type=str, nargs=1,
                        help="Path to the output directory.")

    parser.add_argument("--percent", type=int, nargs=1,
                        help="Percentage from 0 to 1, the supervised list will contain that percentage of the file"
                             " names. The unsupervised list will contain the remaining file names.")

    return parser.parse_args(argv)


def main(argv) -> None:
    args = cli(argv)

    try:
        with open(args.input[0], "r") as input_file:
            file_list = input_file.readlines()
            file_list = [item.strip("\n") for item in file_list]
    except IOError as e:
        raise IOError(e)

    shuffle(file_list)

    supervised = []
    nb_files_to_pick = int(len(file_list) * args.percent[0] / 100)

    for index in range(nb_files_to_pick):
        popped = file_list.pop(index)
        supervised.append(popped)

    output_supervised = open(f"{args.output_dir[0]}/{args.percent[0]}_supervised.txt", "w")
    for item in supervised:
        output_supervised.write(item + "\n")

    output_unsupervised = open(f"{args.output_dir[0]}/{args.percent[0]}_unsupervised.txt", "w")
    for item in file_list:
        output_unsupervised.write(item + "\n")


if __name__ == '__main__':
    main(["--input", "test_folder/input.txt",
          "--output_dir", "test_folder/",
          "--percent", "10"])
