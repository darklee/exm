# coding=utf-8
import os
import shlex
import subprocess


def process(conf, ctx):
    ensureJavaVersion(conf)
    if not conf["java"].get("bin"):
        conf["java"]["bin"] = "%s/bin/java" % conf["env"]["JAVA_HOME"]
    pass


def ensureJavaVersion(conf):
    javaHome = conf["env"]["JAVA_HOME"]
    version = str(conf["java"]["version"])
    # FIXME: 探测Java的版本号
    shell_cmd = '"%s/bin/java" -version' % javaHome
    cmd = shlex.split(shell_cmd)
    p = subprocess.Popen(
        cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while p.poll() is None:
        line = p.stdout.readline()
        line = line.strip()
        if line.startswith("java version"):
            if line.find(version) == -1:
                raise Exception(
                    "Java version is incorrect: %s, expected: %s" % (line, version))
    if p.returncode != 0:
        raise Exception("Detect java version failed, java: %s" % javaHome)
