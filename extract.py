import os
import sys

CUR_DIR = os.path.dirname(os.path.realpath(__file__))

def main():
    inputs = os.listdir(os.path.join(CUR_DIR, './tests/inputs/'))
    inputs = [input + '\n' for input in inputs]
    inputs[-1].strip('\n')

    file = open(os.path.join(CUR_DIR, 'inputs.txt'), 'w')
    file.writelines(inputs)
    file.close()

    sys.exit(len(inputs) - 1)

if __name__ == '__main__':
    main()