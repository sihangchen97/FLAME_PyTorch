from argparse import ArgumentParser
import os

if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument('-s', "--src_pkl", type=str, default="")
    parser.add_argument('-d', "--dst_pkl", type=str, default="")
    opt = parser.parse_args()

    if not os.path.exists(opt.src_pkl):
        print("src file not exists")
        exit()

    content = ''
    with open(opt.src_pkl, 'rb') as infile:
        content = infile.read()
    with open(opt.dst_pkl, 'wb') as output:
        for line in content.splitlines():
            output.write(line + str.encode('\n'))

    print("rewrite successfully!")


