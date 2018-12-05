# coding=utf-8
import argparse
import os
import sys

import yaml

import const
from sections import env, java, maven
from utils import yaml_util

parser = argparse.ArgumentParser(
    description="A tool for execution environment management")
parser.add_argument("exm_file")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="Print verbose log")
args = parser.parse_args()


def main():
    os.chdir(const.SCRIPT_DIR)
    print "Work dir: %s" % const.SCRIPT_DIR
    conf = yaml_util.load(args.exm_file)
    run(conf)
    pass


def run(conf):
    ctx = processctx(conf)
    if args.verbose:
        print "Execution configuration: %s" % conf
    pass


def processctx(conf):
    ctx = {}
    # FIXME: 这里应当采用自动装载sections执行
    env.process(conf, ctx)
    java.process(conf, ctx)
    maven.process(conf, ctx)
    return ctx


if __name__ == '__main__':
    sys.exit(main())
