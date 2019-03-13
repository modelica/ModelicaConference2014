# coding=utf-8

import subprocess, sys

assert(sys.argv[1].startswith("proceedings/"))
rel = ""
for i in range(2,sys.argv[1].count("/")):
  rel = rel + "../"

output = open(sys.argv[1]).read()
output = output.replace(' class="selected"', "").strip()
head = \
"""<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">

<html>
    <head>
        <title>The 10th International Modelica Conference 2014</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    </head>
    <body>
        <p>
            <a href="https://www.modelica.org/events/modelica2014" target="_blank">
                <img src="%sstatic/images/modelica2014.png" alt="Modelica2014" />
            </a>
        </p>
        <hr />
                        <ul>
                            <li><a href="%sindex.html">Home</a></li>
                            <li><a href="%ssessions/index.html">Sessions</a></li>
                            <li><a href="%sauthors/index.html">Authors</a></li>
                            <li><a href="%sschedule.html">Schedule</a></li>
                            <li><a href="%smaterial.html">Further material</a></li>
                        </ul>

        <hr />""" % (rel,rel,rel,rel,rel,rel)

foot = \
"""<hr />
        <h2>Organized by:</h2>
        <p>
            <a href="http://www.modelon.com"><img src="%sstatic/images/modelonlogo.png" alt="Modelon AB" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
            <a href="https://www.lccc.lth.se/"><img src="%sstatic/images/lccclogo.png" alt="Linnaeus center LCCC" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
            <a href="http://www.modelica.org"><img src="%sstatic/images/modelicalogo.png" alt="Modelica" /></a>
        </p>
        <hr />
        <h2>Sponsored by:</h2>
        <p>
            <a href="http://www.3ds.com/"><img src="%sstatic/images/3dslogo.png" alt="Dassault Syst&#232;mes" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
            <a href="http://www.esterel-technologies.com/"><img src="%sstatic/images/esterellogo.png" alt="Esterel Technologies" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
            <a href="http://www.maplesoft.com/"><img src="%sstatic/images/maplesoftlogo.png" alt="Maplesoft Europe" /></a>
        </p>
    </body>
</html>""" % (rel,rel,rel,rel,rel,rel)

#print(output)
#print(head)
#print(rel)

assert(head in output)
assert(foot in output)
output = output.replace(head, "").replace(foot, "")
output = output.strip()

mdfile = sys.argv[1].replace(".html",".md")
open(mdfile, "w").write(output)
subprocess.check_output(["git", "add", mdfile])
subprocess.check_output(["git", "rm", "-f", sys.argv[1]])
